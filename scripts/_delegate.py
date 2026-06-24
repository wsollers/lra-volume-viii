#!/usr/bin/env python3
"""Delegate leaf script invocations to the canonical lra-governance checkout."""

from __future__ import annotations

import os
import runpy
import sys
from pathlib import Path


def governance_root() -> Path:
    candidates: list[Path] = []
    env = os.environ.get("LRA_GOVERNANCE_ROOT")
    if env:
        candidates.append(Path(env))
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidates.append(parent.parent / "lra-governance")
    candidates.append(Path("F:/repos/lra-governance"))

    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        if (resolved / "scripts").is_dir() and (resolved / ".git").exists():
            return resolved
    raise SystemExit(
        "lra-governance is not present. Set LRA_GOVERNANCE_ROOT, place it at "
        "../lra-governance, or clone it to F:/repos/lra-governance."
    )


def delegate(wrapper_file: str) -> None:
    wrapper = Path(wrapper_file).resolve()
    scripts_root = wrapper.parent
    rel = wrapper.relative_to(scripts_root)
    target = governance_root() / "scripts" / rel
    if not target.exists():
        raise SystemExit(f"canonical governance script not found: {target}")
    sys.argv[0] = str(target)
    sys.path.insert(0, str(target.parent))
    runpy.run_path(str(target), run_name="__main__")