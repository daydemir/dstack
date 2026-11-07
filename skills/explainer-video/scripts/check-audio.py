#!/usr/bin/env python3
"""Compare local Whisper transcripts to narration and check the delivered audio."""
import argparse
import json
from pathlib import Path
import re
import subprocess


def normalize(text):
    text = text.lower().replace("%", " percent").replace(",", "")
    return " ".join(re.sub(r"[^\w' ]", " ", text).split())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("timing", type=Path)
    parser.add_argument("--audio", type=Path, help="Check the final MP4 instead of the narration WAV")
    parser.add_argument("--max-wer", type=float, default=0.1)
    args = parser.parse_args()
    import mlx_whisper
    from jiwer import wer

    timing = json.loads(args.timing.read_text())
    root = args.timing.resolve().parent
    final = args.audio.resolve() if args.audio else root / timing["audio"]
    inputs = [(row["id"], root / row["audio"], row["text"])
              for row in timing["sentences"]]
    inputs.append(("combined", final, " ".join(row["text"] for row in timing["sentences"])))
    rows = []
    for identifier, path, expected in inputs:
        heard = mlx_whisper.transcribe(str(path),
            path_or_hf_repo="mlx-community/whisper-large-v3-turbo", language="en")["text"].strip()
        error = wer(normalize(expected), normalize(heard))
        rows.append({"id": identifier, "expected": expected, "transcript": heard,
                     "wer": error, "needs_review": error > args.max_wer})
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "csv=p=0", str(final)], capture_output=True, text=True, check=True)
    duration = float(probe.stdout)
    analysis = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(final), "-vn", "-af",
        "silencedetect=noise=-40dB:d=0.7,volumedetect", "-f", "null", "-"],
        capture_output=True, text=True, check=True).stderr
    peak = re.findall(r"max_volume: ([-\d.]+) dB", analysis)
    report = {"audio": str(final), "duration": duration,
              "duration_matches": abs(duration - timing["duration"]) <= 0.5,
              "peak_db": float(peak[-1]) if peak else None,
              "long_silences": analysis.count("silence_start:"), "transcripts": rows}
    report["needs_review"] = (any(row["needs_review"] for row in rows)
        or not report["duration_matches"] or report["peak_db"] is None
        or report["peak_db"] >= 0 or report["long_silences"] > 0)
    (root / "audio-check.json").write_text(json.dumps(report, indent=2) + "\n")
    for row in rows:
        print(f"{row['id']}: WER={row['wer']:.3f}, review={row['needs_review']}")
    print(f"Review needed: {report['needs_review']}; report: {root / 'audio-check.json'}")
    raise SystemExit(1 if report["needs_review"] else 0)


if __name__ == "__main__":
    main()
