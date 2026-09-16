# DAVID Technical Hypotheses

## Status of this file

The technical roundtable is one of the richest idea sources in the repo and one of the easiest places to mistake elaborate explanation for established mechanism. Treat this as a **hypothesis registry**.

Its most valuable contribution is methodological: technical vocabulary must be operational, proprietary internals must not be invented, and every operator needs controls, ablations, dose-response sweeps, limitations, and replication across seeds.

## Primary failure-surface taxonomy

The roundtable explores:

- text/reference conditioning conflict;
- feature binding and attribute leakage;
- sequence-distance / prompt-budget effects;
- denoising or flow-trajectory sensitivity;
- iterative encode/decode drift;
- latent/reference overconstraint;
- temporal correspondence and feature reassignment;
- topology instability through time;
- tokenization / delimiter effects;
- VAE/compression artifacts becoming semantic structure;
- positional encoding and aliasing hypotheses;
- source separation, phase, meter, tuning, and hierarchical-form conflict in audio.

## Named operators extracted so far

### CMMS — Cross-Modal Manifold Shear
**Status:** HYPOTHESIS  
**Recipe idea:** strongly anchor identity/reference while another conditioning signal pushes toward a poorly compatible geometry/material regime.  
**Expected family:** material leakage, connective tissue, partial satisfaction, identity/geometry compromise.  
**Critical control:** remove reference conditioning while holding text/guidance constant.

### SP-DUS — Syntactic Possession via Dual-Use Strata
**Status:** SPECULATIVE HYPOTHESIS  
Claims malformed/nested formal syntax may alter text-encoder representation enough to affect spatial/temporal output. A later participant correctly challenges the story: denoisers do not receive an AST; any effect would have to emerge through the contextual text embeddings, token norms, sequence structure, or learned correlations.  
**Required test:** raw delimiter structure vs natural-language equivalent with same meaning.

### Attention-Sink Collision (correction to SP-DUS)
**Status:** HYPOTHESIS  
More technically cautious formulation: unusual token patterns may redistribute attention or encoder representation, which could affect conditioning. Do not claim a bracket literally “carves” image space without instrumentation.

### HICC — Hierarchically Inverted Conditioning Crossfade
**Status:** HYPOTHESIS  
**Recipe idea:** change conditioning at different stages/strengths of a controllable generation trajectory to test whether already-established coarse structure constrains later attempts to impose incompatible local properties.  
**Caveat:** the source gives exact timestep bands as if universal. They are not canonical facts; sweep the boundary empirically per model/scheduler.

### RBC-AS — Remote Binding Cleavage via Attention Starvation
**Status:** HYPOTHESIS  
**Recipe idea:** vary distance and competition between an entity and its required modifier; test whether binding weakens, the attribute drops, migrates, or nucleates a second host.  
**Strong experimental value:** sequence-distance sweep and adjacent-token ablation are easy to define.  
**Caveat:** “finite attention budget” is useful intuition, not permission to claim a specific softmax-starvation mechanism for every architecture.

### NCHR — Non-Commutative Hysteretic Ratchet
**Status:** HYPOTHESIS with strong observable experiment  
**Recipe idea:** alternate partial transformations A and B across repeated image-to-image, continuation, or remix cycles; compare A→B→A with B→A→B and direct endpoints.  
**Expected family:** irreversible semantic drift, fossilized intermediate structures, accreted connective tissue, path dependence.  
**Why it matters:** this can be tested from outputs without pretending to inspect hidden state.

### CC-CAE — Categorical Cancellation via Competing Attractor Equilibrium
**Status:** HYPOTHESIS  
Broad idea: maintain competing category pressures near a boundary where neither cleanly wins; look for hybrid representations or oscillating assignment rather than simple averaging/dropout.

### UEP-GD — Unconstrained Embedding Projection via Glitch Dispersion
**Status:** SPECULATIVE  
Retain as an experiment family only after its operational recipe is separated from claims about hidden embedding geometry.

### ARS-FBA — Anisotropic RoPE Shear via Frequency-Band Aliasing
**Status:** HIGHLY ARCHITECTURE-SPECIFIC HYPOTHESIS  
Potentially useful only on systems where the relevant positional representation and controls are actually known/exposed. Do not generalize it to black-box image/music models.

## How an operator graduates

For each operator:

1. Specify an accessible model/tool and exact controllable variables.
2. State what observation would differ from a simpler explanation.
3. Build an ablation that removes only the proposed interaction.
4. Sweep strength/timing/distance rather than trying one dramatic setting.
5. Repeat across seeds.
6. Record whether the system ignores one condition, saturates, or produces a stable artifact family.
7. Separate “this makes amazing shit” from “our mechanistic explanation survived testing.”

## Do not inherit source overconfidence

The source sometimes uses exact equations, layer claims, attention maps, or timestep thresholds without evidence that the named proprietary/black-box system exposes those quantities. Canonical experiments must scale their causal claims to what can actually be measured.

Source: `ai_readable/general/04-ai-slop-roundtable-tech-guys.md`.
