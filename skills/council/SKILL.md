---
name: council
description: Get independent model reviews when the user requests a council.
---

# Council

Fix known issues and outstanding PR findings, then run the relevant checks before
review. Give reviewers the updated diff and a bounded brief: the user's request word
for word (including later corrections), your reading of it, exact head and
base, checks, exclusions and open findings. Reviews are read-only. Ask
reviewers to flag where your reading differs from the request, and to report
any context they need but the brief lacks as a finding.

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

### T3 sessions

Use T3's own delegation: native subagents for this provider when no extra
settings or checkout are needed; a new `delegate_task` for another provider,
user-requested settings or a separate checkout, with options under
`target.options`. Follow its `next`: completion wakes the parent; end the turn
when instructed and do not poll. Do not switch to a CLI after a T3 auth failure.

### Standalone Codex, Claude CLI and Hermes

Use a fresh native peer when it can run the selected same-provider model.
Run the other provider with `darma t3 run`: one tool-free read on that
provider's T3 subscription account. It may run both panel members when the
native interface cannot select the requested model; the panel must still contain
two providers and two independent review contexts.

Read `darma t3 run --help`. Pick the T3 instance (`codex`, `claudeAgent`) and a
model its catalog offers; Fable only when the user explicitly chooses it. darma
is subscription-only and refuses API billing. A tool-free reviewer sees only its
prompt, so write one prompt file outside the repo holding the whole bounded brief
and the exact diff (`git diff <base>...<head>`), plus any file contents the review
needs, then:

```sh
darma t3 run --instance <codex|claudeAgent> --model <slug> --effort high \
  --prompt <brief-and-diff-file> --workdir <repo> --timeout 1800
```

It prints `{"result": PATH}`; PATH and `PATH.meta.json` (provider, model,
session) are temporary, so read them at once. Exit 1 with
`ROBIN_SUBSCRIPTION_LIMIT:<provider>:<kind>` is a usage limit; exit 2 is any
other failure. Use a fresh run for each independent review or recheck.

If `darma t3 run`, the second provider's T3 instance or its subscription login is
unavailable, say **“council blocked: second provider unavailable here”**, give
the concrete reason, and stop the council. Keep independent authorized work
moving. Leave T3, darma and logins as they are, and keep the panel to two real
providers: the author's own assessment is not a member. Report the actual
instances, models and providers used.
Other harnesses without a supported delegation route report the same gap and stop.

Give each reviewer the same scoped material and ask for findings, a score out
of 10 and an approve/request-changes verdict. Reviewers start no children and
never watch the PR. Record the model and provider the harness reports; label
unverified identity or missing scores rather than guessing.

Do not wait idle. When a result arrives, check its findings against the code
at once and decide what to fix while the other reviewers run. Do not edit
files while a reviewer still reviews the same checkout. If the user's
instructions mark a reviewer as non-blocking, do not wait for it; treat a
late result as feedback and do not record its score.

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
