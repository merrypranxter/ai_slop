# Epistemic Status and Technical Hygiene

This repo mixes art practice, prompt craft, software-controlled experiments, genuine ML concepts, intentionally theatrical prose, and AI-generated technical speculation. That mixture is fertile as hell and also a perfect factory for accidental bullshit. This file is the firewall.

## Status labels

### OBSERVED
Repeated behavior documented in actual runs. Observation does not imply a universal internal cause.

### SUPPORTED
Mechanism is broadly consistent with established public technical understanding and the experiment is framed at the correct level of abstraction.

### HYPOTHESIS
A plausible explanation of behavior that needs controls, ablation, and ideally replication across seeds/models.

### PROCEDURAL
A property our own prompt/controller/software explicitly imposes. Example: TOPOS-SRE increments a decay variable. This says nothing about the generator literally “decaying” internally.

### METAPHOR
Useful project language with no literal technical claim. “Latent-space vandalism,” “semantic scars,” “the void,” “the creature,” and “honest slop” often live here.

### SPECULATIVE
An experiment or architecture worth trying with insufficient evidence to claim a mechanism.

### ARCHIVED / SUPERSEDED
Preserved for history but replaced, merged, demoted, or rejected in current architecture.

## Claims that need automatic skepticism

- Exact hidden-layer behavior inferred only from a text/image result.
- Claims that punctuation or specific tokens “hijack attention heads” without instrumentation.
- Claims that prompt wording literally modifies weights or embeddings.
- Claims that a commercial model exposes or executes encoded instructions “before safety sees them.”
- Universal timestep boundaries like “macro geometry always finishes at t=.70.”
- Statements that an output is “raw tensors” or “the base model speaking.”
- Claims that a model “cannot” represent something unless tested.
- Proprietary implementation details presented as known facts.
- One-off artifacts presented as a stable operator.

## How to salvage an overclaim

Do not throw away a useful experiment because its explanation is dramatic.

Split it into:

1. **Observable recipe** — what we actually changed.
2. **Observed result** — what happened.
3. **Plausible mechanism** — why it might have happened.
4. **Alternative explanations** — what else could cause it.
5. **Ablation/control** — what to remove or hold fixed.
6. **Status** — hypothesis until evidence improves.

This pattern converts “AI folklore” into usable experimental material.

## Special note on “latent space”

Different model families have different representations, and many generative systems involve multiple embedding/latent/hidden spaces rather than one master map. The project may use “latent space” conversationally because it captures the experience of conceptual navigation. Software documentation should say what representation is actually being manipulated: external embeddings, explicit state vectors, prompt conditions, image latents, audio features, controller variables, etc.

## Special note on safeguards

Historical documents contain explicit jailbreak/bypass rhetoric. Canonical material should extract any benign generative insight without preserving “bypass the filter” as a goal or claiming success at doing so. Technical specificity is valuable because it can produce better-controlled art; it is not evidence that safeguards were circumvented.
