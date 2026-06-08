#!/usr/bin/env python3
"""Compatibility wrapper for the canonical governance note-block validator."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


tool = Path(__file__).resolve().parents[1] / "tools" / "governance" / "validate_note_blocks.py"
if not tool.is_file():
    print(
        "ERROR: local governance wrapper is missing; expected tools/governance/"
        "validate_note_blocks.py in this leaf repo.",
        file=sys.stderr,
    )
    raise SystemExit(2)

sys.argv[0] = str(tool)
sys.path.insert(0, str(tool.parent))
runpy.run_path(str(tool), run_name="__main__")
