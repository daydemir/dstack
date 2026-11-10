---
name: council
description: Get independent model reviews when the user requests a council.
---

# Council

Fix known issues and outstanding PR findings, then run the relevant checks before
review. Give reviewers the updated diff and a bounded brief: intent, exact head
and base, checks, exclusions and open findings. Reviews are read-only.

## Select the panel

Use providers enabled in the current machine and harness, with models offered by
its live catalog. In T3 Code, use `orchestrator_capabilities` once per thread;
refresh it only after an error or an explicit provider change. Require
`canRunChildTask: true`; a configured or disabled provider is not an available
reviewer. Known authentication or usage failures remain blockers even when the
catalog advertises the model.

Honor the user's named panel. Otherwise use two independent model providers,
preferably an enabled GPT Sol and an enabled Claude model, at high effort. Two
accounts or harnesses for the same model provider are not two independent
providers. If the user requests more reviewers, choose only from the enabled
catalog. Report the chosen public model names and provider instances.

GPT-6 Astra is reserved for a user who explicitly chooses it as wargamer,
grandmaster or final reviewer. Ordinary council and “latest/strongest model”
selection use the enabled Sol/Claude panel; they do not select Astra.

If a requested member or a second provider is unavailable, report the missing
capability or exact auth/access failure. Do not silently substitute a model,
copy credentials or label one provider's reviews a completed council.

## Run and resolve

Use the current harness's supported delegation route. Use native subagents for
models on this provider when no extra settings or checkout are needed. In T3,
use a new `delegate_task` for another provider, user-requested settings or a
separate checkout, with model options under `target.options`. Every recheck uses
a fresh reviewer. Follow a delegate's `next`: completion wakes the parent; end
the turn when instructed and do not poll. Outside T3, if the available native
interface cannot reach both providers, report the gap.

Give each reviewer the same scoped material and ask for findings, a score out
of 10 and an approve/request-changes verdict. Reviewers start no children and
never watch the PR. Record the model and provider the harness reports; label
unverified identity or missing scores rather than guessing.

Check findings against the actual code. Apply material fixes yourself, prove
them, and request a fresh review of the changed head. Keep later rounds focused
on changed behavior and unresolved findings. Decline unsupported scope expansion
with evidence. Stop when the panel approves the reviewed head; budget exhaustion,
missing replies and auth errors are not approval. The fleet contract and the
user's scope still govern delivery and permissions.

## Record the result

Put the result in the PR description before its model/harness attribution, or
in the final answer when there is no PR. Include round count, exact reviewed head,
public model names, provider instances, scores and remaining findings. Use one
column per round; write `no score` when none was supplied. Never post a duplicate
review-summary comment. Use `babysit-pr` for the delivery endpoint the user asked
for, and verify the current head and checks again before merging.
