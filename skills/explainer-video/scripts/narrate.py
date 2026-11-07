#!/usr/bin/env python3
"""Generate sentence audio and measured visual timing with Kokoro Heart at 1.2x."""
import argparse
import json
from pathlib import Path
import subprocess
import urllib.request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sentences", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--model-dir", type=Path,
                        default=Path.home() / ".cache/explainer-video/models")
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

    args.model_dir.mkdir(parents=True, exist_ok=True)
    files = ["kokoro-v1.0.onnx", "voices-v1.0.bin"]
    for name in files:
        target = args.model_dir / name
        if not target.exists():
            partial = target.with_suffix(target.suffix + ".part")
            urllib.request.urlretrieve(
                "https://github.com/thewh1teagle/kokoro-onnx/releases/download/"
                "model-files-v1.0/" + name, partial)
            partial.replace(target)
    engine = Kokoro(*(str(args.model_dir / name) for name in files))
    args.output.mkdir(parents=True, exist_ok=True)
    chunks, sentences = [], []
    cursor = 0
    sample_rate = None
    for index, line in enumerate(lines):
        audio, rate = engine.create(line, voice="af_heart", speed=1.2, lang="en-us")
        if not len(audio) or not np.isfinite(audio).all():
            raise RuntimeError(f"Invalid audio for sentence {index + 1}")
        if sample_rate is not None and sample_rate != rate:
            raise RuntimeError("Sample rate changed between sentences")
        sample_rate = rate
        name = f"sentence-{index + 1:03d}.wav"
        sf.write(args.output / name, audio, rate, subtype="PCM_16")
        sentences.append({"id": index + 1, "text": line, "audio": name,
                          "start": cursor / rate, "end": (cursor + len(audio)) / rate})
        chunks.append(audio)
        cursor += len(audio)
        if index < len(lines) - 1:
            gap = np.zeros(round(rate * 0.3), dtype=np.float32)
            chunks.append(gap)
            cursor += len(gap)
    raw = args.output / "narration-raw.wav"
    sf.write(raw, np.concatenate(chunks), sample_rate, subtype="PCM_16")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(raw), "-af",
                    "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(sample_rate),
                    str(args.output / "narration.wav")], check=True)
    raw.unlink()
    timing = {"voice": "af_heart", "speed": 1.2, "sample_rate": sample_rate,
              "audio": "narration.wav", "duration": cursor / sample_rate,
              "sentences": sentences}
    (args.output / "timing.json").write_text(json.dumps(timing, indent=2) + "\n")
    print(f"Generated {len(lines)} sentences, {timing['duration']:.2f} seconds")


if __name__ == "__main__":
    main()
