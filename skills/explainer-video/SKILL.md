---
name: explainer-video
description: For efficiently transferring knowledge or filling in the user when they might not remember or have full context, or if the user asks for video.
---

Make a video that leaves the viewer understanding the subject. Use visuals that make the ideas being communicated more intuitive and clear.

1. **Research.** Read the real sources and use only facts you found. Say what you couldn't verify.
2. **Plan.** Find the one core idea, then show one main idea on screen at a time. For architecture or connected concepts, use a concept map: one continuous world where each concept keeps a fixed place and the camera's movement shows how ideas relate. Otherwise, use whatever is clearest.
3. **Script.** Write it to be spoken, main point first. Join related ideas with conjunctions (and, but, so, because, which) instead of stacking fragments or using dashes, colons, and parentheses, since the voice handles connected clauses more naturally than choppy sentences. Make it 3–10 minutes, whatever is most valuable given what the user cares about. Spell out anything a voice could misread.
4. **Voice.** Run `scripts/narrate.py` (Kokoro `af_heart` at 1.2x, downloaded if missing). It generates one sentence at a time and writes `timing.json`, which sets all visual timing. Read [the helper usage](references/helpers.md) for setup and commands.
5. **Render.** Use `npx -y hyperframes@0.9.20` with `HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_TELEMETRY=1`, and pass `--skip-skills` to `init`. Check stills before the final render.
6. **Check.** You can't hear audio, so run `scripts/check-audio.py` to compare a transcript against the script. Redo any wrong sentences.
7. **Deliver.** Give the video with a few bullets on its overall concepts, plus 1–2 sentences on what you checked and what you didn't.
