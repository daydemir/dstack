#!/usr/bin/env python3
"""Transcribe a YouTube video locally, or list a channel's or playlist's uploads.

Usage: python3 -I transcript.py URL OUTDIR

A video writes OUTDIR/meta.md (title, channel, date, duration, description) and
OUTDIR/transcript.txt. A channel or playlist writes OUTDIR/uploads.tsv
(id, title, url) of its newest uploads and transcribes nothing.
"""

import json
import shutil
import subprocess
import sys
import venv
from pathlib import Path

MODEL = "mlx-community/whisper-large-v3-turbo"
MLX_WHISPER = "mlx-whisper==0.4.3"
VENV = Path.home() / ".cache/youtube-transcript/venv"
UPLOADS_LISTED = 30
UPGRADE = (
    "HOMEBREW_NO_AUTO_UPDATE=1 HOMEBREW_NO_INSTALL_CLEANUP=1 "
    "HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK=1 brew upgrade yt-dlp"
)


def fail(message: str) -> None:
    sys.exit(f"youtube-transcript: {message}")


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
        [str(whisper()), str(audio), "--model", MODEL, "--output-format", "txt",
         "--output-name", "transcript", "--output-dir", str(out), "--verbose", "False"],
        stdout=subprocess.DEVNULL,
    )
    shutil.rmtree(audio_dir)


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: transcript.py URL OUTDIR")
    url, out = sys.argv[1], Path(sys.argv[2]).expanduser().resolve()
    missing = [tool for tool in ("yt-dlp", "ffmpeg") if not shutil.which(tool)]
    if missing:
        fail(f"missing {' '.join(missing)}; install with: brew install {' '.join(missing)}")
    out.mkdir(parents=True, exist_ok=True)
    info = json.loads(ytdlp(["-J", "--flat-playlist", "--playlist-end", str(UPLOADS_LISTED), url]))
    if info.get("_type", "video") != "video":
        write_uploads(info, out)
        return
    write_meta(info, url, out)
    transcribe(url, out)
    print(f"{info.get('title')} ({info.get('duration_string')}): {out / 'meta.md'}, {out / 'transcript.txt'}")


if __name__ == "__main__":
    main()
