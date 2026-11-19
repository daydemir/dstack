---
name: t3-approval-cards
description: "Shell commands in T3 Full access: two shapes stop the thread on an approval card nobody answers. Codex: never rm with -f/-rf/--force, even in a trap; remove task scratch with plain rm (files) or rm -r (dirs). Claude: no zsh-only syntax like ${(k)M}, no long code in Bash heredocs; Write code that deletes nothing to a file, then run it."
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

Deletions stay visible: a literal `rm` in the command, only on scratch the task
made (temp files, build outputs, clones). Never move a deletion somewhere a
check can't see it, such as into a script, a variable or another tool.

## Codex: no forced rm

Codex asks before any literal `rm` with a force flag (`-f`, `-rf`, `-fr`,
`-r -f`, `--force`), including inside `trap`, `sudo`, `env`, `bash -c` and
`$(…)`. Full access means to run commands without asking, and plain `rm` runs
without a card.

- A file: `rm -- "$file" </dev/null`. A directory: `rm -r -- "$dir" </dev/null`.
  Without `-f`, `rm` asks before deleting a read-only file (git objects, module
  caches) when stdin is a terminal, and Codex shells can be one; `</dev/null`
  stops that prompt.
- A path that may be gone already, as in a trap:
  `trap 'if [ -e "$file" ]; then rm -- "$file" </dev/null; fi' EXIT`.
- Skip the temp file when you only pass text along and the tool reads stdin
  (`--body-file -`).

## Claude: syntax bash and zsh both read

Claude Code parses every Bash command as bash, while the shell that runs it is
the user's (zsh on the fleet Macs). When the parse fails on a command that
deletes nothing, Claude can't rule out a dangerous removal and asks. A removal
it flags in a command it can parse is rejected and the turn goes on, so that
one doesn't block.

- Keep inline commands to syntax both shells read. zsh parameter flags such as
  `${(k)M}` trip the check; bash-only forms such as `${!M[@]}` break under zsh.
- Write code, associative-array loops and long file contents with the Write
  tool, then run the file (`bash path.sh`, `python3 path.py`). A long code body
  in a heredoc (`cat > f <<'EOF'`, `python3 - <<'EOF'`) can also trip the
  check; a short plain heredoc is fine.
- Keep deletions out of those files: remove scratch with its own plain `rm`
  command. A removal Claude rejects stays rejected; leave it, or ask the user.
