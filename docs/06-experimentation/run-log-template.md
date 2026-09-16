# Experiment Run Log Template

Use this for any test where the mechanism matters, especially DAVID operators, iterative image/video/audio loops, Temporary Mind benchmarks, SRE perturbations, and Semantic Manifold route comparisons.

The goal is not paperwork for its own sake. The goal is to make it possible to tell the difference between **a repeatable artifact family**, **a lucky freak**, and **a cool result produced for the wrong reason**.

## Copyable run record

```yaml
run_id:
date:
researcher:
media: image | video | audio | text | controller | mixed
model_or_tool:
model_version:
operator_ids: []
epistemic_status_before: SPECULATIVE | HYPOTHESIS | OBSERVED | SUPPORTED | PROCEDURAL

input_or_seed_material:
seed_or_randomness:
reference_assets:

assumption_attacked:
mechanism_claim:
competing_conditions:
invariant_or_anchor:

baseline:
control:
ablation:
independent_variable:
dose_or_strength:
iteration_or_cycle:
operation_order:

expected_artifact_family:
condition_dropout_risk:
known_confounds:

observed_result:
artifact_coordinates_or_timestamps:
persistence_after_cause_removed:
route_or_history_effect:

creative_utility: null
mechanism_confidence: null

next_test:
notes:
```

## What the scores mean

`creative_utility` and `mechanism_confidence` are deliberately separate. Use whatever numeric scale is convenient for a batch, but define it before comparing runs.

A result can be **artistically excellent and mechanistically uncertain**. That is not failure. It means the artifact belongs in the creative lineage while the causal story remains a hypothesis.

## Minimal comparison sets

For a one-variable operator, prefer at least:

- baseline;
- operator on;
- ablation/control;
- a small dose sweep;
- more than one seed/input.

For an interaction between A and B, use the 2×2 whenever practical:

| Condition | A | B |
| --- | --- | --- |
| baseline | off | off |
| A only | on | off |
| B only | off | on |
| interaction | on | on |

For path claims, compare routes, not just endpoints. A minimum useful set is often:

`A → C` versus `A → B → C`

and, when order is part of the claim:

`A → B` versus `B → A`

## Artifact-family record

Do not record only the single prettiest output. Describe the repeated mutation signature across the batch:

- what recurred;
- what varied;
- which condition caused dropout;
- which conditions destroyed fidelity;
- whether the artifact survived after the originating pressure was removed;
- whether direct endpoint generation could reproduce it;
- whether the family generalized to unlike inputs.

That family description is what allows an operator to graduate from **juicy hypothesis** to something reusable.
