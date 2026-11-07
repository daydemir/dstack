# Helper usage

These helpers target Apple silicon Macs with Python 3.12, Node/npm, and ffmpeg (including ffprobe). Create the environment outside the skill checkout:

```sh
python3.12 -m venv "$HOME/.cache/explainer-video/venv"
"$HOME/.cache/explainer-video/venv/bin/pip" install -r /absolute/path/to/explainer-video/scripts/requirements.txt
```

Write `sentences.json` as a JSON array of nonempty strings, one spoken sentence per entry. Spell numbers and abbreviations as they should be spoken. Keep the output directory outside the skill checkout.

```sh
"$HOME/.cache/explainer-video/venv/bin/python" /absolute/path/to/explainer-video/scripts/narrate.py sentences.json /absolute/path/to/output
"$HOME/.cache/explainer-video/venv/bin/python" /absolute/path/to/explainer-video/scripts/check-audio.py /absolute/path/to/output/timing.json
```

Narration defaults to the approved `af_heart` voice at 1.2x, with a 0.3-second gap between sentences. The first run downloads Kokoro v1.0 files from the upstream release into `~/.cache/explainer-video/models`; `--model-dir` can reuse existing files. Use a fresh output directory for each run. It writes individual sentence WAVs, a combined `narration.wav` normalized to -16 LUFS, and `timing.json`. Sentence `start` and `end` are seconds in the combined audio, excluding the following gap; `duration` includes all gaps. Drive animation and captions from those measured times.

The checker uses local MLX Whisper (`mlx-community/whisper-large-v3-turbo`, downloaded if missing). It transcribes each sentence and the combined track without supplying the expected text to the recognizer, then writes `audio-check.json`. A word error rate above 10% flags review and exits nonzero; inspect substitutions, omissions, and names even below that threshold. A transcript mismatch may be a recognizer error. Change the spoken spelling or regenerate affected sentences, then regenerate the combined track and timings.

After muxing, check the actual MP4 too. AAC encoding can introduce peak overshoot; if the checker flags a peak at 0 dB, lower the export gain or apply a limiter before encoding, then check the new MP4 again.

```sh
"$HOME/.cache/explainer-video/venv/bin/python" /absolute/path/to/explainer-video/scripts/check-audio.py /absolute/path/to/output/timing.json --audio /absolute/path/to/final.mp4
```

This also compares final media duration with narration duration (0.5-second tolerance). The checker measures transcription agreement, peak level, and silence. It cannot judge naturalness, prosody, or whether the visuals teach well. Deniz approved the Heart 1.2x sample; a changed voice needs a listening sample before claiming the same quality.

Upstream references: [Kokoro ONNX setup and model files](https://github.com/thewh1teagle/kokoro-onnx), [MLX Whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper). Dependencies and model weights stay outside this repository. No fleet installation or sync is performed by this skill.
