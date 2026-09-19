# DAVID LAB v0.1

A deliberately small first executable layer for AI SLOP.

It does **not** call a model, mutate weights, claim access to latent space, or spend API credits.
It turns the existing machine-readable operator registry and experiment schema into a usable browser workbench.

## What v0.1 does

- reads `machine/operators.json`
- lets a user define an anchor, attacked assumption, and competing conditions
- selects one canonical operator
- assigns a dose/strength
- generates a 5-point boundary sweep around that dose
- emits an experiment record compatible with the spirit of `machine/experiment.schema.json`
- stores draft runs in browser `localStorage`

This is the first layer of the larger proposed system:
**define pressure → run externally → observe → save → compare → breed/mutate later**

## Run it

From the repository root:

```bash
python -m http.server 8000
```

Then open:

```
http://localhost:8000/lab/
```

Opening `index.html` directly as a file may block loading the registry because browsers restrict local file fetches.

## Why this exists

The repository already has strong canonical operator definitions and an experiment schema.
The missing piece is an executable surface that makes them usable without scraping prose or manually building JSON.

v0.1 intentionally stays cheap and boring under the hood.
Later versions can add:
- result collection + scoring
- baseline/control/ablation bundles
- route/scar comparison
- artifact families
- lineage + breeding
- medium adapters
- automated boundary search
- real local/open-model interventions
