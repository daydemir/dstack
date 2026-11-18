#!/usr/bin/env python3
"""Fresh-context critique of a rendered explainer.

Usage: critic.py <claude|codex> <stills-dir> <ask.md> <source-dir> <critique.md> [previous-critique.md]

Stages only the stills (from stills.py), the ask, the sources, critic.md,
checks.md and the previous critique, if given, in a new temporary directory,
runs the named agent CLI there read-only, and writes its reply to
<critique.md>. Fails if the CLI fails.
"""
import shutil, subprocess, sys, tempfile
from enum import Enum
from pathlib import Path

REFS = Path(__file__).resolve().parent.parent / "references"
PROMPT = "Read critic.md in this directory and follow it exactly."


class Agent(str, Enum):
    claude = "claude"
    codex = "codex"


def command(agent: Agent, frames: list[Path]) -> list[str]:
    if agent is Agent.claude:
        return ["claude", "-p", "--model", "claude-opus-5-5", "--effort", "high",
                "--allowedTools", "Read,Glob,Grep", "--", PROMPT]
    images = [arg for f in frames for arg in ("-i", str(f))]
    return ["codex", "exec", "--skip-git-repo-check", "-s", "read-only", "-m", "gpt-6.2-sol",
            "-c", "model_reasoning_effort=high", *images, "-"]


def main():
    agent = Agent(sys.argv[1])
    stills, ask, source, out = (Path(a).resolve() for a in sys.argv[2:6])
    previous = Path(sys.argv[6]).resolve() if len(sys.argv) > 6 else None
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        shutil.copytree(stills, d / "stills")
        shutil.copy(ask, d / "ask.md")
        shutil.copytree(source, d / "source")
        for name in ("critic.md", "checks.md"):
            shutil.copy(REFS / name, d / name)
        if previous:
            shutil.copy(previous, d / "previous.md")
        frames = sorted((d / "stills").glob("frame-*.png")) + sorted((d / "stills").glob("motion-*.png"))
        if not frames:
            raise SystemExit(f"no frame-*.png in {stills}")
        result = subprocess.run(command(agent, frames), cwd=d, check=True, text=True,
                                capture_output=True,
                                input=PROMPT if agent is Agent.codex else None)
    out.write_text(result.stdout)
    print(f"critique -> {out}")


if __name__ == "__main__":
    main()
