---
name: climb
description: "when user asks for a hill climb or climb, or if the user asks to do work towards some kind of measurable goal"
---

Turn the user's goal into a bounded search: try changes, evaluate them, retain
credible improvements, and present the best result when progress levels off.

## Shape the climb

Inspect the target project's instructions, dashboards, metric definitions,
existing evaluations, and tools before asking the user to explain them. Reuse
established measurements and identify their coverage, attribution, and delay.
Keep domain knowledge in the target project.

Propose the objective, editable surface, evaluator, regression constraints,
resource budget, and stopping rule. Prefer one primary metric with independent
constraints over a composite score that can hide regressions. Establish a
baseline before changing anything. Resolve routine choices yourself; ask only
for consequential ambiguity or authority that the existing request does not
supply. Activating this skill does not expand permission to spend, publish, or
change external systems.

Prefer a blind, repeatable script measuring the actual outcome. Keep its inputs
and scoring rules outside the candidate's editable surface. If quality cannot
be measured adequately that way, propose a council drawn from diverse available
model families within the user's allowed models and costs. Pin the rubric and
judge versions; anonymize candidates, vary presentation order, and retain
individual judgments and disagreements. Use judgments as a proxy only when
measured outcomes are unavailable; a persuasive proposal cannot replace observed
performance. Keep final validation independent of the feedback used to search.

## Climb unattended

Once the setup is clear and authorized, run without routine human intervention.
Choose the simplest execution method the environment supports. Persist enough
state that a fresh agent can recover the objective, baseline, best candidate,
failed approaches, resource use, and next experiment.

For each experiment, record the hypothesis, change or artifact reference,
evaluation evidence, score, resource use, and keep/discard decision. Compare
against the current best under comparable conditions. Use repeated measurements
or controlled experiments when noise, delayed outcomes, or changing conditions
could create a false win. Keep changes that improve the objective while passing
the constraints; restore the best candidate after failed attempts. Preserve the
user's unrelated work and record failed experiments rather than erasing them.

Treat evaluator drift, missing telemetry, and exhausted resources as distinct
from poor candidates. A proxy score or a tracking change must not manufacture a
win. For live experiments, respect authorized budgets and allow outcomes to
mature. Use a supported durable continuation when an observation window exceeds
the current run; claim automatic follow-up only after that continuation exists.

Stop at the declared target, plateau, or resource limit. A plateau means no
credible improvement found within this search's scope and budget, not proof of a
global optimum. Re-evaluate the best candidate independently before presenting
it, distinguishing confirmed gains from provisional or inconclusive results.

## Present and restart

Use a lab notebook and peak report as the default dashboard guidance. Read
[references/dashboard.md](references/dashboard.md) when creating the climb's
presentation; adapt it to the existing project rather than requiring a new app.

Present the best artifact, baseline comparison, validation, constraints checked,
why the climb stopped, failed approaches worth remembering, and promising next
hypotheses. Leave the result at the endpoint authorized by the user and the
project's delivery rules. On restart, carry forward the evidence and lessons;
version changed objectives or evaluators and establish a comparable baseline.
