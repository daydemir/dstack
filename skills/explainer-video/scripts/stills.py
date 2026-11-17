#!/usr/bin/env python3
"""One frame per narration sentence, contact sheets and a transcript, for review.

Usage: stills.py <video.mp4> <timing.json> <outdir>

Writes <outdir>/frame-<id>-<second>.png at each sentence's midpoint,
<outdir>/sheet-<n>.png tiling them labelled with the second only, and
<outdir>/transcript.md with each sentence and its time span. Frames and sheets
carry no narration text, so they can be read with the sound off.
"""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

COLS, TILE_W, PER_SHEET, LABEL_H = 3, 640, 15, 30


def main():
    video, timing, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    out.mkdir(parents=True, exist_ok=True)
    frames, lines = [], ["# Narration", ""]
    for s in json.loads(timing.read_text())["sentences"]:
        mid = (s["start"] + s["end"]) / 2
        f = out / f"frame-{s['id']:03d}-{mid:07.2f}.png"
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{mid:.3f}",
                        "-i", str(video), "-frames:v", "1", str(f)], check=True)
        frames.append((f, mid))
        lines.append(f"- [{s['start']:.1f}–{s['end']:.1f}s] {s['text']}")
    (out / "transcript.md").write_text("\n".join(lines) + "\n")
    font = ImageFont.load_default(size=20)
    for n in range(0, len(frames), PER_SHEET):
        chunk = frames[n:n + PER_SHEET]
        w, h = Image.open(chunk[0][0]).size
        th = TILE_W * h // w
        rows = -(-len(chunk) // COLS)
        sheet = Image.new("RGB", (COLS * TILE_W, rows * (th + LABEL_H)), "white")
        d = ImageDraw.Draw(sheet)
        for i, (f, mid) in enumerate(chunk):
            x, y = (i % COLS) * TILE_W, (i // COLS) * (th + LABEL_H)
            d.text((x + 6, y + 4), f"{mid:.1f}s", fill="black", font=font)
            sheet.paste(Image.open(f).convert("RGB").resize((TILE_W, th)), (x, y + LABEL_H))
        sheet.save(out / f"sheet-{n // PER_SHEET + 1}.png")
    print(f"{len(frames)} frames, {-(-len(frames) // PER_SHEET)} sheets and transcript.md in {out}")


if __name__ == "__main__":
    main()
