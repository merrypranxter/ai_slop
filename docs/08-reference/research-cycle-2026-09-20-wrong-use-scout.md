# Research Cycle — 2026-09-20 Wrong-Use Scout

## Source

Kimi wrong-use research scout, run 2026-09-20, compared against the current AI SLOP operator registry and the Perceptual Wound / Semantic Fossil work.

## What changed

This cycle did not merely add weird prompt ideas. It found nine mechanism cards by mining stabilization, reliability, interpretability, codec, video, steering, and model-merging literature for measured failure surfaces and then reversing the intended engineering use.

Three findings are especially strong as new operator-grade candidates:
- cyclic denoising attractor cartography;
- attention sink amputation / parking-lot occupation;
- codebook vocabulary mutation / dead-code injection.

Other cards mostly give native technical implementations, controls, or measurable knobs to existing AI SLOP machinery.

## Card 1 — Cyclic Denoising Attractor Atlas

**Observed source claim:** partial-noise encode/decode cycling can reveal ultrastable diffusion memories as dynamical attractors; full noising at γ=1 degenerates to fresh resampling; prompt removal distinguishes prompt-stabilized from memory-stabilized basins.

**Source:** arXiv 2606.24000, *Cyclic Denoising Reveals Ultrastable Memories in Diffusion Models* (2026).

**Wrong-use turn:** use repeated partial-noise cycling as attractor cartography rather than a memorization audit. Sweep γ, record convergence/orbits/escape, find γ* bifurcation thresholds, compare prompt-on vs prompt-removed trajectories, and cluster unlike prompts by shared fixed point.

**Relation:** variant/support for `hysteretic_iteration`, `artifact_fossilization`, and `attractor_perturb`, but adds a continuous dose knob and an operational basin-membership test.

**Next action:** open image model, γ sweep, 20-cycle trajectory grids, prompt-removal ablation.

## Card 2 — Attention Sink Amputation / Parking-Lot Occupation

**Observed source claim:** decoder-only transformers use the first few token positions as attention sinks; removing them can catastrophically raise perplexity, while preserving sink positions restores stability.

**Source:** Xiao et al., *Efficient Streaming Language Models with Attention Sinks* (ICLR 2024, arXiv 2309.17453), plus follow-up softmax variants.

**Wrong-use turn:** treat sink count as a coherence fader; remove 0/1/2/4 sinks or preserve the structural parking positions while changing their occupants. Track where excess attention relocates and whether foreign sink occupants produce content/style bleed.

**Relation:** genuinely new candidate because it intervenes directly in inference-time state rather than only inputs.

**Next action:** reproduce N-sweep on one open model with attention logging, then test 3 occupant classes.

## Card 3 — Guidance-Frequency Jurisdictions

**Observed source claim:** high-CFG oversaturation is strongly associated with low-frequency accumulation; APG separates guidance into parallel and orthogonal components and suppresses the parallel component to reduce oversaturation.

**Sources:** arXiv 2506.21452 (LF-CFG) and arXiv 2410.02416 (APG).

**Wrong-use turn:** amplify the component the fix suppresses; assign different conditions to low- and high-frequency bands; swap band ownership mid-sampling; test positive/sticky momentum.

**Relation:** native sampler-level variant of `separated_jurisdictions` and support for `anchor_mutation_field`.

**Next action:** per-band CFG patch, matched prompt conflict, handoff-timestep sweep.

## Card 4 — Error Accumulation as Video Medium

**Observed source claim:** autoregressive video generation exposes measurable error accumulation, resampling-dose effects, chunk-boundary drift, and global-context anchor placement effects.

**Sources:** Self Forcing (arXiv 2506.08009), Resampling Forcing (arXiv 2512.15702), Knot Forcing (arXiv 2512.21734).

**Wrong-use turn:** invert the stabilizers: misplace anchors, dose resampling corruption, contaminate boundary knots, and measure where drift becomes structured rather than merely destructive.

**Relation:** variant of `hysteretic_iteration`, `anchor_mutation_field`, and `attractor_perturb`, now with three concrete video knobs.

**Next action:** expose anchor position in chunked AR generation and compare forward vs behind anchors on identical prompts.

## Card 5 — Codebook Reset as Scheduled Vocabulary Mutation / Dead-Code Injection

**Observed source claim:** VQ codebooks can contain underused/dead codes; reset/reinitialization methods improve utilization. Hierarchical audio codecs expose multiple discrete levels.

**Sources:** OpenAI Jukebox (2020); CVQ-VAE (ICCV 2023); NS-VQ/TransVQ arXiv 2602.18896.

**Wrong-use turn:** map dead codes, deliberately inject them at controlled rates, reset active codebooks mid-stream, or split corruption across hierarchical/RVQ levels so structure and timbre obey different vocabularies.

**Relation:** new audio-native candidate; supports `separated_jurisdictions` and `token_capability_tax`.

**Next action:** build dead-code usage map on a small VQ audio codec; run injection dose-response and structure-vs-timbre diffs.

## Card 6 — Induction-Head Lesion + Positional Regime Shift

**Observed source claim:** targeted induction-head ablation can severely damage in-context pattern matching while preserving broad fluency; long-context positional bias changes character as relative context fill grows and can invert primacy behavior past roughly half-window regimes.

**Sources:** arXiv 2407.07011; arXiv 2307.03172; arXiv 2508.07479.

**Wrong-use turn:** perform copy-circuitectomy and collect principled pattern near-misses; separately place incompatible instructions in positional jurisdictions and fill the context across the measured regime shift without editing the instructions.

**Relation:** native technical variant of `cognitive_lesion` and `separated_jurisdictions`.

**Next action:** identify top prefix-matching heads, use layer-matched random-head controls, then run pattern and context-fill sweeps.

## Card 7 — Semantic Entropy as Breeding Pressure

**Observed source claim:** semantic entropy measures meaning-level disagreement across sampled answers and predicts hallucination; semantic-entropy probes can estimate this signal cheaply from hidden states.

**Sources:** Farquhar et al., *Nature* 2024, s41586-024-07421-0; arXiv 2406.15927.

**Wrong-use turn:** use semantic entropy as a fitness function rather than a rejection signal. Breed high-but-structured meaning multiplicity and log whether descendant lineages maintain multiple coherent basins or collapse into mush.

**Relation:** support/instrument for `descendant_fitness`, `alien_utility`, and `minority_axis`.

**Next action:** 8-sample clustering loop, 5 generations, cluster-count trajectory per lineage.

## Card 8 — Steering-Vector Stacking to the Coherence/Expressibility Frontier

**Observed source claim:** steering-vector composition degrades as more traits are stacked and exposes a tradeoff between coherence and trait expressibility.

**Source:** arXiv 2607.01802, *On the Limits of Steering Vectors for Preference-Aligned Generation* (2026).

**Wrong-use turn:** deliberately stack contradictory vectors and sweep ratios to map flicker, hybridization, bland midpoint, and collapse regimes.

**Relation:** variant of `separated_jurisdictions` and `minority_axis`.

**Next action:** 3 contradictory vector pairs, ratio sweep, classify flicker vs midpoint vs collapse.

## Card 9 — Loss-Barrier Merging

**Observed source claim:** weight averaging works best inside compatible loss basins; distinct fine-tuning regimes can produce interpolation barriers and task interference.

**Sources:** arXiv 2603.09938 survey; Frankle et al. loss-barrier work; Model Ratatouille / model-merging literature.

**Wrong-use turn:** verify a real interpolation barrier first, then deliberately merge across it; try layer-jurisdiction merges where attention/MLP/embedding blocks inherit different parents; iterate merge → brief fine-tune → merge.

**Relation:** variant of `anchor_mutation_field` and `separated_jurisdictions`; the important new instrument is the loss-barrier gate that verifies the interesting regime before sampling.

**Next action:** two 10× learning-rate-contrast LoRAs on contradictory corpora; plot interpolation loss; only run merge probes when a barrier peak exists.

## Ranked build queue from this cycle

1. Cyclic Denoising Attractor Atlas.
2. Attention Sink Amputation / Parking-Lot Occupation.
3. Dead-Code Injection + codec-level split-brain.
4. Guidance-Frequency Jurisdictions.
5. Semantic-Entropy Breeding.
6. Video anchor inversion / resampling-dose experiments.

This ordering is based on mechanism confidence × creative leverage × cheapness.

## Honest demotions / keep digging

Do not promote these yet:
- reservoir computing at the edge of chaos as an audio medium;
- GAN low-density-region preservation with reprojection removed;
- speculative decoding as a style oscillator;
- Softmax1 / Softpick as a second sink-strength axis;
- cyclic denoising transferred to audio latents;
- reward-model / Goodhart selection pressure for image lineages.

The cycle explicitly demoted weakly sourced ideas instead of turning every interesting phrase into a card.

## Meta-finding

The strongest reusable result is the **Stabilizer Inversion** research pattern:

> When a reliability or consistency paper documents an anti-drift device, its ablations may double as a measured instrument manual for the drift it suppresses.

Canonical method: `../06-experimentation/stabilizer-inversion-wrong-use-research.md`.
