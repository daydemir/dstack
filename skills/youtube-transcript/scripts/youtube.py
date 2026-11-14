#!/usr/bin/env python3
"""Read a YouTube video locally: its transcript, and frames of what is on screen.

Usage:
  python3 -I youtube.py transcript URL OUTDIR
  python3 -I youtube.py frames URL OUTDIR (--at TIME... | --every SECONDS | --scenes)

transcript writes OUTDIR/meta.md (title, channel, date, duration, description)
and OUTDIR/transcript.txt, one "[M:SS] text" line per segment. A channel or
playlist instead writes OUTDIR/uploads.tsv (id, title, url) of its newest
uploads and transcribes nothing.

frames writes OUTDIR/frames/HH-MM-SS.jpg. The video is downloaded once to
OUTDIR/video/ and reused by later frames runs into the same OUTDIR.
"""

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import venv
from pathlib import Path

MODEL = "mlx-community/whisper-large-v3-turbo"
MLX_WHISPER = "mlx-whisper==0.4.3"
VENV = Path.home() / ".cache/youtube-transcript/venv"
UPLOADS_LISTED = 30
VIDEO_FORMAT = "bv*[height<=720]"
FRAME_WIDTH = 1280
SCENE_THRESHOLD = 0.3
UPGRADE = (
    "HOMEBREW_NO_AUTO_UPDATE=1 HOMEBREW_NO_INSTALL_CLEANUP=1 "
    "HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK=1 brew upgrade yt-dlp"
)


def fail(message: str) -> None:
    sys.exit(f"youtube: {message}")


def run(args: list, **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(args, check=True, **kwargs)


def ytdlp(args: list) -> str:
    result = subprocess.run(["yt-dlp", "--no-update", *args], capture_output=True, text=True)
    if result.returncode != 0:
        version = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True).stdout.strip()
        fail(
            f"yt-dlp {version} failed:\n{result.stderr.strip()}\n"
            f"An old yt-dlp is the usual cause; upgrade it with:\n  {UPGRADE}"
        )
    return result.stdout


def seconds(text: str) -> float:
    """Parse SECONDS, M:SS or H:MM:SS."""
    if not re.fullmatch(r"\d+(\.\d+)?|(\d+:[0-5])?\d:[0-5]\d(\.\d+)?", text):
        raise argparse.ArgumentTypeError(f"{text!r} is not SECONDS, M:SS or H:MM:SS")
    total = 0.0
    for part in text.split(":"):
        total = total * 60 + float(part)
    return total


def clock(t: float) -> str:
    h, rest = divmod(int(t), 3600)
    m, s = divmod(rest, 60)
    return f"{h}:{m:02}:{s:02}" if h else f"{m}:{s:02}"


def video_info(url: str) -> dict:
    return json.loads(ytdlp(["-J", "--flat-playlist", "--playlist-end", str(UPLOADS_LISTED), url]))


def is_video(info: dict) -> bool:
    return info.get("_type", "video") == "video"


def whisper() -> Path:
    exe = VENV / "bin/mlx_whisper"
    if not exe.exists():
        venv.create(VENV, with_pip=True, clear=True)
        run([str(VENV / "bin/pip"), "install", "--quiet", MLX_WHISPER])
    return exe


def videos(info: dict) -> list:
    """A channel root nests its tabs (Videos, Shorts) as playlists; flatten them."""
    return [
        video
        for entry in info.get("entries") or []
        for video in (videos(entry) if "entries" in entry else [entry])
    ]


def write_uploads(info: dict, out: Path) -> None:
    rows = [f"{v['id']}\t{v.get('title') or ''}\thttps://youtu.be/{v['id']}" for v in videos(info)]
    (out / "uploads.tsv").write_text("\n".join(rows) + "\n")
    print(f"{info.get('title')}: not a video; listed {len(rows)} uploads in {out / 'uploads.tsv'}")


def write_meta(info: dict, url: str, out: Path) -> None:
    date = info.get("upload_date") or ""
    lines = [
        f"# {info.get('title')}",
        "",
        f"- Channel: {info.get('channel')} ({info.get('channel_url')})",
        f"- URL: {url}",
        f"- Uploaded: {date[:4]}-{date[4:6]}-{date[6:]}",
        f"- Duration: {info.get('duration_string')}",
        "",
        "## Description",
        "",
        info.get("description") or "",
    ]
    (out / "meta.md").write_text("\n".join(lines) + "\n")


def transcribe(url: str, out: Path) -> None:
    audio_dir = out / "audio"
    ytdlp(["-f", "bestaudio", "-P", str(audio_dir), "-o", "audio.%(ext)s", url])
    (audio,) = audio_dir.iterdir()
    run(
        [str(whisper()), str(audio), "--model", MODEL, "--output-format", "json",
         "--output-name", "transcript", "--output-dir", str(out), "--verbose", "False"],
        stdout=subprocess.DEVNULL,
    )
    shutil.rmtree(audio_dir)
    raw = out / "transcript.json"
    segments = json.loads(raw.read_text())["segments"]
    lines = [f"[{clock(s['start'])}] {s['text'].strip()}" for s in segments]
    (out / "transcript.txt").write_text("\n".join(lines) + "\n")
    raw.unlink()


def transcript(url: str, out: Path) -> None:
    info = video_info(url)
    if not is_video(info):
        write_uploads(info, out)
        return
    write_meta(info, url, out)
    transcribe(url, out)
    print(f"{info.get('title')} ({info.get('duration_string')}): {out / 'meta.md'}, {out / 'transcript.txt'}")


def download_video(url: str, out: Path) -> Path:
    video_dir = out / "video"
    if not video_dir.exists():
        if not is_video(video_info(url)):
            fail(f"{url} is not a video; run transcript on it to list its uploads")
        ytdlp(["-f", VIDEO_FORMAT, "-P", str(video_dir), "-o", "video.%(ext)s", url])
    (video,) = video_dir.iterdir()
    return video


def duration(video: Path) -> float:
    probe = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)],
                capture_output=True, text=True)
    return float(probe.stdout)


def scene_changes(video: Path) -> list:
    """Timestamps where the picture changes, starting with the first frame, one per second at most."""
    detect = run(["ffmpeg", "-nostats", "-i", str(video), "-an", "-vf",
                  f"select='gt(scene,{SCENE_THRESHOLD})',showinfo", "-f", "null", "-"],
                 capture_output=True, text=True)
    changes = [0.0, *(float(t) for t in re.findall(r"pts_time:([\d.]+)", detect.stderr))]
    return [t for i, t in enumerate(changes) if i == 0 or int(t) != int(changes[i - 1])]


def extract(video: Path, times: list, frames: Path) -> list:
    frames.mkdir(exist_ok=True)
    paths = []
    for t in times:
        h, rest = divmod(int(t), 3600)
        path = frames / f"{h:02}-{rest // 60:02}-{rest % 60:02}.jpg"
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(video), "-frames:v", "1",
             "-vf", f"scale='min({FRAME_WIDTH},iw)':-2", "-q:v", "3", str(path)])
        paths.append(path)
    return paths


def frames(url: str, out: Path, at: list, every: float, scenes: bool) -> None:
    video = download_video(url, out)
    length = duration(video)
    if at:
        late = [clock(t) for t in at if t >= length]
        if late:
            fail(f"{', '.join(late)} past the end of the video ({clock(length)})")
        times = at
    elif every is not None:
        times = [i * every for i in range(math.ceil(length / every))]
    else:
        times = scene_changes(video)
    paths = extract(video, times, out / "frames")
    print(f"{len(paths)} frames of {clock(length)} in {out / 'frames'}:")
    print("\n".join(f"  {clock(t)}  {p.name}" for t, p in zip(times, paths)))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("transcript", "frames"):
        command = commands.add_parser(name)
        command.add_argument("url")
        command.add_argument("outdir", type=lambda p: Path(p).expanduser().resolve())
    pick = commands.choices["frames"].add_mutually_exclusive_group(required=True)
    pick.add_argument("--at", nargs="+", type=seconds, metavar="TIME", help="SECONDS, M:SS or H:MM:SS")
    pick.add_argument("--every", type=seconds, metavar="SECONDS")
    pick.add_argument("--scenes", action="store_true", help="one frame per scene change")
    args = parser.parse_args()
    if args.command == "frames" and args.every is not None and args.every <= 0:
        parser.error("--every must be more than 0 seconds")

    missing = [tool for tool in ("yt-dlp", "ffmpeg", "ffprobe") if not shutil.which(tool)]
    if missing:
        fail(f"missing {' '.join(missing)}; install with: brew install yt-dlp ffmpeg")
    args.outdir.mkdir(parents=True, exist_ok=True)
    if args.command == "transcript":
        transcript(args.url, args.outdir)
    else:
        frames(args.url, args.outdir, args.at, args.every, args.scenes)


if __name__ == "__main__":
    main()
