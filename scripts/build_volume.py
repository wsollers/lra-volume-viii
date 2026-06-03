#!/usr/bin/env python3
"""Leaf volume build wrapper."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    print("+ " + " ".join(cmd))
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.returncode) from None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and build a leaf LRA volume.")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--refactor-mode", action="store_true")
    parser.add_argument("--latex-command", nargs=argparse.REMAINDER, default=None)
    args = parser.parse_args()

    root = args.root.resolve()
    validator = root / "scripts" / "validate_leaf_proofs.py"
    cmd = [sys.executable, str(validator), "--root", str(root), "--strict"]
    if args.refactor_mode:
        cmd.append("--refactor-mode")
    run(cmd, root)

    if args.validate_only:
        return 0

    latex_cmd = args.latex_command or ["latexmk", "-lualatex", "main.tex"]
    if shutil.which(latex_cmd[0]) is None:
        raise SystemExit(f"Build command not found: {latex_cmd[0]}. Validation already passed; install latexmk or use --validate-only.")
    run(latex_cmd, root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
