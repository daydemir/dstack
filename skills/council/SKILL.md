---
name: council
description: Get independent model reviews and ideas when the user requests a council.
---

# Council

A council is either a code review or feedback on a plan, design or idea.

Before a code review, fix known issues and outstanding PR findings, then run the
relevant checks. When the user wants to discard the implementation and explore
new ideas, skip fixes to code being replaced.

Every reviewer gets the same material (the updated diff, or the plan or idea
under discussion) and the same blind, bounded brief:

- The user's request word for word, including later corrections, except any
  council score target or approval bar: "until every reviewer scores 9.5"
  becomes "until [score target withheld]". Product, performance and safety
  targets stay in.
- Your reading of the request, checks, exclusions and open findings, plus the
  exact head and base for a code review.
- On a recheck, what changed and how each earlier finding was handled, stated as
  facts.

Blind means the brief holds no score, verdict or attribution from any reviewer
or round, the reviewer's own included, and asks for no particular score. Point
reviewers at the artifact and evidence, not at prior review threads or score
records. Reviews are read-only; reviewers start no children and never watch the
PR.

Reviewers think freely. Invite each to challenge the premise, the approach and
your reading, to propose deleting or replacing what you built, and to report
context the brief lacks as a finding. The user's scope and permissions still
govern what you implement. Ask for findings marked material or preference. For
a code review, also ask for a score out of 10 and an approve/request-changes
verdict against the same task criteria each round. For feedback, ask each to
make the case for what it recommends.

## Select the panel

Use providers enabled in the current machine and harness, with models offered by
its live catalog. In T3 Code, use `orchestrator_capabilities` once per thread;
refresh it only after an error or an explicit provider change. Require
`canRunChildTask: true`; a configured or disabled provider is not an available
reviewer. Known authentication or usage failures remain blockers even when the
catalog advertises the model.

Read `choosing-models` before selecting the panel. Honor the user's named panel;
otherwise select from its model group to fit what this work needs judged, using
its cost and effort guidance. The panel needs at least two independent model
providers; two accounts or harnesses for one provider are not two providers.
Choose only models offered by the enabled catalog, and report the chosen public
model names, efforts and provider instances.

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

Read `darma t3 run --help`. Pick an account of that provider that `darma accounts`
shows signed in (such as `codex-personal` or `claude-suelio`) and the selected
model's slug from its catalog. darma is subscription-only and refuses API billing.
A tool-free reviewer sees only its prompt, so write one prompt file outside the
repo holding the whole bounded brief and the exact diff (`git diff
<base>...<head>`), plus any file contents the review needs, then:

```sh
darma t3 run --instance <account> --model <slug> --effort <effort> \
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
providers: the author's own assessment is not a member.
Other harnesses without a supported delegation route report the same gap and stop.

Record the model and provider the harness reports; label unverified identity
or missing scores rather than guessing.

Do not wait idle. When a result arrives, check its findings against the code
at once and decide what to fix while the other reviewers run. Do not edit
files while a reviewer still reviews the same checkout. If the user's
instructions mark a reviewer as non-blocking, do not wait for it; treat a
late result as feedback and do not record its score.

Check findings against the actual code. Apply material fixes yourself, prove
them, and request a fresh, blind review of the changed head. Keep later rounds
focused on changed behavior and unresolved findings. Settle each preference on
its merits; reopen it for new evidence, not a later reviewer's opposite taste.
Decline unsupported scope expansion with evidence. Stop when all required
reviewers approve the reviewed head and each score meets any target the user
set; budget exhaustion, missing replies and auth errors are not approval. The
fleet contract and the user's scope still govern delivery and permissions.

## Record the result

For feedback, summarize the useful findings, disagreements and recommended next
steps in the final answer, naming each member's model.

When a code-review council ends, put the result in the PR description before
its model/harness attribution, or in the final answer when there is no PR.
Include round count, exact reviewed head, public model names, provider
instances, scores and remaining findings. Use one column per round; write `no
score` when none was supplied. Never post a duplicate review-summary comment.
Use `babysit-pr` for the delivery endpoint the user asked for, and verify the
current head and checks again before merging.
