# Bench 01 — Quantizer Dial & Codec Recirculation

> **Update after Bench 02:** the DAC falsification gate fired. The broad codec-family version of Fidelity–Stability Inversion is **REFUTED**. EnCodec's high-bandwidth wander remains BENCH-MEASURED as an EnCodec-specific instrument signature. Cross-family results that survived: texture dose-insensitivity, low-ladder contractivity, and slower convergence higher on the ladder. See [Bench 02](bench-2026-09-21-dac-falsification-gate.md).

## Status

**BENCH-MEASURED — single codec family / single checkpoint / synthetic signals.**

This is the project's first delivered bench report that replaces literature-only predictions with measurements from an actual run.

Source report: *AI SLOP — Bench Report 01 | The Quantizer Dial & Codec Recirculation*, measured 2026-09-19.

Test substrate:
- EnCodec 24 kHz;
- official checkpoint `d7cc33bc`;
- CPU;
- deterministic eval mode;
- four synthetic 2 s probes: harmonic stack, bandpassed noise, linear chirp, impulse train.

The source PDF was supplied in chat; this repository note preserves the measured result and routing. The current connector cannot archive the uploaded binary PDF itself.

## What changed

Before this run, Topic 06 and the capstone treated RVQ depth as a promising dose dial and codec recirculation as a candidate attractor instrument.

Bench 01 both confirms and corrects that picture.

### R1 — RVQ depth is a real dial, but the gain curve depends on signal class

Across 2 -> 32 quantizers:

- harmonic stack improves monotonically: SNR 5.49 -> 15.58 dB; LSD 31.60 -> 25.31 dB;
- chirp improves monotonically but remains difficult: SNR 0.07 -> 1.97 dB; LSD 44.02 -> 37.36 dB;
- bandpassed noise is nearly dose-insensitive: SNR stays around -2 dB while LSD shifts only 13.05 -> 12.40 dB;
- impulse train is non-monotone: LSD 11.08 dB at 2 quantizers, 11.88 at 8, then 10.39 at 32.

**Canonical correction:** do not describe RVQ depth as one universal monotone fidelity dial. It is a **signal-class-relative dose instrument**.

For structured periodic/swept material, the dose curve is clean. For stochastic texture, waveform identity is destroyed at every rung while texture statistics are regenerated. For transients, a mid-ladder regression appears and remains unexplained.

## R2 — Low-bandwidth recirculation reaches fixed points

At 3 kbps:

- harmonic recirculation reaches float-precision self-similarity by iteration 47;
- noise reaches it by iteration 16;
- drift from the original saturates rather than growing indefinitely;
- harmonic pitch remains recognizable (spectral centroid 416 -> 407 Hz);
- noise darkens substantially (centroid 3941 -> 2193 Hz) but remains noise-like.

This is a genuine reachable fixed-point regime on the measured horizon.

## R3 — High-bandwidth recirculation wanders instead of settling

At 24 kbps, neither tested signal reaches a fixed point in 100 iterations.

Measured effects:
- self-similarity plateaus around 17–18 dB rather than converging;
- harmonic drift reaches -7.98 dB SNR vs original;
- noise drift reaches -18.89 dB;
- RMS grows 0.355 -> 0.826 for harmonic and 0.106 -> 0.926 for noise;
- spectral centroid collapses toward roughly 240–280 Hz.

The result is not simple decay-to-noise. The loop becomes louder and darker while continuing to move.

## Candidate mechanism — Fidelity–Stability Inversion

**Measured phenomenon:** for this EnCodec setup, the setting with better single-pass fidelity is less stable under repeated recirculation.

Low bandwidth behaves contractively and reaches reduced fixed points.

High bandwidth preserves more per-pass detail but remains iteratively unstable over the 100-pass horizon.

**Mechanistic explanation remains HYPOTHESIS.** One plausible account is that low-bandwidth quantization collapses the reachable output set enough that the loop runs out of directions to move, while the high-bandwidth system preserves enough representational freedom for small decoder deviations to re-enter as signal and compound.

Do not promote this to a codec-family law until DAC replication.

## Falsification / replication gate

The next decisive test is the same protocol on DAC or another materially different codec geometry.

If the fidelity–stability inversion disappears or every bandwidth contracts, then the effect is EnCodec-specific tuning. That would reduce generality but not creative usefulness.

## Required follow-up

1. DAC replication.
2. Extend high-bandwidth recirculation to 300–1000 iterations: fixed point, limit cycle, clipping, or continued wander?
3. Per-rung quantizer-dropout ablation to locate the rungs carrying instability.
4. Program material: speech and music, not only synthetic probes.
5. Dense 2->32 rung sweep for the impulse anomaly.
6. Listening evaluation, because SNR/LSD are not perceptual ground truth.

## Cross-project consequences

### Audio
The project now has a bench-measured audio dose instrument rather than only a cited proposal.

### Iteration grammar
The old statement "every recirculation channel has an attractor" is too strong. The grammar needs at least two measured regimes:
- **contractive / fixed-point**;
- **wandering / non-converged on observed horizon**.

Limit cycles remain an open third case.

### Capstone
The unified dial library should be corrected from "RVQ depth = monotone texture deletion" to:

> RVQ depth is signal-class-relative: monotone for some structured signals, flat for stochastic texture, and locally non-monotone for tested transients.

### Loop thesis
This run strengthens the project claim that important failure behavior can be generated by the loop itself. The same codec/checkpoint changes qualitative regime when the recirculation condition and bandwidth change.

## Promotion decision

- **Quantizer dial:** BENCH-MEASURED, with signal-class qualifier.
- **Codec fixed points at low bandwidth:** BENCH-MEASURED for this setup.
- **High-bandwidth wandering / energy inflation:** BENCH-MEASURED for this setup.
- **Fidelity–Stability Inversion as a general codec-family mechanism:** REFUTED by DAC replication; retained only as an EnCodec-specific measured phenomenon.

This is exactly the epistemic progression the repo is designed for: citation -> prediction -> run -> correction -> new candidate mechanism -> falsification gate.
