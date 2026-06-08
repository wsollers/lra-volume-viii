#!/usr/bin/env python3
"""Delegate leaf governance tool calls to the canonical lra-governance repo."""

from __future__ import annotations

import os
import runpy
import sys
from pathlib import Path


def _governance_root() -> Path | None:
    candidates: list[Path] = []
    env_root = os.environ.get("LRA_GOVERNANCE_ROOT")
    if env_root:
        candidates.append(Path(env_root))

    here = Path(__file__).resolve()
    candidates.extend(parent / "lra-governance" for parent in here.parents)

    for candidate in candidates:
        if (candidate / "tools" / "governance").is_dir():
            return candidate
    return None


def main(tool_name: str) -> int:
    root = _governance_root()
    if root is None:
        print(
            "ERROR: lra-governance is not present. Governance tools are canonical "
            "there; clone it next to this leaf repo or set LRA_GOVERNANCE_ROOT.",
            file=sys.stderr,
        )
        return 2

    tool = root / "tools" / "governance" / tool_name
    if not tool.is_file():
        print(
            f"ERROR: lra-governance does not provide required governance tool: {tool}",
            file=sys.stderr,
        )
        return 2

    sys.argv[0] = str(tool)
    sys.path.insert(0, str(tool.parent))
    runpy.run_path(str(tool), run_name="__main__")
    return 0
