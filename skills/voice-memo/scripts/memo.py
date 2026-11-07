#!/usr/bin/env python3
"""Voice a script as a Kokoro Heart 1.2x memo, then check it with local Whisper."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import urllib.request

FILES = ["kokoro-v1.0.onnx", "voices-v1.0.bin"]
CACHE = Path.home() / ".cache"


def normalize(text):
    text = text.lower().replace("%", " percent").replace(",", "")
    return " ".join(re.sub(r"[^\w' ]", " ", text).split())


def model_dir(chosen):
    if chosen:
        return chosen
    shared = CACHE / "explainer-video/models"
    if all((shared / name).exists() for name in FILES):
        return shared
    return CACHE / "voice-memo/models"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sentences", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--model-dir", type=Path)
    parser.add_argument("--max-wer", type=float, default=0.1)
    parser.add_argument("--no-check", action="store_true")
    args = parser.parse_args()
    lines = json.loads(args.sentences.read_text())
    if not isinstance(lines, list) or not lines or any(
            not isinstance(line, str) or not line.strip() for line in lines):
        parser.error("sentences must be a nonempty JSON array of nonempty strings")
    if args.output.exists() and any(args.output.iterdir()):
        parser.error("use an empty output directory")

    import numpy as np
    import soundfile as sf
    from kokoro_onnx import Kokoro

    models = model_dir(args.model_dir)
    models.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        target = models / name
        if not target.exists():
            partial = target.with_suffix(target.suffix + ".part")
            urllib.request.urlretrieve(
                "https://github.com/thewh1teagle/kokoro-onnx/releases/download/"
                "model-files-v1.0/" + name, partial)
            partial.replace(target)
    engine = Kokoro(*(str(models / name) for name in FILES))
    parts = args.output / "sentences"
    parts.mkdir(parents=True, exist_ok=True)
    chunks, rate = [], None
    for index, line in enumerate(lines):
        audio, sample_rate = engine.create(line, voice="af_heart", speed=1.2, lang="en-us")
        if not len(audio) or not np.isfinite(audio).all():
            raise RuntimeError(f"Invalid audio for sentence {index + 1}")
        if rate is not None and rate != sample_rate:
            raise RuntimeError("Sample rate changed between sentences")
        rate = sample_rate
        sf.write(parts / f"{index + 1:03d}.wav", audio, rate, subtype="PCM_16")
        chunks.append(audio)
        if index < len(lines) - 1:
            chunks.append(np.zeros(round(rate * 0.35), dtype=np.float32))
    raw = args.output / "memo-raw.wav"
    sf.write(raw, np.concatenate(chunks), rate, subtype="PCM_16")
    memo = args.output / "memo.m4a"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(raw), "-af",
                    "loudnorm=I=-16:TP=-2:LRA=11", "-ar", "48000",
                    "-c:a", "aac", "-b:a", "128k", str(memo)], check=True)
    raw.unlink()
    duration = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(memo)], capture_output=True, text=True, check=True).stdout)
    print(f"Wrote {memo} ({len(lines)} sentences, {duration:.1f} seconds)")
    if args.no_check:
        return

    import mlx_whisper
    from jiwer import wer

    inputs = [(index + 1, parts / f"{index + 1:03d}.wav", line)
              for index, line in enumerate(lines)]
    inputs.append(("memo", memo, " ".join(lines)))
    rows = []
    for identifier, path, expected in inputs:
        heard = mlx_whisper.transcribe(str(path),
            path_or_hf_repo="mlx-community/whisper-large-v3-turbo", language="en")["text"].strip()
        error = wer(normalize(expected), normalize(heard))
        rows.append({"id": identifier, "expected": expected, "transcript": heard,
                     "wer": error, "needs_review": error > args.max_wer})
    analysis = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(memo), "-af",
                               "volumedetect", "-f", "null", "-"],
                              capture_output=True, text=True, check=True).stderr
    peak = re.findall(r"max_volume: ([-\d.]+) dB", analysis)
    report = {"audio": str(memo.resolve()), "duration": duration,
              "peak_db": float(peak[-1]) if peak else None, "transcripts": rows}
    report["needs_review"] = (any(row["needs_review"] for row in rows)
                              or report["peak_db"] is None or report["peak_db"] >= 0)
    (args.output / "memo-check.json").write_text(json.dumps(report, indent=2) + "\n")
    for row in rows:
        if row["needs_review"]:
            print(f"{row['id']}: WER={row['wer']:.3f}\n  expected: {row['expected']}\n"
                  f"  heard:    {row['transcript']}")
    print(f"Review needed: {report['needs_review']}; peak {report['peak_db']} dB")
    raise SystemExit(1 if report["needs_review"] else 0)


if __name__ == "__main__":
    main()
