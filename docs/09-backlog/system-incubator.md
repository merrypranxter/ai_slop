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

**State:** first implementation slice now exists; not yet a finished system.

**What was built on 2026-09-20:**
- `experiments/perceptual_wound/run_lenia_occlusion.py` — four matched conditions on the public `jessescool/lenia-umwelt` substrate: no mask, physical state erasure, unnormalized sensory occlusion, and normalized sensory occlusion;
- `experiments/perceptual_wound/README.md` — protocol, measurements, provenance, and run instructions;
- `.github/workflows/perceptual-wound-smoke.yml` — CPU smoke test that clones the source substrate rather than vendoring it.

**Why it matters:** this remains the strongest integrated build path from the 2026-09-19 research cycle, and the full primary-source intake strengthened it substantially with Self-Organising Digital Circuits, Cells2Pixels, and moving-neighborhood causal tests.

**Sequence:**
1. **IMPLEMENTED v0.1:** perception-only injury / Lenia sensory occlusion harness;
2. **NEXT:** visible recovery plus hidden-state / second-injury scar assay;
3. split recovery into appearance, internal state, function, and interaction graph;
4. add Cells2Pixels skin-vs-state controls;
5. add movement/state-rule swap tests when NPA is available;
6. behavior-sensitive archive descriptors;
7. archive the artifact by intervention response, not appearance alone.

**Current epistemic status:** PROCEDURAL / HYPOTHESIS. The harness makes the comparison runnable; source-paper reproduction and AI SLOP claims still require matched runs and recorded failures.

**Next move:** run and stabilize the v0.1 four-condition assay, then build the standardized Functional Scar / Second-Injury Assay on visibly recovered states.

**Combines with:** controlled temporal leakage, delayed-injection conflict, external-state controllers, AutoQD/QD archive work.

---

## NEXT-WORK-SESSION — Semantic Fossil Instrument

**State:** recommended integrated build; not yet inserted as a finished system.

**Last known concept:** persistent state + multiple renderers + route comparison + validator + archive, with transformation order leaving reproducible scars.

**Why not now:** intentionally held behind current research accumulation.

**Next move:** build the instrument and minimum run-record schema; preserve route ancestry and reset/ablation behavior.

**Combines with:** Silent Scar, hysteretic transformation, artifact fossilization, language-history experiments.

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

# HOW ITEMS LEAVE THIS FILE

An item graduates only when one of these happens:

1. **Built system:** implementation exists and has its own canonical docs.
2. **Canonical operator:** mechanism is operationally distinct, tested enough to deserve registry status.
3. **Merged:** it turns out to be an adapter, validator, implementation, or composition of existing machinery.
4. **Rejected:** evidence says it is redundant, untestable, useless, or based on a bad explanation.
5. **Archived:** interesting historical material, but no longer worth active work.

When an item leaves, keep a one-line tombstone here or in the research intake index so we can still see what happened to it.
