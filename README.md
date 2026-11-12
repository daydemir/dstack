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
accounts, and only what each account opts into, pinned to a dstack commit per
account:

```sh
darma stack                      # show the choices, pins and what is chosen
darma stack choose               # interactive
darma stack agents-md on|off     # link user/AGENTS.md into each Claude/Codex home
darma stack skills dstack all|none|NAME...
darma stack check                # what is new upstream; `darma stack update` takes it
darma sync
```

Darma links the chosen skills into `~/.agents`, `~/.claude`, `~/.codex`,
custom Claude/Codex homes (including T3's) and Hermes' `skills/dstack`
category. Outside the fleet, symlink the same folders by hand.

## Upstream collections

dstack no longer vendors other skill collections. Darma offers
[mattpocock/skills](https://github.com/mattpocock/skills),
[t3dotgg/tstack](https://github.com/t3dotgg/tstack) and
[cursor/plugins `pstack/`](https://github.com/cursor/plugins/tree/main/pstack)
as their own sources, each chosen and pinned per account and linked as
`mattpocock-NAME`, `tstack-NAME` and `pstack-NAME` beside the adapted copies
here (`darma stack`). Their MIT notices, which also cover the adapted copies in
`skills/`, are kept in [`licenses/`](licenses/).

## TStack workflows

All nine selected tstack workflows are installed from the fleet adaptations in
`skills/`: `babysit-pr`, `council`, `file-pr`, `full-send`, `full-stop`,
`leaving-pr-comments`, `modernize`, `sol-loop` and `takeover`. Darma delivers them
to opted-in coding profiles and the Hermes `dstack` category. Provenance and
deliberate adaptations are recorded in `skills/VENDORED.md`.

Fleet authority and the requested delivery endpoint govern the workflows.
`full-stop` is explicit-only (`$full-stop`), never ordinary emphasis. Council
selects enabled providers, reports its actual panel, and reserves Astra for an
explicitly chosen wargamer, grandmaster or final reviewer.

## PStack in T3 Code

[`skills/poteto-mode/`](skills/poteto-mode/) is a separate entry point with a
[T3/Codex adapter](skills/poteto-mode/references/t3.md). It reads the upstream
package from darma's pinned checkout of the `pstack` source
(`~/.darma/sources/pstack/pstack`), so existing installed versions of `how`,
`tdd`, and other skills are left in place. The pstack leaves are reached by
this mode; an account links them globally only by taking the `pstack` source.

With its skills chosen, `darma sync` installs the entry point alongside the other
shared skills. Invoke `$poteto-mode` with your task; it is explicit-only. Model-role
configuration is optional and is created only when you ask for `setup-pstack`.
