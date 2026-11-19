---
name: choosing-models
description: Use before choosing a model or reasoning effort for a subagent, delegate, council or review in T3 or any harness.
---

# Choosing models

Pick the cheapest model whose intelligence and taste fit the task, then the first listed effort that suffices. Scores are 0–10 judgments informed by Slopalytics. Cost reflects share of the weekly plan limit per task. T3's catalog shows where each model runs.

| Model | Intelligence | Taste | Cost (0 = cheap) | Notes |
|---|---:|---:|---:|---|
| Fable 5.2 | 10 | 9.5 | 10 | Only needed above Opus 5.5 for more taste or a strategic thinker. For work that needs taste and doesn't have a clear right answer; when we need creativity, intuition, or gut calls; to help land changes that have been spinning a while. Efforts: high, medium, low. |
| Opus 5.5 | 9 | 9 | 8 | Preferred daily driver for strategic thinking and coding. Thorough and diligent, great for work that's measurable and concrete; not the most adversarial, should be told to push back and express if it has a better idea. Efforts: high, xhigh, medium. |
| Astra 6.2 | 8.5 | 7.5 | 9 | High-level thinker and sharp code reviewer that catches bugs others miss; strong on 3D, games and motion. Stops early and turns literal on long autonomous runs, and writes worse than Astra 6, so give it bounded tasks. Bring in for a council or hard review that pits the best strategic thinkers against each other. Efforts: high, xhigh, medium. |
| Gemini 4 Neon | 8 | 6.5 | 8 | Default Gemini for multi-file coding, debugging, analysis and code review. Start at medium, use high for harder work, and reserve xhigh for cases where high falls short. |
| Sol 6.2 | 7.5 | 5.5 | 4 | Solid code writer, code reviewer and overall workhorse; faster and cheaper per task than Sol 6.1. Can hand back a plan instead of the change, so ask for the full implementation; weak at answering questions about a codebase. Efforts: xhigh, high, medium. |
| Gemini 4 Hydrogen | 6.5 | 6 | 5 | Fast Gemini for codebase reads, scoped edits and verification. Start at low for simple work and use high when the task needs more reasoning. |
| Muse Wonder Full | 5.5 | 4.5 | 7.5 | Diversifies thinking; an extra reviewer and good council member. Effort: default. |
| DeepSeek V4.1 | 5 | 2 | 0.5 | Use through OpenCode on the deploy API. It's API-billed and the one allowed exception to subscription-only, because it's very cheap for us; use it liberally as a helper. Does well on tightly briefed, bounded research and implementation; give it an exact scope and checks. Effort: high, the top the deploy model offers. |
| Terra 6.1 | 4.5 | 4 | 3 | Dumber, cheaper Sol workhorse for bounded reads and small edits. Often stops at inspection on implement-and-land tasks, so don't hand it those. Efforts: high, medium, low. |
| Haiku 5.5 | 4.5 | 5 | 2 | Grunt work that needs some taste. Efforts: low, medium, high. |
| Grok 4.7 | 4.5 | 5 | 7.5 | Rounds out thinking and diversifies opinions. Useful for challenging taste and design and injecting creativity. Efforts: high, low. |
| Luna 6 | 3.5 | 3 | 1.5 | Cheapest tasks. Efforts: max, xhigh, high, medium, low. |

Neon and Hydrogen have provisional intelligence scores informed by [Artificial Analysis](https://artificialanalysis.ai/providers/google). Their taste and subscription cost scores are Deniz's ratings. Use Carbon for a second opinion on web design or when prior runs show it suits the workload. Use Argon when prior runs favor it on that workload.
