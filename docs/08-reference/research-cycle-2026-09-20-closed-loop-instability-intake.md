# AI SLOP Research Integration Notes
## Closed-loop intervention / instability / evolvable jurisdiction intake — 2026-09-20

**Source:** `Perplexity AI slop research today.pdf`

**Status:** research intake only. No canonical operator promotion from this pass.

## Executive delta

This cycle does contain genuinely new project material relative to the current repo. The strongest additions are not new aesthetics; they are control architectures and evaluation contracts:

1. **Sparse Autotelic Perturbation** — a closed-loop controller watches an evolving system, makes small local interventions, and pays a cost for every intervention.
2. **Instability-Gated Intervention** — use trajectory-local failure/convergence signals as an address for where and when to intervene.
3. **Evolvable Jurisdiction Stack** — explicitly separate local measurements, global measurements, and decision logic into independently mutable program modules.
4. **Repair–Corruption Frontier** — score beneficial conversions and damage to already-good samples separately instead of hiding them in one average metric.
5. **Symbiotic Fitness** — assign fitness to a relationship/consortium when capability exists only in the interaction.
6. **Trajectory Fossils** — preserve unstable latents, residual schedules, or failure intervals as reusable route state rather than discarding them.

The cycle also usefully reclassifies Flow Lenia: not a new operator, but a literal substrate in which local laws move with organisms.

---

# F11 — CARL / Artificial Experimentalist

**Source:** Cvjetko, Hartl, Levin, Moulin-Frier, Oudeyer, `The Artificial Experimentalist: Discovery and Control of Self-Organizing Phenomena with Autotelic Reinforcement Learning`, arXiv 2608.26116v2.

**Classification:** candidate regulator / experimental architecture; possible future Temporary Mind substrate.

### What is demonstrated
A goal-conditioned RL policy observes a live Lenia field and repeatedly chooses local add/remove/no-op interventions. Intervention itself carries an explicit cost. The controller can discover or maintain persistent localized patterns and steer existing solitons, with incomplete but real transfer to held-out rules/action settings.

### What is new for AI SLOP
Feedback control already exists in the project. The new operational ingredient is:

**closed-loop observation + high-level target + sparse local action + explicit intervention tax + replaceable goals**

The intervention tax matters. It pressures the controller to make the substrate do as much of the work as possible.

### Proposed project term
**Sparse Autotelic Perturbation**

### Secondary metric
**Intervention Debt:** how much continued external correction an artifact requires to remain viable after control begins or ends.

### Useful creative sweep
- zero intervention cost -> micromanaged surface churn;
- moderate cost -> occasional surgical scars;
- high cost -> rare interventions or collapse;
- time-varying cost -> alternating dependence/autonomy regimes.

### Boundaries
Do not claim:
- open-ended evolution;
- autonomous goal invention;
- severe-damage regeneration;
- transfer to proprietary generative models;
- that discovered patterns are novel species.

### Next investigation
Verify code/checkpoints/API, action-cost ablations, and whether the controller can act on Flow-Lenia local rule parameters rather than mass alone.

---

# F12 — High-CFG inversion / Prompt Pressure / SkipInv

**Source:** Zeng, Hosoya, Tran, Okatani, `When Does High-CFG Diffusion Inversion Fail? A Controlled Study of Prompt–Latent Interactions`, arXiv 2607.04731v2.

**Classification:** validator + diagnostic variable + technical intervention candidate.

### What is demonstrated
The work studies fixed-point inversion across prompt/latent pairs and introduces timestep-resolved **prompt pressure**, measuring the conditional guidance displacement from the unconditional trajectory. Failures are relational: prompts divide into easy, hard, and intermediate latent-sensitive regimes. SkipInv relaxes guidance only when an inverse step becomes locally unstable.

### What is new for AI SLOP
The useful thing is not "high CFG can fail." The new piece is that failure can be **temporally localized and prompt–latent specific**, giving us an address for intervention.

### Proposed project term
**Instability-Gated Intervention**

Intervene only at timesteps where a local instability/convergence signal crosses a threshold.

### Proposed artifact class
**Trajectory Fossil**

Persist one or more of:
- unstable latent states;
- fixed-point residual spikes;
- instability interval boundaries;
- intervention schedule;
- local guidance oscillation history.

Reuse them as generative conditions in later routes.

### First artistic inversion
Build an **Anti-SkipInv** analogue:
- ordinary SkipInv = relax guidance at unstable steps;
- Anti-SkipInv = increase, alternate, freeze, or reroute guidance specifically at unstable steps.

### Required ledger identity
For this class of experiments, the minimum identity becomes:

`MODEL + PROMPT + LATENT + SCHEDULE + INTERVENTION HISTORY`

A prompt or seed alone is not enough.

### Boundaries
Do not generalize from SD1.4/DDIM/FPI to all diffusion/flow architectures without testing.

---

# F13 — Programmable Cellular Automata

**Source:** Khalifa, Nasir, Siper, James, Togelius, arXiv 2609.06102v2.

**Classification:** new implementation architecture / generator-evolution protocol / interpretable substrate.

### What is demonstrated
A CA is represented as modular executable code:
- local functions produce neighborhood measurements;
- optional global functions inspect the entire state;
- a decision function combines them;
- modules mutate/crossover independently;
- an LLM can synthesize replacement Python functions.

Global modules helped solve small PCG tasks that local-only propagation handled poorly, but could also become metric-cheating shortcuts.

### What is new for AI SLOP
The project already has Separated Jurisdictions. The new implementation pattern is making the jurisdiction boundary itself **explicit, executable, evolvable, and attributable**.

### Proposed project term
**Evolvable Jurisdiction Stack**

- local modules govern texture/neighborhood behavior;
- global modules compute conservation, rarity, connectivity, composition, etc.;
- decision module negotiates between them;
- mutation rates can differ by jurisdiction.

### Critical warning
Global knowledge can become useful cheating. The system must track:
- what information each jurisdiction is allowed to see;
- which global signals are leaked into local decision making;
- whether a high score comes from structurally trivial shortcut morphology.

### Next implementation idea
Port a small version to JavaScript with functions restricted to GLSL-compatible expressions, and preserve source/lineage for every surviving generator.

---

# F14 — Mechanistic Interpretability of Code Correctness

**Source:** 2026 OpenReview manuscript, exact venue/version still unresolved in the source cycle.

**Classification:** validator update, not a new steering operator.

### What is demonstrated
Correctness-associated directions can predict some failure structure, but universal steering has asymmetric collateral damage: the source reports repair of 4.04% of erroneous programs while corrupting 14.66% of initially correct programs. Degenerate repetition also appears under steering.

### What is new for AI SLOP
Not "steering has side effects." The useful upgrade is to treat repair and corruption as **two response surfaces**.

### Required evaluation
**Repair–Corruption Frontier**

For every steering/intervention family record:
- bad -> good conversion rate;
- good -> bad corruption rate;
- unchanged bad;
- unchanged good;
- degeneration rate;
- dose;
- matched-norm random direction;
- independent gating detector.

### Proposed control architecture
**Selective Intervention Gate**

Classify whether a current state is likely to benefit before applying an operator.

This should modify the project experimental method immediately, even though the steering mechanism itself is not new.

---

# F15 — Flow Lenia reclassified

**Source:** Plantec et al., Flow Lenia.

**Classification:** existing mechanism implementation / substrate. Merge, do not duplicate.

### What matters now
Flow Lenia localizes rule parameters inside the field. Multiple structures can carry different local rule regimes through the same world.

### Proposed descriptive term
**Localized Law Carriage**

A structure transports its own transformation parameters through a shared field and may blend/exchange those parameters on contact.

### Why this became more important now
CARL supplies a plausible controller that could act not just on mass, but on local rule fields. That combination is new even though Flow Lenia itself is not.

---

# F16 — Barricelli / SymBa symbiogenesis revival

**Source:** Ashford et al., SymBa / ALICE 2026 workshop.

**Classification:** speculative selection hypothesis / experimental protocol.

### What is demonstrated
Historical Barricelli-style replication, 2D extensions, and preliminary collective/symbiotic constraints. Evidence is workshop-scale and does not establish mature open-ended evolution or collective intelligence.

### Proposed project term
**Symbiotic Fitness**

Score the persistent **relationship or consortium**, not the individuals.

A valid symbiotic case should require:
- order sensitivity;
- pair specificity;
- persistence after separation;
- failure under shuffled partners;
- reproducible offspring effects;
- a joint capability neither member produces alone.

### Relation to current project
This is distinct from crossover/blending. It belongs near Descendant Fitness, breeding, operator ecology, and cross-artifact feedback.

---

# Updates to existing project ideas

## Feedback control
CARL strengthens feedback/control work but only its **sparse costed intervention** is new.

## Separated Jurisdictions
Programmable CA gives an executable local/global/decision architecture and exposes **global leakage** as an experimental variable.

## Activation steering
Add the repair–corruption frontier to donor-provenance, random-basis, matched-norm, and dose-response controls.

## Failure as specimen
High-CFG inversion adds a way to **locate failure along the route**, not merely observe the failed output.

## Open-endedness
Continue to reject "diverse snapshots = open-ended evolution." Require sustained novelty, inheritance, and non-saturation evidence.

## Flow Lenia
Merge as a substrate under Property Unbundling + Separated Jurisdictions; do not mint a redundant operator.

---

# Strong combination signals created by this cycle

1. **CARL + Flow Lenia** -> sparse controller edits mass and/or local law fields; measure post-control autonomy.
2. **Instability-Gated Intervention + Semantic Fossil Instrument** -> unstable intervals become addressable route fossils.
3. **Instability-Gated Intervention + Controlled Temporal Leakage** -> intervene only when the trajectory crosses a local failure boundary, then control whether damage spreads.
4. **Programmable CA + Operator Genetics** -> breed executable local/global/decision modules rather than prompt prose.
5. **Symbiotic Fitness + Mr. Slop breeding** -> relationship can become the reproductive unit instead of one child artifact.
6. **Selective Intervention Gate + Steering Donor Provenance** -> a steering direction is applied only where an independent detector predicts net benefit.

---

# Research gates / unresolved checks

- CARL official code, license, checkpoints, and intervention API.
- SkipInv implementation and access to timestep residual logs.
- Official Programmable Cellular Automata repository.
- Flow-Lenia + CARL compatibility.
- Code-correctness paper exact version/authors/code and random-direction controls.
- SymBa replication code and quantitative symbiosis criteria.
- Hugging Face artifact lineage remains incomplete in the source cycle.

---

# Disposition

## ADD TO BACKLOG
- Sparse Autotelic Perturbation
- Instability-Gated Intervention
- Evolvable Jurisdiction Stack
- Symbiotic Fitness
- Trajectory Fossil
- Intervention Debt

## UPDATE METHODS
- Repair–Corruption Frontier
- full route identity: model + prompt + latent + schedule + intervention history
- global-knowledge leakage as a jurisdiction variable
- morphology/behavior validation against metric-cheating solutions

## MERGE
- Flow Lenia -> Property Unbundling + Separated Jurisdictions
- generic feedback language -> existing controller architecture
- generic prompt pressure -> guidance dynamics; retain trajectory-local instability
- ordinary program evolution -> meta-genomic/operator evolution; retain explicit jurisdiction modules

## DO NOT PROMOTE YET
No canonical operator JSON changes until implementations/ablations show reproducible, distinct behavior.
