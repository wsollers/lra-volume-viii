#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$ROOT"

LRA_PRINT_EDITION=1 latexmk -g -lualatex -interaction=nonstopmode -halt-on-error -jobname=main-print main.tex "$@"
