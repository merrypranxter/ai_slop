# AI SLOP Research Integration Notes
## Living Ledger Cycle 1 - source labeled 2026-09-20

**Repository target:** `merrypranxter/ai_slop`

**Status:** research intake only. Nothing in this document is promoted to a canonical operator or system yet.

**Date note:** the supplied ledger is labeled **2026-09-20**. It was ingested during the 2026-09-19 working session, so keep the source label as-is rather than silently normalizing the date.

## Why this cycle matters

This cycle does not mainly add more prompt tricks. It adds several concrete technical mechanisms that line up with existing AI SLOP themes: steering, sparse feature surgery, temporal drift, quality-diversity archives, developmental systems, iterative editing, and field evolution.

The useful shift is from "we can describe this weird behavior" toward "there are now published or open implementations that may let us manipulate the relevant variable directly, or at least test a cleaner analogue of it."

Do not build a new cathedral of terminology around every paper. Preserve the findings, map them to existing machinery, and wait for a few more scouting cycles before deciding which combinations deserve systems.

---

## Shift 1 - Audio moves from prompt conflict toward representation-level steering

### Source lead
**TADA! - Tuning Audio Diffusion Models through Activation Steering** (arXiv 2602.11910; ledger identifies ICLR 2026 Re-Align WS)

Ledger summary:
- activation steering / activation patching for audio diffusion;
- tested on ACE-Step, AudioLDM2, and Stable Audio Open;
- benchmark of eight steering methods on functional layers;
- open code and Hugging Face steering artifacts;
- follow-up seeds: CASteer, AUSteer, Universal DiffSAE, SMITIN, SAE-on-MusicGen.

### What changes for AI SLOP
We already use contradictory instructions, role exchange, alien metrics, temporal rules, and recursive contamination to pressure music generators from the outside. TADA creates a more direct technical reference point: **specific internal layers may carry controllable musical or semantic behavior that can be pushed without retraining the whole model.**

This does not mean Suno exposes those layers. It means our prompt-induced audio experiments now have a technical cousin that can be tested on open models.

### Candidate research direction
**Audio Functional-Layer Steering**

Questions to preserve:
- Which layers affect local timbre, rhythm, intensity, instrumentation, form, or semantic content?
- Does steering one layer create collateral changes elsewhere?
- Can two steering directions be made to compete while both remain active?
- Does repeated steering across generation steps produce drift, hysteresis, or attractors?
- Can a deliberately bad or unstable steering direction become a reusable creative control?

### Existing AI SLOP connections
- audio/Suno contradiction experiments;
- latent-control trajectory ideas;
- separated jurisdictions;
- alien utility / synthetic valence as selection layers;
- experimental-method requirement to separate creative utility from mechanism confidence.

### Status
**High-priority implementation lead. Not a new canonical operator yet.**

---

## Shift 2 - Sparse feature editing becomes actual concept surgery in video

### Source lead
**EraseSAE** (arXiv 2609.03629; ledger identifies ECCV 2026)

Ledger summary:
- sparse-autoencoder-based concept erasure in text-to-video diffusion transformers;
- partitioned convolutional SAE;
- contrastive attribution;
- timestep-resolved spatiotemporal masks;
- monosemantic-feature-level intervention;
- ledger specifically flags the possibility of inverting erasure into amplification.

### What changes for AI SLOP
Our older language around "concept collision" and "feature entanglement" was mostly inferred from model behavior or literature. EraseSAE suggests a much more surgical experiment: identify a sparse feature or feature set, then intervene over specific timesteps and regions.

The most interesting AI SLOP question is not erasure. It is **overexpression, grafting, and selective mis-timing**.

### Candidate research direction
**SAE Concept Surgery / Concept Grafting**

Possible experimental axes:
- erase vs amplify the same feature;
- amplify only early, middle, or late denoising timesteps;
- spatially restrict the feature to regions where it "should not" belong;
- transfer a feature between semantic contexts;
- combine two features whose ordinary co-occurrence is weak;
- alternate amplification and suppression over time;
- test whether the intervention creates stable semantic changes or only surface artifacts.

### Required controls
- matched perturbation norm;
- random sparse directions or random basis controls;
- target effect vs collateral damage;
- identity preservation vs concept strength;
- same intervention with the relevant feature absent.

### Existing AI SLOP connections
- feature entanglement;
- binding failure;
- separated jurisdictions;
- cross-modal manifold shear;
- earlier SAE random-baseline hygiene.

### Status
**Very high-value research lead. Keep separate from ordinary prompt-based "concept mixing."**

---

## Shift 3 - Style can be decomposed instead of treated as one giant aesthetic blob

### Source lead
**LouvreSAE** (arXiv 2512.18930)

Ledger summary:
- art-specific SAE on CLIP embeddings;
- "style profiles" as decomposable steering vectors;
- few-reference style steering without fine-tuning;
- interpretable concept sliders;
- code and Hugging Face models listed.

### What changes for AI SLOP
The interesting move is not "copy a style." It is **decompose a style into manipulable components and then violate the normal relationships among those components.**

### Candidate research direction
**Style-Profile Surgery**

Potential operations:
- remove one style component while holding the rest;
- overdrive one component until it stops behaving stylistically and starts behaving structurally;
- transplant components between unrelated style profiles;
- breed profiles by component inheritance rather than image blending;
- keep palette from one profile, material logic from another, composition bias from another;
- test whether a style component can become a literal material or geometry constraint.

### Existing AI SLOP connections
- property unbundling / ownership transfer;
- destructive compression + substrate transference;
- operator breeding;
- math-face material anchoring;
- aesthetic conservation.

### Status
**Strong candidate adapter / operator family seed. Do not canonize until tested.**

---

## Shift 4 - Video drift may be a controllable variable instead of only a defect

### Source lead
**What Matters in Clean-Context Autoregressive Video Diffusion** (ledger identifies ICML 2026 F2S workshop, Wei & Zhou)

Ledger summary:
- autoregressive video drift is backbone-dependent;
- drift linked to cross-frame information leakage through temporal normalization;
- leakage can be added or removed;
- follow-up seeds: Context Forcing, Self Gradient Forcing, Diagonal Forcing.

### What changes for AI SLOP
This is a major conceptual upgrade. We have treated temporal drift as a failure surface to harvest. If the ledger is right that a structural leakage mechanism can be manipulated, then **drift becomes a parameter that may be swept deliberately.**

### Candidate research direction
**Controlled Temporal Leakage / Drift Knob**

Questions:
- At what leakage strength does identity begin to migrate?
- Which feature class drifts first: material, topology, object identity, pose, lighting, or background?
- Does drift accumulate smoothly, jump between basins, or enter cycles?
- Can leakage be pulsed rather than held constant?
- What happens when a reference anchor is held fixed while leakage pressure increases?
- Does a later "repair" step erase drift or fossilize it?

### Controls
- no-leak baseline;
- matched generation length;
- backbone-specific comparison;
- freeze-vs-real-consistency control;
- track identity, motion, topology, and material separately.

### Existing AI SLOP connections
- temporal correspondence failure;
- semantic drift;
- object permanence failure;
- artifact fossils / scars;
- external-state controllers;
- iterative transformation.

### Status
**Potentially one of the most important video findings in this cycle.**

---

## Shift 5 - Evolutionary search gets an adversarial archive pressure model

### Source leads
**Digital Red Queen** (arXiv 2601.03335) + **DEI** (arXiv 2605.27130)

Ledger summary:
- LLM used as mutation operator inside MAP-Elites;
- adversarial Core War coevolution;
- distributed heterogeneous-LLM variant;
- convergent evolution observations;
- champion-sharing protocol.

Related lead:
**PBT-NCA** (arXiv 2604.11248)
- population-based training of Petri Dish NCA;
- novelty archive + DINOv2 visual diversity;
- open-ended discovery without a fixed target;
- quality-diversity plus foundation-model scoring.

### What changes for AI SLOP
This strongly reinforces the repository's existing move away from "one best output." The better frame is a **population of weird solutions occupying different behavioral niches, under pressure to keep producing new viable descendants.**

This is very close to the breeding / archive machinery already being developed elsewhere in the project, but this cycle adds concrete research ancestry for adversarial archive pressure and open-endedness.

### Candidate research direction
**Adversarial QD Archive Pressure**

Preserve these ideas for later synthesis:
- MAP-Elites-style archive cells based on behavior, not just appearance;
- mutation operator can itself be an LLM or Temporary Mind;
- champions can be shared across populations;
- archive pressure can reward novelty without collapsing into random noise;
- convergence is itself data: record repeated rediscovery of structures;
- use multiple model families as heterogeneous mutation ecologies.

### Existing AI SLOP connections
- Operator Ecology Workbench concept;
- descendant fitness;
- meta-genomic speciation;
- archive behavior descriptors;
- conceptual allergy / operator burnout;
- breeding system in Mr. Slop.

### Status
**Strong architecture evidence. Hold for cross-project synthesis after more cycles.**

---

## Shift 6 - Flow-model editing needs different intervention logic

### Source leads
**UniEdit-Flow** (ICLR 2026) + **FlowAlign** (ICLR 2026)

Ledger summary:
- predictor-corrector inversion for flow models;
- trajectory-regularized inversion-free editing;
- delayed injection;
- theory for why diffusion-era editing methods break on flow models;
- reverse-editing capability.

### What changes for AI SLOP
A lot of our conceptual editing language assumes diffusion-style behavior. Flow-model editing creates a different failure surface and, more interestingly, **delayed injection lets us introduce a conflicting condition after some structure has already committed.**

That is practically a native implementation of structured instability: build a container first, then force an incompatible rule into the partially committed trajectory.

### Candidate research direction
**Delayed-Injection Conflict / Trajectory Vandalism**

Potential sweeps:
- injection time;
- conflict strength;
- which attribute is allowed to commit before intervention;
- single injection vs repeated pulses;
- reverse edit after mutation;
- whether the result returns, scars, or enters a new basin.

### Existing AI SLOP connections
- causing structured instability;
- reference anchoring;
- three-axis stabilization;
- semantic recoil;
- hysteretic transformation;
- stateful scars.

### Status
**High-value cross-media technical lead.**

---

## Secondary but important findings

### MetaNCA - developmental weight generation
Ledger summary:
- graph neural cellular automaton local rule self-organizes weights of arbitrary neural architectures;
- "Weight Transformer";
- developmental attractor over weight space;
- architecture-agnostic;
- reported 16x compression.

Why it matters:
This is not a near-term AI SLOP operator. It is a research bridge toward **Temporary Minds as developmental processes rather than static instruction packets**. The provocative future question is whether a controller can grow, repair, or mutate another controller's weights or parameters under local rules.

Status: **deep research / future substrate**, not current build.

### Collision-based logic in Lenia - composition boundaries
Ledger summary:
- INHIBIT gate from Orbium glider collisions;
- negative results around delivery / absorber requirements;
- phase fragility maps;
- glider-collision operator primitives.

Why it matters:
The negative result is the useful part. AI SLOP needs more explicit records of **which operators refuse to compose** and why. A composition boundary can be as informative as a successful combination.

Status: **experimental design influence**.

### Spore.fun + ALife-in-the-Wild - deployed agent divergence
Ledger summary:
- open-environment agent evolution;
- cultural speciation of clones;
- memory poisoning;
- judge-shaped fitness;
- field methods for deployed agents.

Why it matters:
This is more about longitudinal observation than generation. It may provide empirical vocabulary for Temporary Mind divergence, model ecology, external-state effects, and selection pressures.

Status: **field-method / provenance support**, not a generator.

---

## Active frontiers to keep searching

Retain the ledger's frontier list, with AI SLOP routing:

1. **Audio diffusion functional-layer steering** -> direct technical counterpart to Suno/audio slop.
2. **Monosemantic video concept surgery** -> test amplification/insertion, not only erasure.
3. **Clean-context drift as controllable operator** -> explicit temporal leakage sweeps.
4. **LLM-driven adversarial QD archives** -> breeding + archive pressure.
5. **NCA-as-weight-generator** -> developmental Temporary Mind substrates.
6. **ALife-in-the-wild field methods** -> clone divergence and selection pressure.
7. **Flow-model trajectory manipulation** -> delayed injection and reverse editing.

---

## Searches to stop wasting time on

Carry forward the ledger's low-yield list:

- generic "10 AI art repos" listicles;
- generic temporal-drift production blogs with no mechanism;
- generic 2026 SAE-steering searches dominated by LLM alignment - use modality-qualified searches;
- "differentiable reaction diffusion 2026" unless a new lead appears.

Also keep the existing project rule: do not promote a new label simply because a paper, repo, or metaphor gives us a fresh noun.

---

## Vocabulary worth preserving as search seeds

- functional layer
- style profile
- partitioned convolutional sparse autoencoder
- timestep-resolved spatiotemporal mask
- contrastive attribution
- clean-context training
- cache-writing gap
- delayed injection
- trajectory regularization
- reverse editing
- Digital Red Queen
- cultural speciation
- memory poisoning
- judge-shaped fitness landscape
- Weight Transformer
- Petri Dish NCA
- composition boundary
- petri-dish open-endedness
- Recursive Feature Machines steering

---

## Labs / author orbits worth watching

From the ledger:

- Sakana AI - Digital Red Queen, Petri Dish NCA, ASAL lineage;
- Inria Flowers - Flow-Lenia ecosystem;
- Bert Wang-Chak Chan - Lenia lineage;
- Warsaw UT / IDEAS - audio interpretability;
- HiDream-ai - video SAE tooling;
- KAIST / Jong Chul Ye lab - FlowAlign;
- Maneesh Agrawala group - LouvreSAE;
- Jeff Clune / Jakob Foerster orbits - open-endedness / Hyperagents;
- Marvin Tong / Phala - Spore.fun;
- Mura ALife Labs, openLife, Alternative Machine Inc. - wild-ALife practice.

---

## Open questions from this cycle

Keep these unresolved instead of hand-waving answers:

1. Does EraseSAE-style masking work for **concept insertion or amplification**?
2. Does a clean-context leakage control transfer to **Wan2.1, CogVideoX, or other video backbones**?
3. Can Digital Red Queen-style archives operate on **images, prompts, music, or other non-code substrates**?
4. Can style profiles be bred or transplanted while preserving interpretable ancestry?
5. Can TADA-like audio steering create controlled **conflicts between functional layers** rather than a single scalar steering direction?
6. Does delayed injection create a **recoverable edit, a persistent scar, or a new attractor**?
7. Can MetaNCA-like developmental rules become a substrate for Temporary Mind evolution without turning the metaphor into a false claim about hosted models?
8. Which AI SLOP operators have genuine **composition boundaries** rather than merely poor prompt compatibility?

---

## Integration rule for now

For the next few scouting cycles:

- **collect first;**
- map each finding to existing AI SLOP machinery;
- record possible combinations;
- avoid implementing a large new system yet;
- promote only after repeated cycles reveal clusters that genuinely reinforce each other.

The next synthesis pass should look for **convergence across cycles**, not whichever paper has the coolest noun.
