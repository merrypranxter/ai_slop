# Experimental Method

The technical roundtable produced one of the strongest rules in the entire repo: **creative utility and mechanism confidence are separate scores**.

A bizarre artifact can be artistically excellent even when our causal story is wrong. Keep the artifact. Test the story.

## Minimum operator record

Every technical/operator experiment should record:

- **NAME** — short stable identifier.
- **STATUS** — observed / supported / hypothesis / speculative.
- **TARGET** — image, video, audio, text/controller; model/version if known.
- **ASSUMPTION ATTACKED** — what default behavior is being pressured.
- **MECHANISM CLAIM** — stated cautiously at the level we can support.
- **COMPETING CONDITIONS** — what remains simultaneously active.
- **PROCEDURE** — the exact controllable changes.
- **EXPECTED ARTIFACT** — what should happen if the idea is right.
- **LIMITATION** — how the system may simply ignore or collapse the conflict.
- **CONTROL** — baseline condition.
- **ABLATION** — remove one causal ingredient.
- **DOSE RESPONSE** — vary strength while holding other variables fixed.
- **SEEDS / REPEATS** — enough runs to distinguish family behavior from a lucky seed.
- **RESULT** — what actually happened.
- **MECHANISM CONFIDENCE** — separate from whether the output fucking rules.

## The basic experiment

1. Run a baseline with ordinary conditions.
2. Change one mechanism variable.
3. Repeat across seeds/tries.
4. Sweep intensity rather than testing only OFF vs MAXIMUM.
5. Remove the supposedly causal component while holding the rest constant.
6. Compare the artifact family, not a single favorite output.
7. Record failure cases.
8. Only then promote an idea from SPECULATIVE/HYPOTHESIS toward OBSERVED/SUPPORTED.

## Interaction experiments

Many project ideas depend on two pressures interacting. Use a 2×2 when practical:

- neither A nor B;
- A only;
- B only;
- A + B.

If A+B looks no different from A, B probably is not doing causal work. If the interaction produces a new family of behavior, that is stronger evidence for a genuine combined operator.

## Stateful/iterative systems

For feedback loops, also record:

- cycle number;
- state before intervention;
- intervention timing;
- history/ledger;
- attractor measures if available;
- when a feature first appeared;
- whether it persisted after its originating condition was removed;
- whether reversing operation order changes the result.

Path dependence is real only if history changes what follows.

## Temporary Minds benchmark inheritance

The cognitive library already defines a useful test discipline: same task, ordinary baseline, mechanism-specific stress test, pairwise-collapse tests, failure ledger, and versioned safeguards. Reuse that spirit across media.

## Lab-note shorthand

```text
SEED / INPUT:
MODEL + VERSION:
OPERATOR:
STATUS BEFORE RUN:
CONTROL:
VARIABLE CHANGED:
STRENGTH / DOSE:
ITERATION / CYCLE:
EXPECTED:
OBSERVED:
WEIRD MOMENT + COORDINATE:
DID IT PERSIST?:
ABLATION RESULT:
MECHANISM CONFIDENCE:
CREATIVE UTILITY:
NEXT TEST:
```


## Additional measurement contracts from the 2026-09-19 full primary-source intake

These are method upgrades, not new operators.

### Recovery is multidimensional

When a system is damaged and "recovers," record separately:

- visible / outward appearance;
- hidden or internal state;
- function / task behavior;
- interaction or communication graph;
- response to the same standardized second perturbation.

Do not infer full recovery from one recovered dimension.

### Mutable-sequence experiments need edit traces

For insertion/deletion/substitution generators, preserve actual edit events. A final answer saying "I revised X" is not evidence that the sequence scaffold performed revision.

### Steering experiments need donor provenance

For activation/SAE steering, record at minimum:

- donor prompt/context;
- extraction token or boundary;
- tail inclusion;
- layer;
- pooling rule;
- subtraction baseline;
- steering norm/strength;
- model/version.

"The vector for X" is not a complete experimental recipe.

### Semantic and perceptual damage are separate axes

For image/video failure injection, score meaning/object/event displacement independently from visible cleanliness or perceptual quality. A clean-looking output can be semantically wrong.

### Transient controllers need finite-time metrics

For flare-and-return systems, record:

- peak gain;
- excursion direction;
- time-to-peak;
- return time;
- saturation/clipping;
- final attractor;
- history dependence.

Do not use "chaos" as a synonym for a large repeatable transient, and do not call slow decay "memory" without a history-dependent test.

### Moving jurisdictions must be compared at matched edit dose

When an edit mask or permission boundary changes over time, compare against fixed-mask and alternate-mask controls at matched edit strength. Record boundary motion separately from the resulting artifact.

## Graduation rule

An idea becomes a reusable operator when it produces a recognizable mutation signature across unlike inputs without destroying task/media fidelity, and when the characteristic effect weakens or disappears under the relevant ablation.

Until then, call it what it is: a juicy hypothesis.
