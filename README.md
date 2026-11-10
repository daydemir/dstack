# dstack

Deniz's skills and md files for agent work.

## Shared skills

Every folder in [`skills/`](skills/) is a skill that `darma sync` (from
[darma-fleet](https://github.com/daydemir/darma-fleet)) links into `~/.agents`,
`~/.claude` and `~/.codex` on each fleet computer. Skills vendored from other
repos, and the local edits made to them, are listed in
[`skills/VENDORED.md`](skills/VENDORED.md).

## Imported collections

- [`tstack/`](tstack/): verbatim snapshot of [t3dotgg/tstack](https://github.com/t3dotgg/tstack) at commit [`1085050f3baed1ac724caa4a8166145fb2ac88af`](https://github.com/t3dotgg/tstack/commit/1085050f3baed1ac724caa4a8166145fb2ac88af), imported November 10, 2026. Includes all nine skills, supporting files, upstream README, and MIT license.
- [`pstack/`](pstack/): verbatim snapshot of [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack) at commit [`de8ee15dd1194627d21eb5fcd41cb1873208dabb`](https://github.com/cursor/plugins/commit/de8ee15dd1194627d21eb5fcd41cb1873208dabb), imported November 10, 2026. Includes all 58 skills and the complete upstream package, including agents, playbooks, docs, assets, automations, and MIT license. Importing the automation files does not enable them.

## PStack in T3 Code

[`skills/poteto-mode/`](skills/poteto-mode/) is a separate entry point with a
[T3/Codex adapter](skills/poteto-mode/references/t3.md). The upstream `pstack/`
snapshot stays unchanged. The entry point reads supporting skills from that
snapshot, so existing installed versions of `how`, `tdd`, and other skills are
left in place.

To install the entry point for Codex, link this checkout's `skills/poteto-mode`
folder into `~/.agents/skills/poteto-mode`. Keep the checkout available at that
location. Invoke `$poteto-mode` with your task; it is explicit-only. Model-role
configuration is optional and is created only when you ask for `setup-pstack`.
