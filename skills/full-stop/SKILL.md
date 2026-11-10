---
name: full-stop
description: Run the explicitly requested Full Stop workflow, finishing and reviewing a change while leaving its PR unmerged.
disable-model-invocation: true
---

# Full Stop

Use this only for an explicit Full Stop workflow request, such as `$full-stop`.
A closing “full stop” used as emphasis is not a workflow request. The fleet
contract remains authoritative for permissions and delivery; this workflow
selects the user-requested unmerged endpoint.

Do the same work as `full-send`, but stop with the PR ready for the user to merge.
Never merge it.

Read [full-send](../full-send/SKILL.md) and follow its proof, review and
babysitting steps within the same fleet and repository boundaries. An explicit
Full Stop request activates those shared steps without a separate Full Send
request. This request
authorizes preparing this task's PR for the user to merge; it adds no authority
to bypass human-only steps, credentials, access grants or destructive-action
boundaries. The endpoint overrides below apply.

## No merging

You may commit, push, rebase, fix conflicts, and use `--force-with-lease` on
this task's branch. Never merge, enable auto-merge, enter a merge queue, push
to the default branch, bypass branch protection, or delegate those actions.

For this task's PR, disable existing auto-merge and remove it from any merge queue before
work begins; check again before each push. Report these changes. If you
cannot prevent automatic merging, report the blocker before proceeding.

## Stop at the gate

Use full-send's merge gate as the readiness check. Replace its merge and
final report steps with a handoff. Proof and review must cover the final diff;
recheck behavior changes and meaningful conflict fixes before handoff.

Fetch the target branch and check the live PR's head, base, checks, reviews,
and mergeability. Confirm it is open, not a draft, and not set to merge
without the user. If someone else merged it, report that instead.

- **Ready to merge:** the merge gate passes. Leave the PR open and unmerged.
- **Waiting for required approval:** only human approval remains. Confirm
  that this is the actual blocker.
- **Blocked:** explain what prevents readiness, what you tried, and what is
  needed. Follow full-send's rules for asking the user.

In T3 Code, call `unwatch_pull_request` before the handoff or a question.
Report the PR link, final head, verdict, proof, reviewer outcome, and remaining
risks. State whether the PR is still open and unmerged.
