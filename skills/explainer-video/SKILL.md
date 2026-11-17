---
name: explainer-video
description: For efficiently transferring knowledge or filling in the user when they might not remember or have full context, or if the user asks for video.
---

Make a video that leaves the viewer understanding the subject: afterwards they can explain it and sketch its shape. Every frame does explaining work the voice alone could not.

1. **Research.** Read the real sources and use only facts you found. What you couldn't verify goes in the delivery notes, not the video.
2. **Job.** Name the viewer and the one thing they must be able to do afterwards, list the few things they need for it, and cut the rest. Write this to `ask.md` with the user's request.
   - Re-learn a design: the parts, where each runs, one item end to end, what is undecided.
   - Change code safely: how it is organised, the path from the call, each rule a change must not break and the failure behind it.
   - Decide on a product: what it is, what it does in their system, cost, what data leaves, what it changes on their machines, what it won't do.
   - Understand a concept: the layout, one thing travelling through it, what drives it.
   - Be persuaded: see Pitch.
3. **Map.** Draw one architectural map of the *subject*, not an outline of your explanation: concepts spaced out, each nested inside what the source says contains it, umbrellas named, each kind of line meaning one keyed thing. Parts that behave separately are separate nodes, and the place where the point happens (an exchange, a decision, a handoff) gets its own drawing, not a label. If the whole map can't be read with every label at 28 px, it holds too much: cut or collapse. Render it still and check it against [the checks](references/checks.md) before writing any script.
4. **Example.** The idea that makes the subject work is seen working: carry one real, labelled example from the source through the map and show the mechanism decide something, with each branch's outcome. Where a rule exists because of a failure, show the failure beside the fix.
5. **Tour and script.** Build the map up in the order someone would sketch it, one region or relationship per sentence, and end on the whole map with the core path marked. Write to be spoken, in plain sentences (in the source's own words where the ask says whose words to use), main point first, joined with conjunctions rather than fragments, dashes, colons or parentheses. Each sentence names something drawn; if the picture can't show it, cut the sentence or draw it. Length as asked, else 3–10 minutes.
6. **Voice.** Run `scripts/narrate.py` (Kokoro `af_heart` at 1.2x, downloaded if missing). It generates one sentence at a time and writes `timing.json`, which sets all visual timing. Read [the helper usage](references/helpers.md) for setup and commands.
7. **Render.** Use `npx -y hyperframes@0.9.20` with `HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_TELEMETRY=1`, and pass `--skip-skills` to `init`. Same map throughout: fixed identities and places, highlight means "this sentence", and the camera shows place and level and has settled before the sentence starts.
8. **Check.** Run `scripts/check-audio.py`, then `hyperframes check --strict` at every sentence midpoint with no layout errors or text-size warnings, then `scripts/stills.py`.
9. **Critique.** You know what the drawing is meant to say, so you can't see what it fails to say. Run `scripts/critic.py`: it shows only the stills, `ask.md` and the sources to a fresh reader and writes `critique.md`. Fix every finding or say in the notes why not, re-render, and run it once more.
10. **Deliver.** Give the video with a few bullets on its overall concepts, plus 1–2 sentences on what you checked, what you didn't, and anything in the sources you couldn't verify.

**Pitch.** A pitch makes this viewer want the next conversation; it doesn't report status. Spend most of it on the experience and why it matters to a person: put the viewer inside one concrete moment of using the thing, drawn large, and carry the feeling with the source's most vivid lines rather than its driest. Open on the tension, charted, with an arrow from it to the idea. Say what exists today in one short, dated line: strengths lit, limits stated plainly but not lit. End on the human outcome and a specific invitation (what you want from this viewer), alone on the last frame. Quotes are evidence, not narration: short, attributed, never raw speech with its filler.
