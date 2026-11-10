# dstack

Deniz's skills and md files for agent work.

## Shared skills

Every folder in [`skills/`](skills/) is a skill that `darma sync` (from
[darma-fleet](https://github.com/daydemir/darma-fleet)) links into `~/.agents`,
`~/.claude` and `~/.codex`, including discovered custom coding homes, on each
fleet computer. Hermes receives one `skills/dstack` category link; its own
profile, soul and stock skills stay in place. Skills vendored from other
repos, and the local edits made to them, are listed in
[`skills/VENDORED.md`](skills/VENDORED.md).

[`fleet/AGENTS.md`](fleet/AGENTS.md) holds the fleet-wide agent rules. `darma sync`
links it as `AGENTS.md` into each Claude and Codex home, including custom
homes set in T3 Code. New accounts start with dstack off. Choose
`darma dstack on` followed by `darma sync` to install skills and rules;
`darma dstack off` removes their managed links together.

dstack owns generic skills and fleet rules shared across LLCs. Darma owns the
people/project/machine directory, shared commands (including Linear and Slack),
shared Hermes config, skill linking and shell setup. It runs no daemon; a future
shared machine job can be a plain launchd unit from darma-fleet. Each is its own
project.

Muavin is Deniz's life-management project, including Mooney's soul, personal
skills, protected Apple data and device signing/keychain. It remains installed
on every Mac for now. Each project's home repo is also its T3 project and Darma
target; that home owns AGENTS.md, project skills, the project agent's soul/persona,
child-repo verification and project jobs. Per-machine identity facts stay in
Darma's host entry. Rolly is the MIX AI-employee role, potentially several agents;
its mini is the Suelio MIX build/knowledge computer.

MIX gate Xcode admission/storage belongs to mix-mono. Worktrees use T3/plain Git,
with no fleet ownership service; `fleet/AGENTS.md` governs retirement. Each later
ownership move is a small PR with a check that the affected agent still starts.

Darma points to one repository per project; for MIX, `suelio-arts/mix` owns and
checks its child repositories. Sync runs on demand, without a scheduled job.
MIX coordination notes belong in that workspace's tracked `handoffs/` directory.
Placement of generated MIX CLI skills is awaiting their usefulness audit; none
are linked by Darma yet.

## Imported collections

- [`tstack/`](tstack/): verbatim snapshot of [t3dotgg/tstack](https://github.com/t3dotgg/tstack) at commit [`1085050f3baed1ac724caa4a8166145fb2ac88af`](https://github.com/t3dotgg/tstack/commit/1085050f3baed1ac724caa4a8166145fb2ac88af), imported November 10, 2026. Includes all nine skills, supporting files, upstream README, and MIT license.
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

With dstack enabled, `darma sync` installs the entry point alongside the other
shared skills. Invoke `$poteto-mode` with your task; it is explicit-only. Model-role
configuration is optional and is created only when you ask for `setup-pstack`.
