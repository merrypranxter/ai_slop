# Semantic Fossil Instrument v0.2

An external, inspectable path-dependence controller for AI SLOP.

The instrument keeps four things separate:

1. current active state;
2. causal fossils that later operations may read;
3. immutable audit ancestry;
4. current interpretation.

That distinction makes a clean reset experiment possible.

## The core test

A route can restore its visible/current state to an earlier checkpoint while keeping its fossil ledger.

Then a later operator can respond to the fossil.

So this becomes possible:

```text
DIRECT:
A -> C

VIA:
A -> B -> restore active state -> C

ABLATION:
A -> B -> full restore -> C
```

Immediately before C, DIRECT and VIA can have the same active state while VIA still carries the B fossil.

If C explicitly reads that fossil, the outputs diverge.

If a full reset removes the fossil and the divergence disappears, the instrument has a complete external path-dependence mechanism rather than a spooky story about "memory."

## Quick start

Run the original deterministic Semantic Fossil Choir:

```bash
python experiments/semantic_fossil/instrument.py run \
  --spec experiments/semantic_fossil/examples/choir.json \
  --out /tmp/fossil-choir
```

Run the causal scar demonstration:

```bash
python experiments/semantic_fossil/instrument.py run \
  --spec experiments/semantic_fossil/examples/causal-scar.json \
  --out /tmp/fossil-scar
```

Validate:

```bash
python experiments/semantic_fossil/instrument.py validate --run /tmp/fossil-scar
```

Run tests:

```bash
python -m unittest experiments/semantic_fossil/test_instrument.py -v
```

No third-party Python dependencies are required.

## Outputs

Every run writes:

- `run.json` — minimum run record;
- `checks.json` — validation results;
- `audit.jsonl` — immutable ancestry;
- `fossils.csv` — causal fossil ledger;
- `report.md` — readable route comparison;
- `archive/index.jsonl` — route signatures;
- route-specific states, projections, snapshots, and audits.

The runner refuses to reuse a non-empty output folder unless `--overwrite` is supplied.

## Epistemic boundary

This is application state. It is not a hidden-activation viewer, latent-space probe, or claim that prompts rewrite model memory.

That limitation is a feature: because the state is explicit, we can actually ablate the fucking thing.


---

## Creative bridge

v0.2 can now compile route state into **Suno** and **visual** instructions, write provider-neutral request packets, and ingest the resulting media back into route history as explicit artifact fossils.

Compile every route:

```bash
python -m experiments.semantic_fossil.creative compile \
  --run /tmp/fossil-scar \
  --renderer all
```

Write a transform packet for a local or external generator:

```bash
python -m experiments.semantic_fossil.creative packet \
  --run /tmp/fossil-scar \
  --route VIA_B_STATE_RESTORE \
  --renderer visual \
  --out /tmp/fossil-requests
```

After generation, ingest an artifact:

```bash
python -m experiments.semantic_fossil.creative ingest \
  --run /tmp/fossil-scar \
  --route VIA_B_STATE_RESTORE \
  --medium image \
  --file rendered.png \
  --operator visual_renderer \
  --descriptor identity_anchor_preserved=true \
  --descriptor topological_damage=0.72
```

The generated file is copied into the run folder. Its hash, path, media type, and explicit descriptors become a new fossil overlay. Compile the route again and later instructions can respond to that recorded artifact.

### Current plugin surfaces

- `adapters/` — provider-neutral model/generator boundary;
- `renderers/` — medium-facing output plugins;
- `compilers/suno.py` — route history -> Suno style + lyrics/control;
- `compilers/visual.py` — route history -> visual generation prompt;
- `artifacts.py` — artifact storage, hashing, descriptors, and fossilization;
- `creative.py` — command-line bridge.

The base experiment record stays frozen. Post-render artifact fossils live in `artifact-fossils.jsonl` and are overlaid only when compiling later creative passes.
