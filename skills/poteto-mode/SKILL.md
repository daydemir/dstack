---
name: poteto-mode
description: Run PStack's engineering playbooks when the user explicitly requests poteto-mode or a PStack workflow in T3 Code.
---

# Poteto mode in T3 Code

The upstream package, referred to below as `<pstack>`, is the `pstack/` folder
of darma's checkout of cursor/plugins: `~/.darma/sources/pstack/pstack`, pinned
when the account takes the `pstack` source (`darma stack` clones it otherwise).
Outside darma, use the `pstack/` folder of a cursor/plugins clone. Stop and say
so if neither exists.

1. Read [the T3/Codex adapter](references/t3.md).
2. Read `<pstack>/skills/poteto-mode/SKILL.md` in full and run its matching
   playbook with that adapter applied throughout the run.

Resolve supporting skills, playbooks, agents, and references within `<pstack>`,
even when a skill with the same name is installed elsewhere. Give delegates
the absolute package and adapter paths. Read principle leaves as the upstream
mode requires. Never edit the package; local integration changes belong in this entry point
and its references.
