---
name: climb
description: "when user asks for a hill climb or climb, or if the user asks to do work towards some kind of measurable goal"
---

Improve what the user actually cares about through repeated, scored experiments.

## Decide what matters

Work out the value behind the user's goal and pick the measure closest to it.
Use a real outcome or other quantifiable metric wherever one exists. When quality
cannot be quantified, use a blind AI council: judges from diverse model families,
one fixed scoring prompt, and anonymized candidates in varied order.

Keep the measure out of the candidates' reach, and score a baseline before
changing anything.

Present this to the user and wait for their approval before climbing:

- **Measure:** the number and exactly how it is calculated, or the council score
  and the exact prompt the judges receive.
- **Baseline:** the current score.
- **Goal:** the score to hit.

## Climb unattended

Once approved, run until done, without check-ins. Try a change, score it under
the same conditions as the current best, keep it if it wins, and restore the best
if it does not. Log every attempt, including failures, so a fresh agent can
resume: hypothesis, change, score, and decision. A broken or changed measure
produces no score.

Stop when the goal is hit, progress levels off, or the budget runs out. Confirm
the best candidate with a fresh measurement before calling it a win.

## Report

Build a dashboard or report, using the project's existing surface when it has
one. Plot every attempt and best-so-far. Show baseline against best, what worked,
what failed, why the climb stopped, and what to try next. Label inconclusive
results as inconclusive.
