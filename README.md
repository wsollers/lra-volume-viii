# lra-volume-viii

**Volume VIII: Applied and Computational Mathematics** — Overleaf-ready standalone repository.

## Structure

```text
volume-viii.tex          — full-volume root (Overleaf main document)
volume-viii-<book>.tex   — individual book roots
common/               — shared LaTeX infrastructure supplied by lra-common; ignored here
bibliography/         — per-book bibliography shards
volume-viii/             — all LaTeX content for this volume
```

## Overleaf

Upload or checkout `common/` beside this repository's TeX roots, then set the main document to `volume-viii.tex` for the full volume or to one of the book roots:

```text
volume-viii-applied-methods.tex, volume-viii-numerical-foundations.tex
```

`common/` is ignored by git in this volume repo; edit shared infrastructure in `lra-common`.

## Building locally

```powershell
python F:\repos\lra-governance\tools\governance\build_volume_docker.py --root F:\repos\lra-volume-viii --common-root F:\repos\lra-common
```
