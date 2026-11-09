---
name: ask-through-questions
description: When your reply would end with action items, open decisions, or recommendations for the user to approve, or the user asks to go through items one at a time.
---

Turn the list into a sequence of questions the user answers with the question tool (`AskUserQuestion` in Claude Code, `request_user_input` in Codex), instead of a report that ends in a list or a question buried in prose.

1. **Collect.** Find every item that needs the user: decisions, approvals, items to triage. Drop anything you can settle yourself from the code, the docs, or a sensible default, and just do it. Order the rest by what matters most or what unblocks other items.
2. **One item per question.** Ask about one item at a time, numbered ("3 of 7 — ABC-123: Update the landing page"). Batch only small items that don't depend on each other, up to four in one call.
3. **Make each question stand alone.** The user may see only the dialog, so cover in a few short lines: what the item is, why it matters or why it ranks where it does, and what you recommend. Use names and facts, not "the thing above."
4. **Options.** Give 2–4 concrete actions, recommended one first and marked "(Recommended)". Each option says what you'll do if it's picked. Include a real alternative like defer, retire, or hand off, not filler. The user can always write their own answer.
5. **Act, then continue.** After each answer, do what was chosen (or start it), say in one line what happened, then ask the next question. If an answer is free text that changes the plan, do that first and come back to the queue.
6. **Finish.** Once every item is answered, give a short summary: what was decided, what you did, and what's still running or blocked.

Never ask "should I proceed?" or ask to approve a plan as a question. Ask the decision inside it.
