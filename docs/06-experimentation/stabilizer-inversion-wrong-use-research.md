# Stabilizer Inversion / Wrong-Use Research

## Status

Canonical research method for AI SLOP mechanism scouting.

This method does **not** assume that every failure-prevention paper contains a useful creative operator. It treats mitigation and stabilization literature as a high-value search surface because those papers often publish the exact ablations, thresholds, dose curves, and failure measurements needed to turn vague instability into a controllable experiment.

## Core idea

Read the literature backwards.

When a paper says it **stabilizes, suppresses, mitigates, corrects, prevents, repairs, regularizes, de-biases, restores, or removes** an undesirable behavior, preserve the paper's measurement apparatus and ask whether the suppressed behavior can be cultivated as controlled material.

The research turn is:

`documented failure -> documented stabilizer -> ablation/dose map -> invert or misplace the stabilizer -> preserve the metric -> test whether the failure becomes structured material`

The point is not "break it harder." The point is to inherit a measured control surface.

## Scout procedure

For every candidate paper:

1. **Name the intended fix.** What failure is the paper trying to remove?
2. **Extract the measurement.** What observable quantity proves the fix worked?
3. **Extract the knob.** Is there a guidance scale, noise level, sink count, timestep, code usage threshold, anchor position, vector ratio, interpolation coefficient, context fill ratio, or other tunable variable?
4. **Read the ablation table backwards.** Which ablation restores the failure? Where is the threshold? What is known to be degenerate?
5. **Preserve the paper's control condition.** The original stabilizing setting is usually the best baseline.
6. **Invert only one thing first.** Remove, reverse, misplace, over-amplify, delay, rotate, contaminate, or selectively apply the stabilizer.
7. **Keep both pressures active.** Reject cases where one condition is simply ignored.
8. **Separate observed from hypothesized.** The source may prove the failure and the fix while our creative inversion remains untested.
9. **Record a falsifier.** State what result would show that the proposed mechanism story is wrong.
10. **Route the result.** Promote only after experiment; otherwise store as a candidate/variant/support instrument.

## Search vocabulary

High-yield search verbs and phrases include:

- stabilize / stabilization
- suppress / suppression
- mitigate
- consistency / coherence
- drift correction
- collapse prevention
- exposure bias
- error accumulation
- oversaturation
- dead code / codebook collapse
- streaming stability
- long-context degradation
- steering interference
- task interference
- model merging failure
- resampling / forcing
- ablation
- dose response
- failure recovery
- regularization
- robust guidance

The useful unit is often not the paper's headline contribution but an ablation figure or appendix that documents exactly what the fix suppresses.

## Required card format

Each retained finding should record:

- **Finding**
- **Source / evidence**
- **Intended use**
- **Weak joint**
- **Wrong-use turn**
- **Anchor**
- **Pressure**
- **Incompatibility**
- **Consequence**
- **Observation**
- **Expected failure surface**
- **Minimum experiment**
- **Media**
- **Relation to existing AI SLOP machinery**
- **Epistemic label**
- **Next action**

## Epistemic rule

A published failure mechanism does not automatically validate our inversion.

Use:
- **OBSERVED** for behavior actually demonstrated by cited sources.
- **HYPOTHESIS** for the proposed creative inversion or new artifact class.
- **VARIANT** when the new work mainly supplies a concrete native-model implementation or knob for an existing operator.
- **SUPPORT** when the source supplies a detector, metric, validator, or control for existing machinery.
- **NEW CANDIDATE** when the intervention changes what the system can do and has no existing operator equivalent.

## Graduation rule

A wrong-use candidate does not become canonical merely because the source is strong.

Promote only after:
1. a reproducible baseline,
2. an isolated intervention,
3. a dose or threshold sweep when possible,
4. at least one ablation/control,
5. failures recorded rather than discarded,
6. creative utility scored separately from mechanism confidence,
7. the mechanism remains distinct after deduplication against the operator registry.

## First scout produced by this method

See:
- `../08-reference/research-cycle-2026-09-20-wrong-use-scout.md`
- `../09-backlog/candidate-mechanisms-2026-09-20-wrong-use-scout.md`

The first run surfaced a particularly strong meta-pattern: **every anti-drift device is documented by what it suppresses.** That is now a standing research heuristic, not a one-off observation.
