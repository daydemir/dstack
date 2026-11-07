---
name: voice-memo
description: when user wants you to communicate with them by voice memo or audio
---

Turn the message you would have written into a voice memo that makes sense by ear alone.

1. **Content.** Work out the message first, meaning what you would say in text and its arc from opening to conclusion. Use only facts you have, and say out loud what you couldn't verify.
2. **Script.** Keep the same overall arc and conclusions, but reorganize the ideas for someone who can't see a screen or scroll back. Lead with the point, then say how many parts are coming and signpost each one ("first", "the second thing", "so the upshot is"). Name each idea before giving its details. Turn lists, tables, code, and links into spoken descriptions, and end with a one-sentence recap if the memo runs longer than a minute. Join related ideas with conjunctions (and, but, so, because, which) instead of stacking fragments or using dashes, colons, and parentheses, since the voice handles connected clauses more naturally than choppy sentences. Spell out numbers, symbols, abbreviations, and names the way they should be said. Leave out anything that only works on a screen, like paths, hashes, and commands, and put those in the text reply instead. Keep it as short as the content allows.
3. **Voice.** Run `scripts/memo.py` (Kokoro `af_heart` at 1.2x, downloaded if missing). It voices one sentence at a time and writes `memo.m4a`. Read [the helper usage](references/helpers.md) for setup and commands.
4. **Check.** You can't hear audio, so `memo.py` transcribes the result and compares it with the script. Rewrite or respell any flagged sentences and run it again.
5. **Deliver.** Give the memo's absolute path, embedded if your client plays audio inline, plus one line saying what it covers and anything screen-only that it left out.
