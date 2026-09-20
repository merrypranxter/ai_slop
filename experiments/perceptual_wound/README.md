# Perceptual Wound v0.1

This is the first targeted build from the AI SLOP system incubator chain:

**Perceptual Wound -> Silent Scar -> Behavior Archive**

The purpose is not to invent a new Lenia implementation. This experiment uses the public
[jessescool/lenia-umwelt](https://github.com/jessescool/lenia-umwelt) substrate from the 2026
Agnosiophobia work and adds an AI SLOP comparison harness around it.

## Question

What changes when the same region is:

1. absent entirely;
2. physically erased from the organism;
3. hidden from sensing without renormalizing the missing information;
4. hidden from sensing with the source implementation's renormalized blind-mask rule?

The anchor is the same settled Lenia creature. The pressure is an information-only wound. The
important distinction is whether the creature changes because its physical state was damaged or
because its perceptual field was altered.

## Four matched conditions

- **no_mask** — ordinary Lenia update.
- **state_erasure** — masked cells are physically zeroed before each update.
- **unnormalized_occlusion** — masked cells remain physically present, but the sensory
  convolution sees zero there and receives no visibility correction.
- **normalized_occlusion** — masked cells remain physically present and the source project's
  renormalized blind-mask update is used.

The harness estimates the creature's travel direction, puts a circular blind zone in front of it,
and branches all four conditions from the same settled state.

## Measurements

The run logs:

- centroid position;
- heading;
- mass;
- connected components;
- weighted and active-cell overlap with the masked region;
- translation/rotation-insensitive sorted-profile distance from an unperturbed morphology
  neighborhood;
- first return to that neighborhood after an excursion.

Outputs:

- `timeseries.csv`
- `summary.json`
- `blind_mask.npy`
- one final `.npy` state per condition

## Setup

Clone the source substrate separately; it is intentionally not vendored here.

```bash
git clone https://github.com/jessescool/lenia-umwelt.git
cd lenia-umwelt
pip install torch numpy scipy matplotlib imageio tqdm
cd /path/to/ai_slop
```

Run the default O2u assay:

```bash
python experiments/perceptual_wound/run_lenia_occlusion.py \
  --umwelt /path/to/lenia-umwelt \
  --animal O2u \
  --out results/perceptual-wound/O2u-run-001
```

A tiny smoke run is enough to test plumbing, not the hypothesis:

```bash
python experiments/perceptual_wound/run_lenia_occlusion.py \
  --umwelt /path/to/lenia-umwelt \
  --animal O2u \
  --grid 64 \
  --burn-in 20 \
  --heading-probe 8 \
  --neighborhood-steps 20 \
  --steps 20 \
  --mask-radius 5 \
  --mask-ahead 10 \
  --out /tmp/perceptual-wound-smoke
```

## Epistemic status

**PROCEDURAL / HYPOTHESIS.**

The code makes the comparison runnable. It does not claim that the source paper has been
reproduced. A proper first result needs repeated matched runs, preserved configurations, and
failure cases.

The natural-neighborhood metric follows the source project's sorted-activation-profile idea, but
this AI SLOP harness adds its own four-way comparison and output schema.

## What comes next

Do not jump straight to a giant Behavior Archive. The next job is the thing the incubator was
actually waiting for:

**Silent Scar / Second-Injury Assay**

Take visibly recovered runs, save full state, then hit repaired and matched-uninjured systems with
the same standardized second perturbation. Score appearance, internal state, function, and
future response separately.

The scar law is:

**A -> C should differ from A -> B -> C if B actually left a scar.**

If the second injury produces no reproducible difference after controlling for visible state, the
wound did not leave a functional scar and we do not get to call it memory just because the
picture looked haunted.


---

# Silent Scar v0.1 — second-injury assay

Stage 2 is now executable too.

This assay asks the more interesting question: **after the visible form has recovered, does the
system respond differently because it has a different history?**

It constructs two routes from the same settled creature:

```text
CONTROL: seed -> ordinary evolution -> second injury -> response
SCARRED: seed -> transient sensory wound -> visible recovery -> second injury -> response
```

The first wound is the normalized perception-only occlusion from Perceptual Wound v0.1. After
that mask is removed, the wounded route evolves until its sorted activation profile has returned
to the ordinary morphology neighborhood for a sustained window. The control route advances
for exactly the same elapsed time without the first wound.

Then both routes receive the same **class and dose** of second injury: a one-shot circular
physical erasure placed relative to each creature's current centroid and heading. This avoids
pretending two moving organisms should still occupy identical absolute coordinates.

The script records the post-injury response family rather than judging one frame:

- profile-distance excursion;
- recovery time;
- mass loss and recovery;
- connected-component changes;
- centroid displacement;
- complete response time series;
- pre-second-injury state snapshots for both routes.

Run it:

```bash
python experiments/perceptual_wound/run_silent_scar.py \
  --umwelt /path/to/lenia-umwelt \
  --animal O2u \
  --out results/perceptual-wound/O2u-silent-scar-001
```

The key validity field in `summary.json` is
`pre_second_injury.both_visibly_in_natural_neighborhood`. If that is false, the comparison is
not yet a clean Silent Scar test; the first route had not returned to the matched visible
neighborhood before the second injury.

A single divergence is **not** a memory claim. The next experimental pass is a dose/repeat
matrix across mask position, radius, and first-wound duration. The effect earns the name
functional scar only if the history-dependent second-injury response recurs while ordinary
visible morphology has recovered.
