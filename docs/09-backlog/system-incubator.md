# AI SLOP System Incubator
## Persistent queue for good shit we have **not** turned into systems yet

This file is the holding pen for ideas, experiments, partial builds, and research clusters that are worth keeping but are **not yet canonical systems**.

Use this instead of relying on memory or scattered conversations.

## Status vocabulary

- **ACTIVE** — being worked on now.
- **NEXT-WORK-SESSION** — ready to continue when Merry has the bandwidth.
- **RESEARCH-ACCUMULATING** — deliberately waiting for more scouting cycles before synthesis.
- **DEFERRED-BY-DESIGN** — intentionally blocked behind cheaper / simpler / prerequisite work.
- **PARKED** — worth keeping, not currently scheduled.
- **NEEDS-STATUS-REFRESH** — last-known state may be stale; inspect the relevant repo/thread before resuming.
- **GRADUATED** — became a real system / canonical mechanism and should be moved out of this file.

## Tracking rule

Whenever Merry says any version of:
- "not today,"
- "next week,"
- "save that,"
- "we'll come back to it,"
- "don't build it yet,"
- "keep researching first,"
- "I'm already having you work on this,"
- or otherwise parks an unfinished AI SLOP idea,

add or update an entry here with:
1. current status,
2. last known state,
3. why it is not being built right now,
4. exact next move,
5. where its source material lives,
6. what other incubator items it may combine with.

Do **not** silently promote an incubator item into a canonical system.

---

# CURRENT BOARD

## RESEARCH-ACCUMULATING — Living research cycles before next systems pass

**State:** ACTIVE / intentionally not building.

**What exists now:**
- 2026-09-19 scouting integration;
- Living Ledger Cycle 1 integration;
- 2026-09-19 full primary-source intake (F01-F10);
- candidate mechanism queues;
- combination watchlist;
- research intake index.

**Current rule:** keep collecting several more Perplexity/research cycles, compare them, and look for repeated structural convergence before designing the next major systems.

**Next move:** each new cycle gets harvested into notes, candidate deltas, and combination signals. No large build until Merry says synthesis time.

**Files:**
- `docs/08-reference/research-intake-index.md`
- `docs/08-reference/research-scouting-2026-09-19-notes.md`
- `docs/08-reference/research-cycle-2026-09-20-integration.md`
- `docs/08-reference/research-cycle-2026-09-19-full-primary-source-intake.md`
- `docs/09-backlog/candidate-mechanisms-2026-09-20.md`
- `docs/09-backlog/candidate-mechanisms-2026-09-19-full-intake.md`
- `docs/09-backlog/research-combination-watchlist-2026-09-20.md`

---

## ACTIVE — Perceptual Wound -> Silent Scar -> Behavior Archive

**State:** first two implementation slices now exist; not yet a finished system.

**What was built on 2026-09-20:**
- `experiments/perceptual_wound/run_lenia_occlusion.py` — four matched conditions on the public `jessescool/lenia-umwelt` substrate: no mask, physical state erasure, unnormalized sensory occlusion, and normalized sensory occlusion;
- `experiments/perceptual_wound/run_silent_scar.py` — matched history-dependence assay: transient sensory wound -> visible recovery -> standardized second injury, compared against an unwounded route at the same elapsed time;
- `experiments/perceptual_wound/README.md` — protocol, measurements, provenance, and run instructions for both stages;
- `.github/workflows/perceptual-wound-smoke.yml` — CPU smoke test that clones the source substrate rather than vendoring it and executes both harnesses.

**Why it matters:** this remains the strongest integrated build path from the 2026-09-19 research cycle, and the full primary-source intake strengthened it substantially with Self-Organising Digital Circuits, Cells2Pixels, and moving-neighborhood causal tests.

**Sequence:**
1. **IMPLEMENTED v0.1:** perception-only injury / Lenia sensory occlusion harness;
2. **IMPLEMENTED v0.1:** visible recovery + standardized Functional Scar / Second-Injury assay;
3. **NEXT:** split recovery reporting into appearance, state, function, and interaction/trajectory behavior where the substrate exposes those dimensions;
4. add Cells2Pixels skin-vs-state controls;
5. add movement/state-rule swap tests when NPA is available;
6. behavior-sensitive archive descriptors;
7. archive the artifact by intervention response, not appearance alone.

**Current epistemic status:** PROCEDURAL / HYPOTHESIS. Both harnesses are runnable and their GitHub smoke test passes; a functional-scar claim still requires repeated matched runs, dose sweeps, and recorded failures. One divergent trajectory is not promoted to "memory."

**Next move:** run a proper repeated/dose matrix for the second-injury assay and add the multidimensional recovery report. Only after that should this feed the behavior archive.

**Combines with:** controlled temporal leakage, delayed-injection conflict, external-state controllers, AutoQD/QD archive work.

---

## GRADUATED — Semantic Fossil Instrument

**State:** v0.2 implemented, documented, tested, and routed into the canonical architecture layer on 2026-09-20.

**What exists:**
- persistent active state plus a separate causal fossil ledger;
- immutable route/audit ancestry;
- checkpoints;
- state-only restore that preserves scars;
- full restore/reset ablation that removes causal scars;
- history-sensitive transform predicates;
- route/checkpoint comparison;
- deterministic replay and anchor validation;
- text/JSON/Markdown/CSV renderers;
- route archive;
- minimum machine-readable run record and schema;
- Semantic Fossil Choir reproduction;
- causal-scar demonstration where identical pre-C active state diverges only when preserved B history is allowed to affect C;
- GitHub smoke/unit tests;
- provider-neutral transform adapter layer;
- Suno + visual renderer/compiler plugins;
- provider-neutral transform request packets;
- artifact ingestion with hashes/descriptors;
- artifact-aware fossil overlays that later compilers can inherit.

**Canonical home:** `docs/05-architectures/semantic-fossil-instrument.md`

**Implementation:** `experiments/semantic_fossil/`

**Why graduated:** the incubator graduation rule allows a built system to leave once implementation and canonical documentation exist. This does **not** promote every fossil/history causal interpretation to a native-model mechanism; the implementation is explicitly external and PROCEDURAL.

**Possible extensions:** direct provider-specific adapter packages, shader renderer plugin, behavior-sensitive intervention descriptors, fossil decay/inheritance policies, route-family dose sweeps, and integration with Silent Scar / Semantic Manifold routes.

---

## PARKED — Grammar Injury and Recovery

**State:** proposed experiment, untested.

**Core question:** what changes when a load-bearing grammatical / representational primitive is removed, explicitly re-enforced, or partially restored?

**Next move:** compare primitive removal, explicit grammar enforcement, and partial restoration under matched tasks and repeated runs.

**Combines with:** Primitive Deletion, cognitive lesions, Semantic Fossil Instrument.

---

## DEFERRED-BY-DESIGN — Reversible Activation-Axis Study

**State:** technically demanding experiment; intentionally after cheaper external-controller studies.

**Core comparison:** prompt-only vs activation-only vs combined vs sham conditions using held-out prompts.

**Why deferred:** do the inexpensive, auditable external-state work first.

**Next move:** only resume once the simpler controller/scar experiments are working.

**Combines with:** TADA/audio steering, SAE concept surgery, representation-level intervention work.

---

## NEEDS-STATUS-REFRESH — DAVID unresolved implementation queue

**State:** long-running project with multiple previously specified but not fully resolved jobs.

**Last-known unresolved items include:**
- internal state/data-contract cleanup;
- Part Ten self-evaluation / test harness;
- model-specific organism/profile work;
- experiment memory / empirical learning;
- sibling-generation quality-diversity selection (Job 8);
- one-writer audit / UX cleanup / violent QA;
- parked Tongues idea after core cleanup.

**Important:** this list is historical. Inspect the DAVID repo/current thread before resuming and update this entry rather than assuming every item is still unfinished.

**Next move:** refresh against current repo state, then select one concrete job.

---

## NEEDS-STATUS-REFRESH — Mr. Slop ongoing rounds

**State:** active multi-round system with breeding/stateful mutation work; exact current point may have moved.

**Last-known unresolved states:**
- Round 1 cleanup / artifact-save plumbing;
- Round 2A conversational mutation action contract;
- later UI/undo/provenance cleanup;
- breeding/SRE work follows only after mutation substrate is solid.

**Next move:** inspect current `mrslop` main and resume from the latest merged job, not this stale note.

---

## PARKED — TOPOS-SRE follow-up

**State:** core UI/token-economics surgery was completed; one later experiment remained interesting.

**Parked experiment:** make local NGL behavior less vocabulary-bound.

**Next move:** only reopen after current higher-priority AI SLOP builds.

---

## PARKED — Temporary Minds second-wave items

**State:** not first-generation priorities.

**Known parked/reconstruction items:**
- Observational Crystallization / Attentional Collapse — build later;
- Semantic Recoil / Interpreter Mutation — reconstruction required;
- Epistemic Succession — merge/consolidation pile;
- broader untouched territories such as social cognition, formal-math cognition, humor, alien beauty, transformed completion, uncertainty, self-model, scale, and irreducible value conflict.

**Next move:** revisit only after first-generation Temporary Minds and current experimental machinery have actual test results.

---

# CYCLE 1 CANDIDATE CLUSTER — DO NOT BUILD YET

These are tracked in detail elsewhere and stay here only as a reminder that they are waiting for cross-cycle convergence:

- Audio Functional-Layer Steering
- SAE Concept Surgery / Concept Grafting
- Style-Profile Surgery
- Controlled Temporal Leakage
- Adversarial QD Archive Pressure
- Delayed-Injection Conflict
- Developmental Weight Ecology
- Composition Boundary Mapping
- Cultural Speciation / Judge-Shaped Fitness

See:
- `docs/09-backlog/candidate-mechanisms-2026-09-20.md`
- `docs/09-backlog/research-combination-watchlist-2026-09-20.md`

---


# FULL PRIMARY-SOURCE INTAKE CLUSTER - DO NOT CANONIZE YET

The 2026-09-19 full primary-source cycle retained ten operational records but promoted zero operators.

Tracked candidates:

- Mutable Sequence Scaffold / Edit-Debt Ledger
- Functional Scar / Second-Injury Assay
- Cultural Annealing Regulator
- Developmental Connectivity
- Skin-State Dissociation
- Moving-Neighborhood Causal Rewiring
- Moving Edit Jurisdiction
- Steering Donor Provenance Contract
- Semantic Fault Atlas
- Non-Normal Flare-and-Return Kernel

**Highest priority later work:** Functional Scar / Second-Injury Assay.

**Deferred local/open-weight bundle:** Edit Flows/LLaDA runtime trace audit, activation donor-provenance study, video numerical fault atlas, and non-normal controller prototype. These require more local runtime/model access than the cheap external-state experiments.

See:
- `docs/08-reference/research-cycle-2026-09-19-full-primary-source-intake.md`
- `docs/09-backlog/candidate-mechanisms-2026-09-19-full-intake.md`
- `docs/09-backlog/research-combination-watchlist-2026-09-20.md`

---


# CLOSED-LOOP / INSTABILITY INTAKE CLUSTER — DO NOT CANONIZE YET

The 2026-09-20 Perplexity cycle added several genuinely new backlog mechanisms and method upgrades.

Tracked candidates:

- Sparse Autotelic Perturbation
- Intervention Debt
- Instability-Gated Intervention
- Trajectory Fossil
- Evolvable Jurisdiction Stack
- Repair–Corruption Frontier
- Symbiotic Fitness
- Localized Law Carriage (implementation/substrate only; merge with existing operators)

**Strongest structural signal:** interventions should increasingly become **conditional on the evolving state** rather than always-on or globally scheduled.

**High-value later prototypes:**
1. Anti-SkipInv / instability-gated inversion harness;
2. CARL-style costed controller on Lenia/Flow-Lenia;
3. executable local/global/decision jurisdiction prototype;
4. relationship-level breeding test for Symbiotic Fitness.

**Why not now:** the project is still intentionally accumulating research cycles before another synthesis/build phase. Preserve the mechanisms and method changes; do not promote canonical operators yet.

See:
- `docs/08-reference/research-cycle-2026-09-20-closed-loop-instability-intake.md`
- `docs/09-backlog/candidate-mechanisms-2026-09-20-closed-loop-instability.md`
- `docs/09-backlog/research-combination-watchlist-2026-09-20.md`

---


# WRONG-USE / STABILIZER INVERSION CLUSTER — DO NOT CANONIZE YET

The 2026-09-20 Kimi scout mined stabilization, reliability, interpretability, codec, video, steering, and model-merging research by reading the fixes backwards.

**Canonical method:** `docs/06-experimentation/stabilizer-inversion-wrong-use-research.md`

**Tracked candidate families:**

- Cyclic Denoising Attractor Atlas
- Attention Sink Amputation / Parking-Lot Occupation
- Guidance-Frequency Jurisdictions
- Error Accumulation as Video Medium
- Scheduled Vocabulary Mutation / Dead-Code Injection
- Induction-Head Lesion / Positional Arbitration Phase Shift
- Semantic-Entropy Breeding
- Steering-Vector Stack Frontier
- Loss-Barrier Merging

**Build priority from the scout:**
1. cyclic denoising atlas;
2. sink amputation / occupation;
3. dead-code injection + codec-level split-brain;
4. guidance-frequency jurisdictions;
5. semantic-entropy breeding;
6. video anchor inversion after the cheaper work is producing.

**Why not canonical yet:** strong source support exists for the underlying failures/fixes, but most AI SLOP inversions are still hypotheses. Run the normal baseline/repeat/dose/ablation protocol first.

**Files:**
- `docs/08-reference/research-cycle-2026-09-20-wrong-use-scout.md`
- `docs/09-backlog/candidate-mechanisms-2026-09-20-wrong-use-scout.md`
- `docs/06-experimentation/stabilizer-inversion-wrong-use-research.md`

---

# HOW ITEMS LEAVE THIS FILE

An item graduates only when one of these happens:

1. **Built system:** implementation exists and has its own canonical docs.
2. **Canonical operator:** mechanism is operationally distinct, tested enough to deserve registry status.
3. **Merged:** it turns out to be an adapter, validator, implementation, or composition of existing machinery.
4. **Rejected:** evidence says it is redundant, untestable, useless, or based on a bad explanation.
5. **Archived:** interesting historical material, but no longer worth active work.

When an item leaves, keep a one-line tombstone here or in the research intake index so we can still see what happened to it.
