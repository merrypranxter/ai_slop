# Semantic Fossil Instrument

## Status

**PROCEDURAL implementation, v0.1.**

The Semantic Fossil Instrument is an external path-dependence controller. It makes route history explicit and testable without pretending that a hosted model exposes hidden neural state.

Implementation:

- `experiments/semantic_fossil/instrument.py`
- `experiments/semantic_fossil/examples/choir.json`
- `experiments/semantic_fossil/examples/causal-scar.json`
- `experiments/semantic_fossil/test_instrument.py`

Machine run schema:

- `machine/semantic_fossil_run.schema.json`

## Why this exists

The Semantic Manifold architecture says the real artifact is:

`STATE + TRAJECTORY + HISTORY + CURRENT INTERPRETATION`

and that:

`A -> C` must be allowed to differ from `A -> B -> C`.

Earlier experiment material already showed deterministic non-commutative language routes, especially the Semantic Fossil Choir. What was missing was the actual multistep controller that could:

1. keep explicit persistent state;
2. record transformation ancestry;
3. distinguish visible/current state from route scars;
4. restore state without necessarily erasing history;
5. run a true reset ablation;
6. let later operations respond to preserved scars;
7. compare routes and checkpoints;
8. render and archive the result.

That is what v0.1 implements.

## The important distinction: two ledgers

The instrument deliberately separates two kinds of history.

### 1. Causal fossil ledger

This is part of the active external controller state.

Each mutation can leave a fossil record containing:

- operator;
- element;
- field;
- value before;
- value after;
- reason.

Later operators may explicitly test this ledger. That makes route history capable of changing future behavior.

### 2. Immutable audit ancestry

This records what the instrument actually did:

- transforms;
- checkpoints;
- restores;
- hashes before and after;
- restore mode;
- whether the requested restore was exact.

The audit log is provenance. It is never used as secret model memory.

This split is necessary because a **full reset ablation** must be able to remove a scar from causal state while still leaving an honest record that the route passed through the scar-producing operation.

## State model

The minimum state is intentionally hybrid rather than one fake-precise vector.

```text
elements
interpretation
traits
invariants
causal fossils
```

Elements are named persistent entities. An element may carry:

- value;
- meaning;
- active/inactive state;
- anchor status;
- additional user-defined fields.

The instrument currently supplies deterministic string/state transforms rather than a generative model backend. A model can later be placed downstream as a renderer or transformation component, but the controller state remains software-owned.

## Route grammar

A route may contain:

- a named transform, e.g. `A`;
- `{"checkpoint":"name"}`;
- `{"restore":"name","mode":"state_only"}`;
- `{"restore":"name","mode":"full"}`.

### State-only restore

Restores current active state to the checkpoint while **preserving causal fossils accumulated after the checkpoint**.

This creates the critical test condition:

> same visible/current state, different route history.

A later transform can read the surviving fossil and respond differently.

### Full restore

Restores both active state and causal fossils to the checkpoint.

This is the reset ablation. If the later path-dependent effect survives a full restore, then the claimed fossil was not the causal ingredient implemented by this controller.

## Transform operations in v0.1

Current deterministic operations:

- replace;
- context-sensitive replace;
- append;
- prepend;
- set;
- retire;
- activate;
- set interpretation;
- set trait.

Operations can be limited to selected elements, exclude elements, or skip anchors.

They can also use simple history predicates:

- fossil operator seen;
- fossil operator not seen;
- fossil count threshold;
- this element was modified by operator X;
- this element was not modified by operator X;
- active-state check.

This is enough to distinguish **mere logging** from **causal path dependence**.

## Hashes

Three route hashes are kept separate.

### Active hash

Current state with fossils excluded.

Two routes can therefore have the same active hash while carrying different history.

### Fossil hash

Normalized causal fossil content. Route-local provenance fields such as route ID and fossil ID are excluded so equivalent scars can compare equal across routes.

### Causal hash

Active state plus normalized causal fossils.

This is the relevant identity for a controller whose future transitions are allowed to inspect fossil state.

The immutable audit log remains separate and can differ even when causal hashes match.

## Example 1: Semantic Fossil Choir

The first example reproduces the deterministic Experiment L language family.

Rules:

- A: every `p` becomes `f`;
- B: intervocalic `f` becomes `v`;
- anchor: `mora` remains unchanged.

It compares:

- A then B;
- B then A;
- B only;
- A then full reset then B.

The expected non-commutative forms remain:

| Proto | A then B | B then A |
|---|---|---|
| papa | fava | fafa |
| papi | favi | fafi |
| apa | ava | afa |
| pota | fota | fota |
| tafa | tava | tava |
| mora | mora | mora |
| kapi | kavi | kafi |
| sapa | sava | safa |

The full-reset route must match B-only in both active and causal state.

## Example 2: causal scar demo

This is the stronger instrument test.

Three routes begin from the same state.

### DIRECT

`A -> checkpoint(pre_C) -> C`

### VIA_B_STATE_RESTORE

`A -> checkpoint(after_A) -> B -> restore active state only -> checkpoint(pre_C) -> C`

### VIA_B_FULL_RESET

`A -> checkpoint(after_A) -> B -> full restore -> checkpoint(pre_C) -> C`

Before C:

- DIRECT and VIA_B_STATE_RESTORE have the same active state;
- their fossil ledgers differ because the second route passed through B.

C is explicitly written to respond to the presence of a B fossil.

Therefore after C:

- DIRECT and VIA_B_STATE_RESTORE diverge.

The full-reset route removes B from causal history before C. It therefore collapses back onto DIRECT.

That is a complete external causal test:

1. same visible/current state before the critical step;
2. different preserved history;
3. later operation consults that history;
4. downstream behavior diverges;
5. removing the history with a full reset removes the divergence.

This demonstrates path dependence **in the instrument**. It does not demonstrate hidden neural memory in a model.

## Outputs

A run folder contains:

- `spec.json` — frozen input specification;
- `run.json` — minimum machine-readable run record;
- `checks.json` — deterministic replay, anchor, restore, and comparison checks;
- `audit.jsonl` — immutable route ancestry;
- `fossils.csv` — causal scar table;
- `report.md` — human-readable comparison report;
- `archive/index.jsonl` — one archive record per route;
- `routes/<route>/final-state.json`;
- `routes/<route>/projection.txt`;
- `routes/<route>/snapshots.json`;
- `routes/<route>/audit.json`.

The archive stores active, causal, and fossil hashes separately. It therefore does not collapse “same final surface” and “same history” into one equivalence class.

## Run it

Semantic Fossil Choir:

```bash
python experiments/semantic_fossil/instrument.py run \
  --spec experiments/semantic_fossil/examples/choir.json \
  --out results/semantic-fossil/choir-001
```

Causal scar demo:

```bash
python experiments/semantic_fossil/instrument.py run \
  --spec experiments/semantic_fossil/examples/causal-scar.json \
  --out results/semantic-fossil/causal-scar-001
```

Validate an existing run:

```bash
python experiments/semantic_fossil/instrument.py validate \
  --run results/semantic-fossil/causal-scar-001
```

By default the runner refuses to write into a non-empty run folder. Use `--overwrite` only when replacement is intentional.

## Validation contract

v0.1 checks:

- deterministic replay;
- anchor preservation;
- exact active-state restore;
- exact full causal restore;
- declared cross-route comparisons.

The causal-scar example specifically requires all of these:

1. same active pre-C state after state-only restore;
2. different fossil/causal pre-C state;
3. downstream divergence when C reads the scar;
4. full reset makes pre-C causal state equal;
5. full reset removes the downstream divergence.

## Relation to Silent Scar

Silent Scar and Semantic Fossil Instrument are related but not interchangeable.

- **Silent Scar** asks whether a dynamical system that visibly recovered responds differently to a later standardized injury.
- **Semantic Fossil Instrument** gives us an explicit software substrate where route scars, resets, and history-sensitive downstream operations are directly inspectable.

Silent Scar is therefore a behavioral assay on an evolving substrate. Semantic Fossil is a controller/instrument for explicit path dependence.

The strongest future experiments can use both:

- route history is explicit in the controller;
- the rendered/dynamical artifact is independently probed for behavior;
- causal state and visible state can be compared rather than conflated.

## Next extensions

v0.1 intentionally stops before pretending to be a universal creative engine.

Useful next work:

- adapter interface for model-backed transforms;
- renderer plugins for image/audio/shader projections;
- intervention-response descriptors for behavior-sensitive archives;
- route families and dose sweeps;
- external artifact references in fossil records;
- fossil decay, inheritance, and mutation policies;
- scar-sensitive compilation into Semantic Manifold / Suno / visual instructions.

Do not add these merely as decorative vocabulary. Each extension should preserve the same requirement: route history must alter legal or likely future transitions in a way that can be ablated.
