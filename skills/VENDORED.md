# Vendored skills

These skills moved here from Muavin's `setup/skills` on November 10, 2026
(muavin@84d9131). `darma sync` links every folder in `skills/` onto each fleet
computer, so this table replaces Muavin's `skills-manifest.toml`.

Changes made in the move:

- `unslop` sets `disable-model-invocation: true` in its own frontmatter. Muavin
  used to enforce that through Claude settings sync.
- `ponytail-help` says fleet copies come from dstack through `darma sync`.
- The `ponytail-*` sub-skills went only to mua and rolly before. They're
  explicit-only, so every computer now gets them.

Local edits in the notes column are deliberate: diff against upstream before
refreshing a skill from its source.

| Skill | Origin | Upstream | Vendored | Notes |
|---|---|---|---|---|
| `wayfinder` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/engineering/wayfinder) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 | local edit: explicit-only optional planning workflow; preserve invocation policy on upstream refresh |
| `prototype` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/engineering/prototype) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `diagnosing-bugs` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/engineering/diagnosing-bugs) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `resolving-merge-conflicts` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/engineering/resolving-merge-conflicts) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `wizard` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/engineering/wizard) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `research` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/engineering/research) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `tdd` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/engineering/tdd) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `grilling` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/productivity/grilling) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `grill-me` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/productivity/grill-me) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `handoff` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/productivity/handoff) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `writing-for-agents` | claude-plugins-official mattpocock-skills v1.2.3 plugin cache (skills/productivity/writing-for-agents) | [mattpocock/skills](https://github.com/mattpocock/skills/tree/0ab1b63a410a03d3627979a109c8695de27af954) | 2026-08-20 |  |
| `principle-prove-it-works` | github.com/michael-denyer/pstack-claude plugins/pstack/skills/principle-prove-it-works | [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude/tree/8bf501c1a9f6777f63f8d9a705c2b3f54a5b2eac) | 2026-08-20 |  |
| `blast-radius` | github.com/michael-denyer/pstack-claude plugins/pstack/skills/blast-radius | [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude/tree/8bf501c1a9f6777f63f8d9a705c2b3f54a5b2eac) | 2026-08-20 |  |
| `how` | github.com/michael-denyer/pstack-claude plugins/pstack/skills/how | [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude/tree/8bf501c1a9f6777f63f8d9a705c2b3f54a5b2eac) | 2026-08-20 |  |
| `unslop` | Mooney's local ~/.claude/skills/unslop (canonical — Deniz-tuned fork of pstack-claude's unslop) | [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude/tree/8bf501c1a9f6777f63f8d9a705c2b3f54a5b2eac) | 2026-08-20 | local edit: explicit-only writing skill; upstream watch is advisory only — never overwrite the tuned copy from upstream |
| `ponytail` | ponytail plugin cache v4.8.4 on Rolly (skills/ponytail + hooks/) |  | 2026-08-20 | Explicit-only base skill on every host so legacy unmanaged copies cannot retain automatic activation |
| `ponytail-audit` | ponytail plugin cache v4.8.4 on Rolly (skills/ponytail-audit) |  | 2026-08-20 |  |
| `ponytail-debt` | ponytail plugin cache v4.8.4 on Rolly (skills/ponytail-debt) |  | 2026-08-20 |  |
| `ponytail-gain` | ponytail plugin cache v4.8.4 on Rolly (skills/ponytail-gain) |  | 2026-08-20 |  |
| `ponytail-help` | ponytail plugin cache v4.8.4 on Rolly (skills/ponytail-help) |  | 2026-08-20 |  |
| `ponytail-review` | ponytail plugin cache v4.8.4 on Rolly (skills/ponytail-review) |  | 2026-08-20 |  |
| `diligence` | fleet-local |  | 2026-09-16 | Automatically selected for systematic and infrastructure improvements; bounded by evidenced benefit and existing authority |
| `human-readable` | fleet-local (already versioned in setup/skills before this manifest existed) |  | 2026-08-11 | local edit: explicit-only document style workflow; preserve invocation policy on upstream refresh |
| `html-plan` | Mooney's local ~/.agents/skills/html-plan |  | 2026-08-20 | local edit: description now fires standalone on plan-for-Deniz requests (the old wording referenced a nonexistent 'html' router) |
| `impeccable` | Mooney's local ~/.claude/skills/impeccable reconciled with ~/.agents/skills/impeccable |  | 2026-08-20 | canonical = the .claude copy (richer frontmatter, /command spelling) plus the agents/ dir that only the .agents copy had; internal path references self-correct via the skill's own <skill-base-dir> instruction |
