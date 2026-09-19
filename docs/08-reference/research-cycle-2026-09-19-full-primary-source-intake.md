# AI SLOP Research Integration Notes
## Full primary-source intake - 2026-09-19

**Repository baseline inspected by the research cycle:** commit `974039cb1ee93aa8992d6085915c17fdccebb783`.

**Status:** research intake and implementation mapping only. This cycle retained ten high-value findings/finding families and deliberately promoted **zero** immediate additions to the canonical operator registry.

**Why:** the main gain is not ten more names. It is a set of substrates, controls, adapters, and tests that can make existing AI SLOP ideas less metaphorical and more executable.

**Evidence rule:** evidence confidence applies only to the bounded technical claim actually demonstrated in the cited source. Creative utility is tracked separately. No training runs, benchmark reproductions, or independent replications were performed in this intake.

---

# Executive delta

This cycle adds nine practical distinctions the existing system can now test more cleanly:

1. **Mutable scaffold:** distinguish actual insert/delete/substitute events from prose that merely claims revision.
2. **Repair has multiple invariants:** appearance recovery, hidden-state recovery, functional recovery, and interaction-graph recovery are not interchangeable.
3. **Plasticity can have a lifecycle:** young/old agents can receive different permissions to change.
4. **Connectivity itself can develop:** compare grown topology, generated weights, and moving neighborhoods rather than treating all adaptation as weight change.
5. **Skin can be separated from organism state:** a changed renderer is not automatically a changed underlying system.
6. **Edit jurisdiction can move:** the editable region can follow predicted discrepancy rather than stay a fixed mask.
7. **Steering vectors need provenance:** donor context, token boundary, layer, pooling, subtraction baseline, and strength belong in the record.
8. **Semantic damage can hide behind clean pixels:** perceptual quality and meaning must be scored separately.
9. **Stable systems can flare violently:** peak finite-time excursion and eventual return are separate objectives.

---

# F01 - Edit Flows + LLaDA2.2: mutate the sequence scaffold

**Source/version:** Havasi, Karrer, Gat, and Chen, *Edit Flows*, arXiv v3 (2025-11-12), paired with the currently available InclusionAI LLaDA2.2-mini ecosystem. The two are related edit-based approaches; do not claim LLaDA implements Edit Flows unchanged.

**What is demonstrated**
- Edit Flows uses variable-length sequence dynamics with insertion, deletion, and substitution.
- LLaDA2.2 documents INSERT and DELETE control tokens during diffusion decoding.
- The controllable surfaces differ across the paper and model interface and should remain separate in any adapter.

**Important limitations**
- Reported code/caption scores do not establish general superiority over autoregression.
- LLaDA warns that lower thresholds can cause repetitive or unstable output.
- Aggregate benchmark gain is not uniform capability gain.
- Neither source establishes Semantic Recoil as a discovered internal mechanism.

**AI SLOP mapping**
- Primitive Deletion
- Recall Mutation
- Semantic Recoil
- external-state / edit-history ledgers

**Recipe worth preserving**
**Edit-debt ledger:** record every insertion/deletion/substitution event and what later material must be removed, reinterpreted, or structurally repaid because of it.

**Implementation gate**
- Official mini weights exist but total parameter footprint is larger than the active-per-token number suggests.
- Minnow quantization changes runtime/numerics and does not yet certify insertion/deletion parity.
- Akicou exposes a Levenshtein-editing toggle, but exact upstream operation parity remains unverified.

**Next test**
Trace actual edit events in InclusionAI runtime, compare with substitution-only behavior and Akicou's editing toggle, then inspect OneFlow/mixed-modal continuation work.

---

# F02 - Self-Organising Digital Circuits: recover the function, not the body

**Source/version:** Barylli, Bena, Mordvintsev, Nisioti, and Risi; arXiv v2 (2026-08-14), ALIFE 2026 material, experimental `gabi` branch.

**What is demonstrated**
- A topology-masked recurrent transformer updates local logic/memory on a fixed wiring graph.
- Simulated circuits can recover Boolean function after damage while arriving at multiple functionally equivalent internal configurations.
- Reported tasks include bit reversal, addition, and multiplication.

**Important limitations**
- The reported repair does not grow new wires.
- Random-topology arithmetic does not become exact.
- Size-transfer remains limited.
- This is not a demonstrated physical self-healing chip.
- Message-step and gradient-step comparisons are not compute-matched speed claims.

**AI SLOP mapping**
- Silent Scar
- Return Contract
- Hysteretic Transformation / Artifact Fossilization
- behavior-sensitive archives

**Recipe worth preserving**
**Functional scar assay:** accept "repair" only when the target function returns; then separately compare:
1. outward appearance,
2. internal organization/state,
3. computation/function,
4. response to the same second injury.

Equivalent output does not imply equivalent history.

**Implementation gate**
- MIT JAX/Flax code, checkpoints, browser inference, and figure materials exist.
- `gabi` is the branch to audit; the README documents a Regime II recovery/UMAP reproduction gap and older material in `mergello`.
- Browser demo uses curated wiring pools and implementation changes; do not treat it as an unbiased replay of every paper result.

**Next test**
Reconcile `gabi` commit `9f3592a35f3d0a7b9f88dc185d388782a1b4062f` with `mergello` and archived figure scripts, then run the standardized second-injury assay.

---

# F03 - Aging-game: age the learning rule, not merely the character

**Source/version:** Dziewonski, Plaza-del-Arco, and Verhoef; CoNLL 2026, official EGG-based implementation.

**What is demonstrated**
- Populations undergo turnover.
- Learning rate and Gumbel-Softmax temperature change with agent age.
- In the reported small referential game, age-structured plasticity improves cross-generation communication while within-generation performance remains similar.

**Important limitations**
- Main comparisons use only a small number of seeds.
- Learning-rate-only modulation can destabilize the population.
- All-child and all-adult controls reveal different teaching/stability failures.
- This does not establish a universal law for LLMs, humans, or open-ended semantic cultures.

**AI SLOP mapping**
- GlossoGen
- Meta-Genomic Speciation
- Cliche Mortality / Operator Burnout
- cultural speciation

**Recipe worth preserving**
**Cultural annealing regulator:** give newer agents more mutation/plasticity permission and older agents more convention-stabilizing responsibility; require turnover rather than one immortal population.

**Implementation gate**
MIT code exposes age normalization, sigmoid/linear plasticity schedules, turnover grids, and temperature-only / learning-rate-only controls. README defaults should not be conflated with selected paper settings.

**Next test**
Run matched turnover/population-size grids, then test an external-controller analogue against static-budget and random-turnover controls. Keep literal optimizer plasticity separate from controller-level mutability.

---

# F04 - Developmental Graph Cellular Automata: grow the computation graph

**Source/version:** Barandiaran and Stovold, accepted manuscript *Growing Echo State Networks through Graph-Based Morphogenesis with Developmental Graph Cellular Automata*; manuscript carries 2026-07-29 submission information.

**What is demonstrated**
- Local developmental rules control cell division, removal, persistence, and connectivity.
- Grown reservoirs are evaluated on NARMA tasks.
- Smaller grown reservoirs can outperform larger random comparators.
- Useful stochastic reservoirs can be acyclic, challenging the assumption that good reservoirs must be richly recurrent.

**Important limitations**
- Proxy dynamical descriptors are weaker optimization targets than task fitness.
- Spectral-radius intuition does not reliably identify the best evolved solutions.
- No lifelong autonomous graph growth, repair, or general reasoning is demonstrated.

**AI SLOP mapping**
- developmental Temporary Mind substrates
- Descendant Fitness
- developmental weight / topology work
- future controller ecology

**Recipe worth preserving**
**Developmental jurisdiction:** grow the routes through which a controller can remember/respond, not just the values carried on a fixed route.

**Implementation gate**
The linked MIT repository identifies itself as the ALIFE 2025 implementation and depends on graph-tool. A coauthor fork contains packaging/algorithm changes, but exact correspondence to the accepted manuscript is unverified.

**Next test**
Diff upstream vs coauthor fork, identify the code path matching the manuscript, then compare task-selected growth vs descriptor-selected growth under equal evaluation budgets.

---

# F05 - Cells2Pixels: separate organism dynamics from visible skin

**Source/version:** Pajouheshgar et al., *Neural Cellular Automata: From Cells to Pixels*, arXiv v3 (2026-05-01), SIGGRAPH 2026.

**What is demonstrated**
- A coarse evolving NCA state is rendered through a separate local implicit decoder.
- The same underlying state can be sampled/rendered at higher output resolution.
- Demonstrations span morphology, PBR maps, mesh textures, and volumetric textures.

**Important limitations**
- Primitive-aligned artifacts remain.
- PBR supervision is not final-render-aware.
- Noninteger expansion can settle on neighboring integer tile counts.
- Higher display resolution is not more independently evolving cells.
- Parameter-swap morphs are not optimized for predictable control.

**AI SLOP mapping**
- Property Unbundling
- Observer / Medium Coupling
- Silent Scar
- visible-state vs hidden-state experiments

**Recipe worth preserving**
**Skin-state dissociation:** independently intervene on:
- the evolving organism state;
- the visible decoder/renderer.

Then compare same skin/different state versus same state/different skin.

**Next test**
Pair with Silent Scar: equalize visible reconstruction while checking hidden-state and second-injury response; also test fixed state with altered decoder.

---

# F06 - Neural Particle Automata: movement rewrites who can communicate

**Source/version:** Pajouheshgar, Kim, Suesstrunk, Jakob, and Park; arXiv v2 (2026-06-23), SIGGRAPH 2026.

**What is demonstrated**
- Cells have continuous positions and internal states.
- Shared learned rules update both position and state.
- Spatial hashing/SPH perception creates moving neighborhoods.
- Mixed species can remain separate, cooperate, or disrupt one another.
- Regeneration is shown under several perturbations.

**Important limitations**
- Particles cannot split or merge.
- Rotational equivariance is not enforced.
- Removing gradient stopping or normalization destabilizes training.
- Vortex-like distributed-memory interpretations remain speculative.

**AI SLOP mapping**
- Cybernetic Circuit Closure
- Separated Jurisdictions
- interaction-graph scars
- moving-neighborhood ALife substrates

**Recipe worth preserving**
**Locomotion as communication rewiring:** movement changes neighborhood, neighborhood changes received messages, messages change movement.

**Next test**
Hold state rules fixed and swap movement rules; then hold movement fixed and swap state rules. Record interaction graphs and second-perturbation response instead of calling every persistent swirl "memory."

---

# F07 - RIDGE: make edit jurisdiction follow predicted damage

**Source/version:** Gong, Wang, Wang, and Chen; arXiv v1 (2026-08-04).

**What is demonstrated**
- In inversion-free flow editing, source and edited states are re-noised together.
- Guidance uses predicted clean state.
- A dynamic spatial mask follows estimated source/edit discrepancy.
- Ablations show a preservation/edit-strength tradeoff between mask and guidance components.

**Important limitations**
- Conservative preservation can resist large geometry changes.
- CLIP-style alignment and a small preference study do not prove exact semantic correctness.
- No verified public RIDGE implementation was established in this intake.

**AI SLOP mapping**
- Anchor + Mutation Field
- Separated Jurisdictions
- flow-model delayed injection
- moving boundary experiments

**Recipe worth preserving**
**Moving damage jurisdiction:** edit permission follows the predicted region of change rather than a permanent prompt boundary.

**Implementation gate**
Paper-specified, not install-ready.

**Next test**
Compare fixed mask, attention mask, and discrepancy-following mask at matched edit strength. Add intentional mask delay as a new AI SLOP experiment; do not attribute delayed-mask results to RIDGE.

---

# F08 - Activation source selection: harvest intention before verbal residue

**Source/version:** Ye et al., *Where Steering Signals Come From: Activation Source Selection in Activation Steering*, arXiv v2 (2026-08-28).

**What is demonstrated**
Keeping the downstream additive steering method fixed while changing:
- donor context,
- extraction position,
- pooling,
- subtraction baseline

can substantially change steering behavior. A reported aggregate comparison shows prompt-final extraction outperforming answer-only mean pooling in the tested setup.

**Important limitations**
- Results depend on layer/strength grid choices and limited model/task families.
- Multi-turn durability and multimodal transfer are not established.
- No verified code release was established in this intake.

**AI SLOP mapping**
- activation steering validation
- SAE/random-basis controls
- Reversible Activation-Axis Study
- representation-level intervention provenance

**Recipe worth preserving**
**Donor provenance contract:** every steering vector record must include donor prompt/context, token boundary/extraction position, tail, layer, pooling rule, subtraction baseline, and steering strength.

**Next test**
Cross donor-source choice with matched-norm/random-basis controls and report held-out results without choosing the best layer on the final test set.

---

# F09 - T2V-Resilience: numerical scars can change semantics without looking broken

**Source/version:** Coalson et al.; arXiv v1 (2026-08-30), ICML workshop material, MIT code.

**What is demonstrated**
- Simulated bit flips can be injected into diffusion-transformer weights or intermediate activations during video generation.
- Fault metadata is recorded and changed weights are restored between trials.
- In tested models, semantic correctness can degrade more than perceptual quality.
- High-order exponent bits are especially sensitive.
- No simple universal "early = meaning / late = texture" timing law was supported.

**Important limitations**
- Many faults are catastrophic or boring.
- Weight and activation fault conditions are not inherently dose-matched.
- This is not a targeted semantic editor or proof about proprietary video systems.

**AI SLOP mapping**
- Error Axiomatization
- Causal Artifact Chain
- generator-specific error banks
- behavioral archives

**Recipe worth preserving**
**Semantic fault atlas:** archive each trial by:
- numerical fault type/location/dose,
- altered object/event/meaning,
- perceptual disruption,
- temporal persistence,
- model/seed/prompt.

**Implementation gate**
Public fault modules, generation scripts, VBench paths, and evaluation scripts were inspected; dependencies/model-memory still require an actual run check.

**Next test**
Equalize fault dose, preserve identical seeds, include no-fault replay and zero-effect injection controls, and compare semantic displacement independently from perceptual displacement.

---

# F10 - Non-normal transient amplification: flare violently while remaining stable

**Source/version:** Fruchart/Vitelli 2026 nonreciprocal-physics review led to Christodoulou, Vogels, and Agnes, *Regimes and mechanisms of transient amplification* (2022). This is intentionally older mathematics retained because it supplies a missing control kernel.

**What is demonstrated**
- Stable non-normal dynamics can produce large finite-time amplification before decay.
- Amplification regime depends on spectral/feedforward structure.
- Strong amplification can concentrate trajectories into a lower-dimensional subspace.
- Some linear high-frequency effects disappear in nonlinear models.

**Important limitations**
- Nonreciprocity and non-normality are not synonyms.
- Asymptotic stability does not bound transient excursion.
- The source does not demonstrate an AI-art controller.
- Do not call repeatable transient growth "chaos" or long decay "memory."

**AI SLOP mapping**
- Structured Instability
- Attractor Lock -> Perturb
- flare-and-return controllers

**Recipe worth preserving**
**Flare-and-return kernel:** independently tune:
- peak gain,
- excursion direction,
- return time,
- saturation,
- history dependence

while keeping the final attractor/stability condition separate.

**Implementation gate**
The primary study links simulation code. A minimal artistic controller can be built independently, but that adapter would be our proposal, not a reproduced paper result.

**Next test**
Measure peak gain, return time, saturation, and history dependence separately.

---

# Supporting updates from the same cycle

These did not justify new finding cards but should change how existing notes are read:

- **GNCA:** distributed-update evidence strengthens existing Silent Scar / recovery work.
- **BraiNCA:** adds task-dependent long-range-connectivity evidence.
- **SegTune:** adds evidence that musical quality and control strength can trade off.
- **Adapt:** limits any claim that conflict is intrinsically useful; pressure only matters when both conditions remain causally active and the system has a viable compensation path.
- **TextNCA:** adds inference-iteration distribution-shift failures; more iterations are not automatically "more reasoning" or better performance.

---

# Duplicate / merge decisions

Already-covered families should stay in their existing homes rather than be reintroduced as new mechanisms:

- MAP-Elites / quality-diversity / novelty-search families;
- Lenia occlusion;
- GlossoGen;
- TADA;
- MusicLayout;
- LatCH;
- Diff2Mix;
- EraseSAE;
- LouvreSAE;
- Stable Video Infinity;
- IDAttn;
- FlowAlign;
- UniEdit-Flow;
- MetaNCA;
- adversarial ALife/open-endedness work.

**Rejected overclaim:** topology conditioning is not yet a validated guarantee of topology correctness.

**Incomplete audits**
- iSAE full-paper audit was unfinished after HTML fetch failure.
- IAA and ATA remained landing-page leads only; no strong mechanism promotion.

---

# Low-yield search rules carried forward

Do not waste future cycles on vague forms of these queries unless a new author/release/technical term changes the expected yield:

- generic open-ended evolution without a missing descriptor/evaluator/causal control;
- generic "weird AI glitches" without fault type, module, dose, and measurement;
- bare "RIDGE" queries without flow editing + author/mechanism qualifiers;
- bare "TextNCA GitHub" assumptions;
- SAE interpretability headlines without assumptions, seed stability, counterexamples, and code;
- checkpoint ports by filename alone: quantization/conversion does not prove algorithm parity.

---

# Author / implementation graph worth watching

- Havasi / Chen -> Edit Flows -> OneFlow.
- InclusionAI -> Akicou / coder543 -> runtime editing parity.
- Bena / Barylli / collaborators -> `gabi` / `mergello` -> functional scars.
- Dziewonski / Plaza-del-Arco / Verhoef -> EGG -> aging-game.
- Barandiaran / Stovold -> coauthor fork -> grown reservoirs.
- Pajouheshgar / collaborators -> Cells2Pixels / NPA / NoiseNCA / Pandora.
- Ye et al. -> activation source selection -> donor provenance.
- Coalson et al. -> numerical faults -> semantic-fault atlas.
- Fruchart / Vitelli -> Christodoulou / Vogels / Agnes -> non-normal controller.

---

# Query seeds for the next cycle

- OneFlow edit flows mixed modal
- LLaDA2.2 insertion deletion ablation
- LLaDA2.2 Minnow editing parity
- boolean_nca_cc mergello recovery UMAP
- digital circuits functional degeneracy damage
- aging-game cross generation plasticity
- developmental graph automata NARMA topology
- alife_dgca reservoir stochastic development
- Neural Particle Automata multispecies failure
- NoiseNCA discretization seed instability
- Pandora stateful Particle Lenia memory
- Cells2Pixels transition hidden state
- RIDGE dynamic mask editing code
- activation source selection tail subtraction
- TextNCA iteration distribution failure
- video diffusion bit flip semantic
- non normal transient amplification saturation
- identifiable sparse autoencoders stability code

---

# Revisit rules

Reopen a paper-only intervention when an official implementation or author update appears.

Reopen model ports when the runtime claims the relevant editing operation, not merely after a new quantization upload.

Recheck Self-Organising Digital Circuits when Regime II reproduction gaps are resolved.

Recheck DGCA when authors identify the code corresponding to the accepted version.

Keep older mathematics alive when it supplies a missing control; publication age is not mechanism obsolescence.

---

# Repository disposition

**No canonical operator promotions from this cycle.**

The correct repository changes are:
- preserve the ten findings as an integration/reference record;
- add candidate recipes/contracts to backlog;
- add cross-cycle combinations to the watchlist;
- update the experimental method with new measurement contracts;
- mark the strongest next build in the system incubator.

**Priority next build when research accumulation pauses:** a functional-scar / second-injury experiment that distinguishes appearance, hidden state, function, and interaction-graph recovery before another broad novelty sweep.
