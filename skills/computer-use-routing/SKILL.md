---
name: computer-use-routing
description: Use first for browser or desktop UI tasks on fleet Macs, including remote machines and signing in, before backend-specific skills; choose the machine, native tool or shared fallback.
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
| Use a signed-in session, sign in, or open a requested real browser window | A visible browser in that Mac's GUI session, preserving the requested/existing browser. A preview or isolated tab does not satisfy this. |
| Operate a native app | Native computer use for that Mac. |

## 3. Run unattended

Finish without a person at the screen:

- **Sign in yourself** from 1Password (service-account token per darma-fleet's
  README; match items by URL or title), one-time code included. Move each secret
  through the clipboard so it never reaches your context or logs: `op item get ID
  --vault VAULT --fields password --reveal | pbcopy` (or `--otp`), paste it into
  the field, then `pbcopy < /dev/null`. Never print a secret or type it out.
  A login the service account can't see is Deniz's to add to its vaults.
- **Restart what you automate** (the browser or app) when it stops responding;
  session restore keeps its windows.
- **Raise no dialogs.** A command that can prompt for a password or consent on
  the screen (for example `security` on a locked keychain without `-p`) blocks
  every agent behind it; pass the stored secret non-interactively or skip it.
- **A pause names its own test.** Record what clears it; the next run re-tests
  that and resumes on its own instead of waiting for a person.
- **Retry by state, not blindly.** Before rerunning screen work, check what the
  last run already did and do only what's unfinished, so a purchase or submit
  never happens twice.
- **When something needs Deniz** (what no agent can do, such as a macOS
  permission grant, a passkey or device the fleet doesn't hold, or a check you
  couldn't pass after trying; or what his boundaries reserve to him), message
  him at once with `darma msg`, saying exactly what to do and where, rather than
  leaving it for a check-in.

## 4. Which tool

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

## 5. No native tool for the required GUI operation

Use darma's bounded fallback on the **target Mac**:

```sh
darma cu --timeout-secs 90 '<bounded GUI task>'
```

It runs Codex's computer-use plugin in that Mac's logged-in GUI session and works
from Claude, Hermes, SSH or reduced-tool agents. Tasks run one at a time per
Mac, and darma appends a standing brief carrying section 3 to the worker, so
don't repeat it. The queue covers `darma cu` callers only; on a screen other
agents drive through `darma cu`, use it too rather than your native tool. Over SSH, use the
target's `~/.local/bin/darma cu` with a safely quoted remote command; do not
depend on its interactive PATH. `muavin cu` is retired; do not use it.

Use `darma cu --help`; if `cu` is an unknown command, that Mac's darma predates
it, so run `darma update` there. If the default `~/.local/bin/codex` is missing
or is a Node launcher that fails under launchd's PATH, pass `--codex-bin
<existing native Codex executable>` from that installed package. Do not install
a workaround or change the runtime. A run's logs are in the
`$TMPDIR/darma-cu-<id>` it prints.

Branch on its exit code: 0 done; 2 failed; 3 runtime fault (the helper's
AppleEvent `-1712`, or a busy screen), so retry once later by state as in
section 3; 4 needs a human, with the reason after `cu: needs a human:` on stderr, so message Deniz as
in section 3. A pipe, window or AppleEvent failure alone is not a permission
diagnosis. Verify the actual window/result from the worker's report. Preserve
existing windows; close only your disposable tabs.

Claude's tool discovery: [computer use](https://code.claude.com/docs/en/computer-use),
[Chrome](https://code.claude.com/docs/en/chrome). Session tool documentation governs
the actual API.
