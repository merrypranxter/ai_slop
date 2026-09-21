# Audio / Suno

## Core principle: do not blend; assign jurisdiction

The cleanest audio method in the repo is **Productive Contradiction Under Constraint**.

Construct independent systems for:

- **Harmony** — voicing, consonance/dissonance, tuning relations, harmonic motion.
- **Melody** — contour, ornament, pitch movement, repetition, slides, runs.
- **Rhythm** — pulse, subdivision, meter, syncopation, interruption, silence, density.
- **Timbre / atmosphere** — instrumentation, source material, production space, spectral surface.
- **Performance attitude** — articulation, theatrical/emotional delivery.
- **Anchor / invariant** — one persistent recognizable element while the rest mutates.

Choose ingredients that do not naturally resolve into one genre, but give each a separate job so the model cannot solve the task by making a vague hybrid smoothie.

## Operator construction

Good operators describe transformations:

- hold A fixed while B accelerates;
- stretch one system over a radically different time scale;
- force A to behave according to B’s mechanics without literally becoming B;
- alternate precision and collapse;
- preserve the anchor while spatial/timbral structure migrates;
- make two incompatible temporal scales coexist;
- return to the invariant in a more mutated form;
- remove a frequency band when another system crosses a threshold;
- convert performer articulation into the role formerly occupied by an instrument.

The recurring macro-cycle is:

`FORM → DESTABILIZE → FRACTURE → COLLAPSE → ANCHOR RETURNS → REFORM STRANGER`

Treat this as one useful form, not a mandatory universal song structure.

## Cross-domain transduction

The audio sources repeatedly use physics/chemistry/biology as compositional engines. The useful rule is:

`source-domain behavior → musical affordance → explicit control relation`

Examples:

- **Reaction-diffusion:** motifs expand, interact, suppress/amplify neighbors instead of looping normally.
- **Phase interference:** nearly identical lines reinforce/cancel depending on relative timing/pitch.
- **Phase transition:** a threshold changes rhythmic/harmonic state abruptly.
- **Tectonic slip:** long cycle lengths drift against a stable pulse and realign rarely.
- **Oxidation/asphyxiation:** a growing spectral band subtracts usable harmonic space.
- **Cryptobiosis:** activity nearly stops while an invariant survives and later reactivates.
- **Minimal support / string-bikini logic:** tiny connective material carries disproportionate structural load.

Pseudo-equations in source prompts are creative scaffolds unless they are actually mapped to controllable musical parameters.

## Phonetic engine

Nonsense syllables can be treated as physical sound material:

- plosives → transient/percussive attack;
- nasals → cavity/drone resonance;
- open vowels → sustained melodic carriers;
- rolled consonants → flutter/agitation;
- dense consonant clusters → compressed runs;
- long vowels → time stretching;
- heavy syllables → bass-weight articulation;
- sibilants → hiss/noise/scanline-like textures.

This is stronger than random gibberish because phonetics have assigned jobs.

## Useful source blueprints

The archived audio documents include:

- Cryo-Isorhythmic Tectonic Collapse;
- Pyro-Electric Gamelan Overdrive;
- Tesseract Shoegaze Aberration;
- Reaction-Diffusion Fantasy Collapse;
- Thermodynamic Ingestion;
- Non-Euclidean Xeno-Biology;
- long streams of high-entropy “smol slop” text useful as a specimen of degeneration/noise, not as a canonical control language.

Treat those as case studies: extract their operator relationships rather than copying their costume.

## Route-based composition

The Semantic Manifold system generalizes Suno prompting beyond one-shot prompts. A concept is a waypoint that changes the current musical organism; the final prompt is compiled from the state after the route.

`direct A→C` and `A→B→C` should differ if B performed causal work.

## Common failure modes

- random genre stacking;
- every dimension obeying the same source style;
- human-language lyrics swallowing bracket/control behavior;
- “experimental/chaotic/weird” with no operation;
- contradiction resolved by simply dropping one musical system;
- fake science words with no musical consequence;
- anchor so strong nothing else changes;
- so many constraints that Suno collapses into generic noise.

## Testing

When possible, keep style/instrument inventory fixed and change one operator. Compare multiple generations. The meaningful question is not whether one track is bizarre; it is whether the operator produces a recognizable family of structural consequences.


## Bench-measured codec behavior — Bench 01

The audio branch now has actual measured codec-loop data, not only source-derived hypotheses.

On EnCodec 24 kHz (`d7cc33bc`, deterministic CPU run), RVQ depth behaved as a **signal-class-relative dose dial**: harmonic and chirp probes improved monotonically with more quantizers, bandpassed noise was nearly flat across the ladder, and the impulse probe showed a small mid-ladder regression.

More importantly, repeated recirculation split into two regimes:

- **3 kbps:** contractive; harmonic and noise probes reached float-precision fixed points within tens of iterations;
- **24 kbps:** no fixed point in 100 iterations; outputs wandered while becoming louder and darker, with strong low-frequency accumulation.

This produces a new candidate mechanism, **Fidelity–Stability Inversion**: better single-pass fidelity can coincide with worse iterative stability. The phenomenon is BENCH-MEASURED for one EnCodec checkpoint; the general explanation remains HYPOTHESIS until DAC replication.

Canonical bench note: [`../08-reference/bench-2026-09-19-quantizer-dial-codec-recirculation.md`](../08-reference/bench-2026-09-19-quantizer-dial-codec-recirculation.md).


## Bench 02 — DAC falsification gate

DAC replication killed the broad version of **Fidelity–Stability Inversion**.

Using the same general recirculation protocol on a second codec family:
- DAC contracts at every tested ladder position;
- low-rung harmonic/noise fixed points appear in only a few iterations;
- high-rung noise still reaches a fixed point at iteration 4;
- high-rung harmonic converges slowly rather than wandering;
- DAC shows no EnCodec-style energy inflation.

What now survives across two families:
1. **texture dose-insensitivity** for stochastic noise;
2. **low-ladder contractivity**;
3. **slower convergence as ladder position rises**.

What does **not** survive:
- EnCodec's high-bandwidth louder/darker wander as a family-wide rule;
- the impulse-train mid-ladder wrinkle.

The EnCodec failure remains artistically valuable as an **instrument signature**: a repeatable dynamical behavior unique to the measured setup. This is preferable to pretending a failed generalization never happened.

Canonical note: [`../08-reference/bench-2026-09-21-dac-falsification-gate.md`](../08-reference/bench-2026-09-21-dac-falsification-gate.md).
