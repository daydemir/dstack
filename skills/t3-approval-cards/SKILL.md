---
name: t3-approval-cards
description: "Shell commands in T3 Full access: two shapes stop the thread on an approval card nobody answers. Codex: no rm with -f/-rf/--force, even in a trap; use rm -r -- TARGET </dev/null. Claude: no zsh-only syntax like ${(k)M} and no code in Bash heredocs; write the file with Write, then run it."
---

# T3 approval cards

T3 Code 0.1.10 still shows an approval card in Full access for two command
shapes, and an unattended thread then waits for hours until someone answers.
Until T3 ships its fixes, write commands in shapes neither check flags. Codex:
[issue #37298](https://github.com/pingdotgg/t3code/issues/37298), fix
[#39044](https://github.com/pingdotgg/t3code/pull/39044). Claude:
[issue #38572](https://github.com/pingdotgg/t3code/issues/38572), fix
[#38581](https://github.com/pingdotgg/t3code/pull/38581). Delete this skill
once both fixes ship in the T3 release the fleet runs.

Full access is meant to run these commands without asking, so these shapes don't
dodge a review. They cover disposable state the task made: scratch and temp
files, build outputs, clones. Deleting anything else still follows the fleet
boundaries. Never disguise a deletion to get it past a check.

## Codex: no forced rm

Codex asks before any literal `rm` with a force flag (`-f`, `-rf`, `-fr`,
`-r -f`, `--force`), including inside `trap`, `sudo`, `env`, `bash -c` and
`$(…)`. Plain `rm` and `rm -r` run without a card.

- Remove with `rm -r -- "$target" </dev/null`. Without `-f`, `rm` asks before
  deleting a read-only file (git objects, module caches) when stdin is a
  terminal, and Codex shells can be one; `</dev/null` stops that prompt.
- For a path that may be gone already: `[ ! -e "$target" ] || rm -r -- "$target" </dev/null`.
- In a trap: `trap 'rm -- "$body" </dev/null' EXIT`.
- Skip the temp file when you only pass text along: send it on stdin, as in
  `gh pr create --body-file - <<'EOF'`.

## Claude: syntax bash and zsh both read

Claude Code parses every Bash command as bash, while the shell that runs it is
the user's (zsh on the fleet Macs). When the parse fails, Claude can't rule out
a dangerous removal and asks, even for a command that deletes nothing.

- Keep inline commands to syntax both shells read. zsh parameter flags such as
  `${(k)M}` trip the check; bash-only forms such as `${!M[@]}` break under zsh.
- Write code, associative-array loops and long file contents with the Write
  tool, then run the file (`bash path.sh`, `python3 path.py`). A large code
  body in a heredoc (`cat > f <<'EOF'`, `python3 - <<'EOF'`) also trips the
  check; a short plain heredoc is fine.
- If a command that deletes nothing still gets the card, send it again in
  plain syntax; Claude's own message allows that. A refused command that
  deletes something stays refused: drop that part, or ask the user.
