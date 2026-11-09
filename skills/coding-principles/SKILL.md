---
name: coding-principles
description: When writing, changing, or reviewing code.
---

DRY, functional, lean, clean, simple. Hard cuts, not band-aids. No fallbacks unless explicitly asked. Fail fast. Compile-time type safe. CLI-driven (core logic in CLIs, UI on top, use CLI to make sure everything works end to end with tests before building any UI). No loose strings. Minimize global mutable state, side effects, nil checks, force-unwraps. Changes should simplify, not complicate. Less code, while maintaining readability, is always better. Strict type safe enums for choices. When we stumble on a potential bug, root it out instead of stepping around it.
