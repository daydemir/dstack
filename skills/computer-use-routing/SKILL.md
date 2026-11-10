---
name: computer-use-routing
description: Use first for browser or desktop UI tasks on fleet Macs, including remote machines and human sign-in, before backend-specific skills; choose the machine, native tool or shared fallback.
---

# Computer-use routing

## 1. Where

Resolve a named machine with `darma hosts <nickname>`; otherwise use the current
machine (`darma whoami`). “Rolly's browser” means Rolly's GUI session, not a
preview tab on this computer. Use the printed SSH login; never guess it.

For an agent on another Mac, prefer its allowed T3 linked environment so its
native tools operate there. Honor read-only links and existing access scopes.
For an authorized command, use the printed SSH route. If T3 cannot launch an
agent, say so: SSH can open an app/URL in that login's GUI session, for example
`ssh rolly@rollys-mac-mini "open -a 'Google Chrome' 'https://analytics.google.com/'"`.
Opening a window does not give this agent control of the remote screen; further
interaction needs tools on that Mac or the bounded remote fallback below.

## 2. What

| Operation | Route on the resolved machine |
|---|---|
| Read public information without a requested browser interaction | Fetch/search or a purpose-built connector; no browser needed. |
| Click through a site where an isolated session is sufficient | The harness's supported browser/preview tool. |
| Use a signed-in session, prepare human login/2FA, or open a requested real browser window | A visible browser in that Mac's GUI session, preserving the requested/existing browser. A preview or isolated tab does not satisfy this. |
| Operate a native app | Native computer use for that Mac. |

Let the human enter passwords, passkeys and 2FA on that screen. Leave a requested
login window open for them. System Settings, TCC and consent grants are human-only.

## 3. Which tool

Inspect this session's actual tools (including `ToolSearch` where provided),
then read their first-use documentation. A model name or a parent's tool list
does not establish availability in this agent.

- **Codex:** `mcp__cua_repl.js` / `js_reset` expose the documented `cua` app and
  browser APIs. Use native control directly when available for the target Mac.
- **Claude:** use `ToolSearch` for enabled `computer-use` desktop or
  `claude-in-chrome` browser MCP tools, then use the returned definitions.
  A headless CLI may expose neither; do not invent a tool or enable permissions.
- **T3 browser:** `preview_status`, then existing-tab tools or `preview_open`
  when browser work is requested and an isolated preview fits. It is not a
  window on the target Mac's desktop.
- **Public reads:** Codex `web__run`, Claude `WebFetch`/`WebSearch`, or Hermes's
  available web extraction/search tools. A dedicated API/CLI wins when it
  provides the exact requested operation.

## 4. No native tool for the required GUI operation

Use the existing signed shell executor on the **target Mac**:

```sh
muavin cu --timeout-secs 90 '<bounded GUI task; use your own native computer-use tool directly; do not call muavin cu or agent-bridge>'
```

This shared fallback is an explicit exception to Muavin's personal scope; it
adds no authority or new access. It works from Claude, Hermes or reduced-tool
agents. The worker uses its own native tools; never nest the executor.
Over SSH, use the target's `~/.local/bin/muavin` with a safely quoted remote
command; do not depend on its interactive PATH.

Use `muavin cu --help`. If its default Codex path is missing, or a Node launcher
fails under launchd's PATH, pass `--codex-bin <existing native Codex executable>`
from that installed package. Do not install a workaround or change the runtime.

Verify the actual window/result with the tool's returned state or screenshot.
`muavin desktop computer-use-status` is read-only diagnostics, not proof of
granted screen/app access. Report exact denied-access, locked-console or runtime
errors; a pipe/window failure alone is not a permission diagnosis. Runtime
repairs belong to their owning CLI/runbook and the task's existing authority.
Preserve existing windows; close only your disposable tabs, keeping requested
handoff windows open.

Claude's tool discovery: [computer use](https://code.claude.com/docs/en/computer-use),
[Chrome](https://code.claude.com/docs/en/chrome). Session tool documentation governs
the actual API; no new Darma command or GUI binary is needed.
