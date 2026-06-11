#!/usr/bin/env python3
"""Leaf volume build wrapper."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path, env: dict[str, str] | None = None) -> None:
    print("+ " + " ".join(cmd))
    try:
        subprocess.run(cmd, cwd=cwd, check=True, env=env)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.returncode) from None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and build a leaf LRA volume.")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--refactor-mode", action="store_true")
    parser.add_argument("--print-edition", action="store_true",
                        help="omit proof vaults, exercise vaults, and capstones from the rendered PDF")
    parser.add_argument("--latex-command", nargs=argparse.REMAINDER, default=None)
    args = parser.parse_args()

    root = args.root.resolve()
    validator = root / "scripts" / "validate_leaf_proofs.py"
    cmd = [sys.executable, str(validator), "--root", str(root), "--strict"]
    if args.refactor_mode:
        cmd.append("--refactor-mode")
    run(cmd, root)

    latex_cmd = args.latex_command or ["latexmk", "-lualatex", "main.tex"]
    if not args.validate_only:
        if shutil.which(latex_cmd[0]) is None:
            raise SystemExit(f"Build command not found: {latex_cmd[0]}. Validation already passed; install latexmk or use --validate-only.")
        env = os.environ.copy()
        if args.print_edition:
            env["LRA_PRINT_EDITION"] = "1"
        run(latex_cmd, root, env=env)

    route_generator = root / "scripts" / "generate_theorem_routes.py"
    if route_generator.exists():
        run([sys.executable, str(route_generator), "--root", str(root)], root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
