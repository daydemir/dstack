#!/usr/bin/env python3
"""Review stills for a narrated explainer: what each sentence shows, and what moves while it plays.

Usage: stills.py <final.mp4 | project-dir> <timing.json> <outdir>

For each narration sentence, takes frames at 20%, 50% and 80% of it and writes
<outdir>/frame-<id>-<second>.png (the midpoint), <outdir>/motion-<id>.png (the three
side by side, labelled with seconds), contact sheets of the midpoints, and
transcript.md. Given a project directory instead of a video, the frames come from
`hyperframes snapshot`, so a storyboard can be reviewed before rendering.
"""
import json, os, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

COLS, TILE_W, PER_SHEET, LABEL_H, STRIP_W = 3, 640, 15, 30, 960
FRACTIONS = (0.2, 0.5, 0.8)
HYPERFRAMES = ["npx", "-y", "hyperframes@0.9.20"]


def from_video(video: Path, times: list[float], tmp: Path) -> list[Path]:
    paths = [tmp / f"{i:04d}.png" for i in range(len(times))]
    for t, p in zip(times, paths):
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{t:.3f}",
                        "-i", str(video), "-frames:v", "1", str(p)], check=True)
    return paths


def from_project(project: Path, times: list[float], tmp: Path) -> list[Path]:
    env = {**os.environ, "HYPERFRAMES_SKIP_SKILLS": "1", "HYPERFRAMES_NO_TELEMETRY": "1"}
    out = subprocess.run([*HYPERFRAMES, "snapshot", "--at", ",".join(f"{t:.3f}" for t in times),
                          "--no-end", "--json", "-o", str(tmp), str(project)],
                         check=True, capture_output=True, text=True, env=env).stdout
    frames = json.loads(out[out.index("{"):])["frames"]
    if len(frames) != len(times):
        raise SystemExit(f"snapshot returned {len(frames)} frames for {len(times)} times")
    return [Path(f["path"]) for f in frames]


def main():
    source, timing, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    out.mkdir(parents=True, exist_ok=True)
    for stale in [*out.glob("frame-*.png"), *out.glob("motion-*.png"), *out.glob("sheet-*.png")]:
        stale.unlink()
    sentences = json.loads(timing.read_text())["sentences"]
    times = [s["start"] + f * (s["end"] - s["start"]) for s in sentences for f in FRACTIONS]
    font = ImageFont.load_default(size=20)
    mids, lines = [], ["# Narration", ""]
    with tempfile.TemporaryDirectory() as tmp:
        grab = from_project if source.is_dir() else from_video
        shots = grab(source, times, Path(tmp))
        for n, s in enumerate(sentences):
            trio = list(zip(times[3 * n:3 * n + 3], shots[3 * n:3 * n + 3]))
            mid_t, mid_p = trio[1]
            frame = out / f"frame-{s['id']:03d}-{mid_t:07.2f}.png"
            Image.open(mid_p).convert("RGB").save(frame)
            mids.append((frame, mid_t))
            w, h = Image.open(mid_p).size
            th = STRIP_W * h // w
            strip = Image.new("RGB", (STRIP_W * 3, th + LABEL_H), "white")
            d = ImageDraw.Draw(strip)
            for i, (t, p) in enumerate(trio):
                strip.paste(Image.open(p).convert("RGB").resize((STRIP_W, th)), (i * STRIP_W, LABEL_H))
                d.text((i * STRIP_W + 6, 4), f"{t:.1f}s", fill="black", font=font)
            strip.save(out / f"motion-{s['id']:03d}.png")
            lines.append(f"- [{s['start']:.1f}–{s['end']:.1f}s] {s['text']}")
    (out / "transcript.md").write_text("\n".join(lines) + "\n")
    for n in range(0, len(mids), PER_SHEET):
        chunk = mids[n:n + PER_SHEET]
        w, h = Image.open(chunk[0][0]).size
        th = TILE_W * h // w
        sheet = Image.new("RGB", (COLS * TILE_W, -(-len(chunk) // COLS) * (th + LABEL_H)), "white")
        d = ImageDraw.Draw(sheet)
        for i, (f, t) in enumerate(chunk):
            x, y = (i % COLS) * TILE_W, (i // COLS) * (th + LABEL_H)
            d.text((x + 6, y + 4), f"{t:.1f}s", fill="black", font=font)
            sheet.paste(Image.open(f).convert("RGB").resize((TILE_W, th)), (x, y + LABEL_H))
        sheet.save(out / f"sheet-{n // PER_SHEET + 1}.png")
    print(f"{len(mids)} sentences: frames, motion strips, sheets and transcript.md in {out}")


if __name__ == "__main__":
    main()
