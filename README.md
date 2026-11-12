# dstack

Deniz's generic agent opinions: the user-level `AGENTS.md` and the skills that
apply in every project.

- [`user/AGENTS.md`](user/AGENTS.md): user-level instructions, loaded in every
  session: coding principles, boundaries, storage and fleet pointers.
- [`skills/`](skills/): one folder per generic, on-demand skill. Skills vendored
  from other repos, and the local edits made to them, are listed in
  [`skills/VENDORED.md`](skills/VENDORED.md).

Project and repo instructions do not live here: each project's home repo owns
its `AGENTS.md` and `.agents/skills/`, and each repo owns its own.

## Installing

[darma](https://github.com/daydemir/darma-fleet) delivers dstack to fleet
accounts, and only what each account opts into:

```sh
darma stack                      # show the choices and what is chosen
darma stack agents-md on|off     # link user/AGENTS.md into each Claude/Codex home
darma stack skills all|none|NAME...
darma sync
```

Darma links the chosen skills into `~/.agents`, `~/.claude`, `~/.codex`,
custom Claude/Codex homes (including T3's) and Hermes' `skills/dstack`
category. Outside the fleet, symlink the same folders by hand.

## Imported collections

- [`tstack/`](tstack/): verbatim snapshot of [t3dotgg/tstack](https://github.com/t3dotgg/tstack) at commit [`11e37a74d0a6868c121cd0910ab2b3bd9873b92a`](https://github.com/t3dotgg/tstack/commit/11e37a74d0a6868c121cd0910ab2b3bd9873b92a), imported November 10, 2026; refreshed November 11, 2026. Includes all nine skills, supporting files, upstream README, and MIT license.
- [`pstack/`](pstack/): verbatim snapshot of [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack) at commit [`de8ee15dd1194627d21eb5fcd41cb1873208dabb`](https://github.com/cursor/plugins/commit/de8ee15dd1194627d21eb5fcd41cb1873208dabb), imported November 10, 2026. Includes all 58 skills and the complete upstream package, including agents, playbooks, docs, assets, automations, and MIT license. Importing the automation files does not enable them.

## TStack workflows

All nine selected tstack workflows are installed from the fleet adaptations in
`skills/`: `babysit-pr`, `council`, `file-pr`, `full-send`, `full-stop`,
`leaving-pr-comments`, `modernize`, `sol-loop` and `takeover`. Darma delivers them
to opted-in coding profiles and the Hermes `dstack` category. The `tstack/`
snapshot remains verbatim; provenance and deliberate adaptations are recorded
in `skills/VENDORED.md`.

Fleet authority and the requested delivery endpoint govern the workflows.
`full-stop` is explicit-only (`$full-stop`), never ordinary emphasis. Council
selects enabled providers, reports its actual panel, and reserves Astra for an
explicitly chosen wargamer, grandmaster or final reviewer.

## PStack in T3 Code

[`skills/poteto-mode/`](skills/poteto-mode/) is a separate entry point with a
[T3/Codex adapter](skills/poteto-mode/references/t3.md). The upstream `pstack/`
snapshot stays unchanged. The entry point reads supporting skills from that
snapshot, so existing installed versions of `how`, `tdd`, and other skills are
left in place. The other 58 pstack skills remain package references reached
by this mode; they are not separately installed in the global catalog.

With its skills chosen, `darma sync` installs the entry point alongside the other
shared skills. Invoke `$poteto-mode` with your task; it is explicit-only. Model-role
configuration is optional and is created only when you ask for `setup-pstack`.
