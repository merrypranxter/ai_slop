# AI SLOP Candidate Mechanisms Queue
## Full primary-source intake - 2026-09-19

**Rule:** these are recipes, contracts, adapters, validators, and substrate candidates from the full primary-source intake. They are **not canonical operators**.

The research cycle explicitly recommended zero immediate operator promotions. Keep these here until matched controls show that they add a distinct capability.

---

## C10. Mutable Sequence Scaffold / Edit-Debt Ledger

**Source family:** Edit Flows + LLaDA2.2 ecosystem.

**Core idea:** use a generator whose sequence can actually insert, delete, and substitute during sampling, then preserve the edit trace externally.

**AI SLOP use:** give Primitive Deletion / Recall Mutation / Semantic Recoil a mutable scaffold instead of asking an autoregressive model to imitate revision in prose.

**Minimum record:** operation type, location, step/time, inserted/deleted span, later reinterpretation/debt, final ancestry.

**Controls:** substitution-only; same prompt with editing disabled; final-output-only judging vs trace-aware judging.

**Gate:** runtime editing parity across official/ported implementations remains unresolved.

**Current class:** technical adapter + state ledger.

---

## C11. Functional Scar / Second-Injury Assay

**Source family:** Self-Organising Digital Circuits + Cells2Pixels; strengthens earlier Silent Scar work.

**Core idea:** recovery is not one variable. Score outward appearance, hidden/internal state, function, and second-injury response separately.

**Required comparison:** repaired system vs matched uninjured system after the same standardized second perturbation.

**Expected useful outcomes:** equivalent visible recovery with divergent future behavior; function recovery with altered internal organization; same hidden state rendered through different skins.

**Controls:** no-injury, visible-only repair, state reset, function-only acceptance.

**Gate:** reconcile SODC paper/code branch mapping before treating strongest recovery claims as reproduced.

**Current class:** validator / experiment protocol.

---

## C12. Cultural Annealing Regulator

**Source family:** CoNLL aging-game.

**Core idea:** mutation/plasticity privilege decreases with agent age while population turnover remains mandatory.

**AI SLOP use:** model conventions as carried disproportionately by older agents while new agents remain more mutable.

**Potential knobs:** lifespan, death interval, age distribution, mutation budget, update privilege, temperature analogue.

**Controls:** all-young, all-old, random-turnover, static equal-budget population, learning-rate-only / temperature-only analogues when the substrate exposes them.

**Boundary:** controller-level "age" in hosted models is only an analogy to optimizer plasticity.

**Current class:** population regulator.

---

## C13. Developmental Connectivity

**Source family:** Developmental Graph Cellular Automata.

**Core idea:** grow the computation routes themselves rather than only changing values on a fixed graph.

**Potential knobs:** growth steps, node budget, sensing noise, local state types, division/removal/connectivity rules, fitness.

**AI SLOP use:** developmental Temporary Mind/controller substrates; compare topology selection with weight/parameter selection.

**Controls:** random fixed topology of matched size; descriptor-selected vs task-selected growth; deterministic vs stochastic development.

**Gate:** exact accepted-manuscript/code correspondence unresolved.

**Current class:** developmental substrate.

---

## C14. Skin-State Dissociation

**Source family:** Cells2Pixels.

**Core idea:** treat organism dynamics and visible decoding as separately manipulable jurisdictions.

**Core experiment matrix:**
- same state / same decoder;
- same state / changed decoder;
- changed state / same decoder;
- changed state / changed decoder.

**AI SLOP use:** test whether a visual "mutation" changed the system or only its renderer.

**Controls:** equalize visible reconstruction when possible; repeat standardized perturbation from matched visible outputs.

**Current class:** visual adapter + ablation protocol.

---

## C15. Moving-Neighborhood Causal Rewiring

**Source family:** Neural Particle Automata.

**Core idea:** movement changes who can communicate; communication changes movement.

**Potential knobs:** support radius, particle count, movement rule, state rule, update probability, perturbation, species mixture.

**Core test:** exchange movement rules while holding state rules fixed, then reverse.

**Record:** interaction graph over time, morphology, task behavior, second-perturbation response.

**Boundary:** do not label persistent vortex/flow structure "memory" without a causal test.

**Current class:** ALife substrate / cybernetic experiment.

---

## C16. Moving Edit Jurisdiction

**Source family:** RIDGE.

**Core idea:** the permitted edit region follows predicted discrepancy instead of remaining fixed.

**Potential knobs:** mask quantile, softness, lag/delay, guidance schedule, edit window, seed.

**Core comparison:** fixed mask vs attention-derived mask vs discrepancy-following mask at matched edit strength.

**AI SLOP extension:** intentional mask lag so the jurisdiction is always following yesterday's wound.

**Boundary:** delayed-mask behavior is our proposed extension, not a reported RIDGE result.

**Current class:** flow-editing adapter / Separated Jurisdictions implementation.

---

## C17. Steering Donor Provenance Contract

**Source family:** activation source selection.

**Core idea:** "a steering vector for X" is underspecified unless the source construction is recorded.

**Required metadata:** donor prompt/context, extraction token/boundary, tail inclusion, layer, pooling, subtraction baseline, norm/strength, model/version.

**Controls:** random basis, matched norm, alternate donor source, held-out evaluation, no final-test layer selection.

**AI SLOP use:** upgrade the Reversible Activation-Axis Study and future SAE/steering experiments.

**Current class:** validator / experiment schema extension.

---

## C18. Semantic Fault Atlas

**Source family:** T2V-Resilience numerical fault injection.

**Core idea:** numerical perturbations may alter semantic correctness more than visible cleanliness.

**Archive fields:** fault location/type/dose, prompt, seed, changed object/event, semantic displacement, perceptual displacement, persistence across frames.

**Controls:** no-fault replay, zero-effect injection, matched fault dose, identical seed.

**AI SLOP use:** instrument Error Axiomatization/Causal Artifact Chain with reproducible fault metadata rather than generic glitch styling.

**Boundary:** use only local simulated faults in owned/open models; do not generalize to every hardware fault or proprietary system.

**Current class:** failure bank / validator.

---

## C19. Non-Normal Flare-and-Return Kernel

**Source family:** transient amplification mathematics.

**Core idea:** a system can be asymptotically stable while showing a large, structured finite-time excursion.

**Potential knobs:** coupling asymmetry, feedforward strength, initial direction, saturation, peak-gain target.

**Required measurements:** peak gain, excursion direction, return time, saturation, history dependence, final attractor.

**AI SLOP use:** concrete controller kernel for Structured Instability and Attractor Lock -> Perturb.

**Controls:** matched stable eigenvalues with altered non-normal coupling; linear vs nonlinear controller; perturbation-direction sweep.

**Boundary:** repeatable transient growth is not automatically chaos, memory, or nonreciprocity.

**Current class:** mathematical controller kernel.

---

# Promotion criteria

Promote one of these only when:

1. the intervention is runnable and configuration is recorded;
2. the claimed effect survives a matched control or ablation;
3. the useful signature recurs across more than one cherry-picked artifact;
4. the recipe adds capability not already represented by an existing operator/adapter;
5. mechanism confidence and creative utility remain separate;
6. implementation/provenance caveats are preserved rather than erased by a cool result.
