---
name: climb
description: "when user asks for a hill climb or climb, or if the user asks to do work towards some kind of measurable goal"
---

Turn the goal into a bounded search: try changes, evaluate them, keep credible
improvements, and present the best result when progress levels off.

## Set up

Learn the project's existing metrics, evaluations, dashboards, and tools,
including their coverage, attribution, and delay. Propose the objective,
editable surface, evaluator, regression constraints, budget, and stopping rule.
Use one primary metric with independent constraints, since a composite score can
hide regressions. Ask only about consequential ambiguity. Spending, publishing,
and changing external systems need authority beyond this skill.

The evaluator is a blind, repeatable script measuring the actual outcome, with
its inputs and scoring outside the editable surface. When a script cannot measure
quality, propose a council of diverse model families within the allowed models
and costs: pin the rubric and judge versions, anonymize candidates, vary their
order, and retain every judgment and disagreement.

Measure a baseline before changing anything.

## Run

Run unattended once authorized. Keep an experiment record that lets a fresh
agent resume: objective, baseline, best candidate, next experiment, and for every
attempt, including failures, the hypothesis, change, evidence, score, resource
use, and keep/discard decision.

Compare each candidate with the current best under comparable conditions; scores
from different metrics, evaluators, or observation windows are not comparable.
Repeat measurements or use controls when noise, delay, or shifting conditions
could create a false win. Keep changes that improve the objective and pass the
constraints. Otherwise restore the best candidate, preserving unrelated work.

Record evaluator drift, missing telemetry, failed evaluations, and exhausted
resources as blockers, with no score for the candidate. Only a measured outcome
on the unchanged evaluator counts as a win; a council score is provisional. Let
live outcomes mature, and create a durable continuation before promising
follow-up beyond the current run.

Stop at the target, plateau, or budget. A plateau means no credible improvement
within this search's scope and budget.

## Report

Validate the best candidate on evidence the search never used. Separate confirmed
gains from provisional and inconclusive results, and credit individual changes
only when experiments isolate them.

Build both views from the experiment record, in the project's existing reporting
surface or a lightweight local report.

- **Lab notebook, during the search:** objective, metric direction and units,
  baseline, best result, state, stopping rule, editable surface, and constraints.
  Plot every attempt and best-so-far, marking retained, rejected, failed, and
  maturing attempts by label or shape as well as color. Each attempt opens to its
  record, plus repeat-run variation, individual council judges and agreement, or
  live cohort dates, window, coverage, and pending measurements where they apply.
- **Peak report, at the end:** baseline against best validated outcome with units
  and uncertainty, why the climb stopped, links to the artifact and evidence,
  retained changes, constraints checked, failed approaches, limitations, and next
  hypotheses.

Leave the result at the endpoint the user and project authorize. On restart,
carry forward the evidence and lessons, version any changed objective or
evaluator, and measure a comparable baseline.
