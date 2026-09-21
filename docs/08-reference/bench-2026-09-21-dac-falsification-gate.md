# Bench 02 — DAC Falsification Gate

## Status

**BENCH-MEASURED — two codec families.**

This report executes the falsification gate declared in Bench 01.

Source report: *AI SLOP — Bench Report 02 | The Falsification Gate*, measured 2026-09-19/21.

Comparison:
- EnCodec 24 kHz, checkpoint `d7cc33bc` — Bench 01;
- DAC 44.1 kHz, 8 kbps model, 9 codebooks — Bench 02;
- same synthetic signal classes;
- same general sweep/recirculation protocol;
- deterministic CPU eval.

The source PDF was supplied in chat. This note preserves its measured claims and the resulting change in project status.

## Verdict

Bench 01 pre-registered a decisive condition:

> If DAC converges at all ladder positions, then the dramatic high-fidelity wander measured in EnCodec is **not** a codec-family law.

That condition fired.

DAC contracts at every tested ladder position. At the top rung:
- noise reaches a fixed point in 4 iterations;
- harmonic recirculation is still converging at iteration 100, with step self-similarity rising to 44.9 dB and positive drift shrinking;
- no energy inflation appears.

Therefore the original broad **Fidelity–Stability Inversion** is **REFUTED as a codec-family law**.

The EnCodec phenomenon remains real and useful, but it is now an **instrument signature**, not a general law.

## What replicated across two codec families

### Law 1 — Texture dose-insensitivity

Bandpassed noise is statistically regenerated rather than sample-faithfully reproduced across the quantizer ladder in both families.

- EnCodec: waveform SNR remains around -2 dB across rungs.
- DAC: approximately -2.05 -> -0.48 dB while spectral distance remains relatively flat.

**Status:** BENCH-MEASURED, two families.

### Law 2 — Low-ladder contractivity

Minimal quantizer settings produce fast fixed points in both families.

Examples:
- EnCodec harmonic: fixed point around iteration 47.
- DAC harmonic: fixed point around iteration 7.
- EnCodec noise: fixed point around iteration 16.
- DAC noise: fixed point around iteration 3.

**Status:** BENCH-MEASURED, two families.

### Law 3 — Convergence slows as ladder position rises

Both families become slower to settle as the ladder rises.

- EnCodec: low rungs converge; top rung did not settle in 100 iterations.
- DAC: low rungs settle in 3–7 iterations; the highest harmonic condition is estimated to require roughly 150+ iterations.

**Status:** BENCH-MEASURED trend, two families. The severity differs sharply by codec.

## What failed to replicate

### EnCodec high-rung wander

DAC does not reproduce EnCodec's high-bandwidth energy-growth regime.

Bench 01 EnCodec:
- harmonic RMS 0.355 -> 0.826;
- noise RMS 0.106 -> 0.926;
- spectral centroid collapses toward ~250 Hz;
- no fixed point observed in 100 iterations.

Bench 02 DAC:
- endpoints hold or slightly lose energy;
- high-rung noise reaches a fixed point almost immediately;
- high-rung harmonic is slowly contractive rather than wandering.

**Conclusion:** EnCodec's louder/darker wander is codec/checkpoint-specific on current evidence.

### Impulse mid-ladder wrinkle

DAC's transient sweep is cleanly monotone.

The EnCodec impulse anomaly therefore does not replicate and is demoted to an EnCodec-specific quirk or measurement artifact until independently reproduced.

## Bug confession / methodological consequence

The first DAC sweep contained an LSD implementation error: one spectrogram stayed in `log10` while the other was converted to `10*log10`.

It was caught because the numbers looked implausible, fixed, and the sweep re-run.

The recirculation/SNR conclusions were unaffected.

This is a useful project-level result in itself:

> **the metric is part of the instrument.**

A measurement pipeline can manufacture a false structure just as easily as a generator can.

## Revised mechanism card

### Fidelity–Stability Inversion (EnCodec)

**Status:** BENCH-MEASURED, single family / checkpoint; REFUTED as a codec-family law.

**Measured behavior:** EnCodec 24 kHz at 24 kbps fails to settle over the 100-iteration horizon and accumulates low-frequency energy, while the same codec at low bandwidth contracts to fixed points.

**Known boundary:** DAC does not reproduce the phenomenon.

**Creative utility:** very high. The failure becoming codec-specific makes it more instrument-like, not less useful.

## New speculative question — the inversion's inversion

Two codec families suggest a possible trade:

- DAC: higher fidelity, fast/polite attractors, lower dynamical richness.
- EnCodec: lower fidelity, larger attractor separation, richer iterative dynamics.

A tempting hypothesis is:

> better reconstruction may be purchased by making the encode/decode map more contractive and therefore less compositionally interesting under iteration.

**Status:** SPECULATION, n=2 families.

Do not promote until a third codec family or an independent EnCodec checkpoint supports an ordered relationship between fidelity and convergence dynamics.

## Project consequences

1. **A falsifier actually killed a broad claim.** This is now a reference example for the repository's experimental method.
2. **The useful object survives the failed theory.** EnCodec's wander remains a bench-characterized dynamical instrument.
3. **The stable cross-family result changed.** The strongest current laws are texture dose-insensitivity, low-ladder contractivity, and slower convergence higher on the ladder.
4. **Codec identity matters as much as dial position.** The same protocol discovers qualitatively different rooms in different codec families.
5. **The project needs instrument signatures, not only universal mechanisms.** A repeatable failure unique to one model family can be artistically more valuable than a boring general law.

## Next bench queue

- third codec family: SoundStream, AudioDec, SpeechTokenizer, or another open codec;
- another EnCodec checkpoint, ideally 48 kHz stereo;
- extend DAC top-rung harmonic to observed convergence rather than extrapolation;
- program material (speech/music);
- compare attractor-family separation as a possible "dynamical richness" metric.

## Epistemic disposition

- broad codec-family Fidelity–Stability Inversion: **REFUTED**;
- EnCodec-specific fidelity–stability inversion: **BENCH-MEASURED**;
- texture dose-insensitivity: **BENCH-MEASURED, two families**;
- low-ladder contractivity: **BENCH-MEASURED, two families**;
- convergence-slowing with ladder position: **BENCH-MEASURED trend, two families**;
- fidelity-vs-dynamical-richness tradeoff: **SPECULATION**.

This report is now the cleanest example in the repo of why falsification is not failure. The general claim died; the instrument got sharper.
