# Helper usage

The helper targets Apple silicon Macs with Python 3.12 and ffmpeg (including ffprobe). It uses the same dependencies as `explainer-video`, so an existing `~/.cache/explainer-video/venv` works too. Otherwise create an environment outside the skill checkout:

```sh
python3.12 -m venv "$HOME/.cache/voice-memo/venv"
"$HOME/.cache/voice-memo/venv/bin/pip" install -r /absolute/path/to/voice-memo/scripts/requirements.txt
```

Write `sentences.json` as a JSON array of nonempty strings, one spoken sentence per entry. Each sentence is voiced separately with a pause after it, so link clauses with conjunctions rather than splitting them into fragments. Keep the output directory outside the skill checkout and use a fresh one for each run.

```sh
"$HOME/.cache/voice-memo/venv/bin/python" /absolute/path/to/voice-memo/scripts/memo.py sentences.json /absolute/path/to/output
```

It writes `memo.m4a` (AAC, normalized to -16 LUFS, 0.35-second gap between sentences) and `memo-check.json`. Kokoro v1.0 model files are downloaded on first run into `~/.cache/voice-memo/models`, unless `~/.cache/explainer-video/models` already has them; `--model-dir` overrides both.

The check uses local MLX Whisper (`mlx-community/whisper-large-v3-turbo`, downloaded if missing). It transcribes each sentence and the final `memo.m4a` without giving the recognizer the expected text, then compares word error rates. A rate above 10% for any sentence or for the whole memo, or a peak at or above 0 dB, flags review and exits nonzero. Inspect names and numbers even below that threshold, since a mismatch may be either a voicing problem or a recognizer error. Fix it by respelling or rephrasing, then rerun into a fresh directory. `--no-check` skips this step, but only use it when the user asked for speed over verification.

The check measures transcription agreement and peak level. It cannot judge naturalness or prosody. The Heart 1.2x sample was approved by ear, so a changed voice needs a listening sample before claiming the same quality.

Upstream references: [Kokoro ONNX setup and model files](https://github.com/thewh1teagle/kokoro-onnx), [MLX Whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper). Dependencies and model weights stay outside this repository.
