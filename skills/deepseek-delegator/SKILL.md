---
name: deepseek-delegator
description: Hand simple code work to DeepSeek through T3 while Opus plans, orchestrates and reviews, saving Claude Code tokens. Use when the user asks for the DeepSeek delegator or to delegate the work to DeepSeek.
---

# DeepSeek delegator

Opus plans, orchestrates and reviews; DeepSeek does the simple code work, so Claude tokens go to thinking. Work too hard for DeepSeek goes to Neon (when T3 can run it), per `choosing-models`. You never edit files yourself: your own tools are `delegate_task`, reading files, `git diff` / `git status`, and running the repo's tests. Skip `orchestrator_capabilities`: the target is known.

DeepSeek target: `{providerInstanceId: "opencode", model: "deploy/deepseek-ai/deepseek-v4.1-flash-1017", options: {variant: "high"}}`, `mode: "wait"`, `timeoutMs: 3600000`. Each call starts with no memory, so every brief carries the repo path, everything it needs, and the rule to read and write only inside that repo.

1. Research: one call with the task verbatim. It reads the code and replies in at most 80 lines: relevant files and symbols, how the current code works, how to run the tests, constraints, open questions. No edits.
2. Plan: decide the design yourself: what changes where, interfaces, edge cases, tests. Short and concrete.
3. Implement: one call with the task verbatim, your plan and the research map. It implements, runs the tests, and replies in at most 15 lines: files changed, test result, deviations from the plan.
4. Review: read the whole diff and the code around it you need to judge it, and run the tests yourself. Check that every requirement in the task is met and that no existing behaviour or public API broke. Send at most two correction calls with exact fixes, rerunning the tests after each.
5. End with a short summary.
