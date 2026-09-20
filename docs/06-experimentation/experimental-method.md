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


### Steering and corrective interventions need a repair–corruption frontier

For any intervention intended to "improve" a state, do not report one average score. Record separately:

- bad -> good conversions;
- bad -> bad;
- good -> good;
- good -> bad corruption;
- degenerate / collapsed outputs;
- dose;
- matched-norm random or sham intervention;
- whether an independent detector/gate was used.

An intervention that repairs some failures while damaging more already-good cases is not cleanly beneficial.

### Trajectory-local experiments need full route identity

When a result depends on local instability, inversion, or scheduled intervention, preserve:

- model + version;
- prompt / conditioning;
- initial latent or seed;
- complete schedule;
- local stability / residual trace when available;
- exact intervention intervals;
- intervention history.

For these experiments, prompt or seed alone is not a complete specimen identity.

### Closed-loop controllers need intervention-cost accounting

For controllers that repeatedly act on an evolving system, record:

- action count;
- action magnitude;
- intervention cost/tax;
- time to target;
- post-control viability period;
- amount of continued correction required after apparent success.

Treat the last quantity as **intervention debt**. A system that only survives under constant correction is a different result from one made self-sustaining by a few surgical changes.

### Jurisdiction experiments must log information access

When local/global/decision modules coexist, record what each module is allowed to observe. Global information can become a shortcut that inflates fitness while flattening morphology or bypassing the intended local process.

Compare high score against morphology/behavior descriptors and inspect for metric-exploit solutions.


## Research discovery companion — Stabilizer Inversion

The project now has a dedicated scouting method for mining reliability/stabilization literature for controlled failure instruments:

- start from a documented failure;
- preserve the paper's measurement and baseline;
- identify the stabilizer and its ablation/dose curve;
- invert, misplace, delay, over-amplify, or selectively apply **one** stabilizing component;
- test whether the suppressed behavior becomes structured material rather than generic collapse;
- keep the paper's falsifier and the repo's normal controls.

Canonical method: [`stabilizer-inversion-wrong-use-research.md`](stabilizer-inversion-wrong-use-research.md).

This is a **research-discovery procedure**, not a license to promote every failure-prevention paper into a new operator. Candidates remain backlog hypotheses until they pass the same baseline / repeat / dose / ablation discipline used everywhere else.

## Graduation rule

An idea becomes a reusable operator when it produces a recognizable mutation signature across unlike inputs without destroying task/media fidelity, and when the characteristic effect weakens or disappears under the relevant ablation.

Until then, call it what it is: a juicy hypothesis.
