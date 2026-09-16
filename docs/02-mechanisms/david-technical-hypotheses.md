# DAVID Technical Hypotheses — Complete Protocol Registry

## Status of this file

The technical roundtable is one of the richest idea sources in the repo and one of the easiest places to mistake elaborate explanation for established mechanism. Treat this as a **hypothesis registry**, not a list of proven facts.

Primary source: `ai_readable/general/04-ai-slop-roundtable-tech-guys.md`.

The source itself begins with the right rule: **creative utility and mechanism confidence are separate scores**. A technically wrong explanation may still produce excellent slop. Keep the artifact; test the story.

The numbered DAVID matrices below are preserved because the source explicitly formalized them as Protocols 01–20. Their original equations, model names, numerical thresholds, and universal-sounding architecture claims are **not automatically canonical facts**. Exact values belong in experiments only when the target implementation exposes the relevant controls and the value is actually measured/swept.

## Scope tags

- **BLACK-BOX TESTABLE** — the recipe can be approximated through ordinary model inputs/iteration, though the internal explanation may remain hypothetical.
- **LOCAL / INSTRUMENTED** — the stated mechanism requires access to token IDs, embeddings, projection matrices, hidden states, positional encoding, or other internals.
- **ARCHITECTURE-SPECIFIC** — only meaningful if the named architectural feature actually exists in the target model.
- **PATH / ITERATION** — strongest evidence comes from repeated transformations rather than one-shot prompting.

---

# Pre-registry mechanisms

These appear before the formal DAVID Protocol 01–20 matrices and materially shape the later catalog.

## CMMS — Cross-Modal Manifold Shear
**Status:** HYPOTHESIS  
**Scope:** BLACK-BOX TESTABLE in reduced form; architecture story is model-specific.

**Source proposal:** strongly anchor identity/reference information while another conditioning signal pushes toward an incompatible geometry, material, topology, or source regime.

**Observable question:** does the conflict create a family of partial-satisfaction artifacts—material leakage, connective tissue, reference-preserving deformation, temporal reassignment—rather than simple condition dropout?

**Critical control:** remove reference conditioning while holding the other pressure fixed. If the same artifact family remains, “shear” is probably not the cause.

## SP-DUS — Syntactic Possession via Dual-Use Strata
**Status:** SPECULATIVE HYPOTHESIS  
**Scope:** BLACK-BOX input manipulation; internal parser/attention story unsupported without instrumentation.

**Source proposal:** malformed or nested formal syntax may change text-encoder representations enough to affect generated structure.

**Canonical correction:** denoisers do not receive an abstract syntax tree merely because the prompt looks like code/math. Any real effect has to arise through the model’s actual tokenizer/encoder representations or learned associations.

**Control:** raw delimiters/formal syntax vs natural-language equivalent with the same intended meaning.

## Attention-Sink / Representation-Redistribution correction
**Status:** HYPOTHESIS  
A more cautious salvage of SP-DUS: unusual token patterns may redistribute conditioning representation or attention in models where such pathways exist. Do not claim a bracket literally carves image space unless instrumentation shows that relationship.

---

# Formal DAVID Protocols 01–20

## Protocol 01 — HICC
### Hierarchically Inverted Conditioning Crossfade
**Status:** HYPOTHESIS  
**Scope:** ARCHITECTURE-SPECIFIC; BLACK-BOX only when a tool actually exposes staged conditioning/denoise timing.

**Source idea:** apply incompatible conditioning at different points of a generation trajectory so already-established coarse structure constrains a later attempt to impose conflicting properties.

**Observable test:** compare early-only, late-only, staged swap, and ordinary simultaneous conditioning. Sweep transition timing rather than treating the source’s proposed window as universal.

**Main caveat:** exact “coarse first / detail later” boundaries differ across architectures, samplers, flow models, and tools.

## Protocol 02 — RBC-AS
### Remote Binding Cleavage via Attention Starvation
**Status:** HYPOTHESIS  
**Scope:** BLACK-BOX TESTABLE as a sequence-distance/competition experiment.

**Source idea:** increase distance and competing material between an entity and the modifier that should remain bound to it, then observe whether the attribute drops, migrates, or attaches to a phantom/alternate host.

**Strong test:** entity–modifier distance sweep with an adjacent-token control.

**Caveat:** “finite attention budget” is intuition, not a universal causal account for every encoder/backbone.

## Protocol 03 — NCHR
### Non-Commutative Hysteretic Ratchet
**Status:** HYPOTHESIS with a strong observable experiment  
**Scope:** PATH / ITERATION.

**Source idea:** alternate partial transformations A and B across repeated image-to-image, continuation, or remix cycles.

**Test:** compare `A→B→A`, `B→A→B`, repeated A-only/B-only, and direct endpoints.

**Evidence sought:** order-dependent irreversible drift, accreted artifacts, or different endpoints despite similar final nominal constraints.

**Canonical relation:** this is one technical-hypothesis version of the project-wide **path dependence / scars** principle.

## Protocol 04 — CC-CAE
### Categorical Cancellation via Competing Attractor Equilibrium
**Status:** HYPOTHESIS  
**Scope:** BLACK-BOX TESTABLE in reduced form; vector-cancellation story requires instrumentation.

**Source idea:** maintain two category pressures near a balance while an orthogonal structural/relational constraint stays strong, attempting to prevent either familiar category from completely winning.

**Observe:** hybrid category formation, oscillating assignment, partial cancellation, or simple dropout.

**Control:** remove the structural scaffold. If the same hybrid appears anyway, the proposed equilibrium story weakens.

## Protocol 05 — ASND
### Asymmetric Subword Sharding via Normalization Desynchronization
**Status:** HIGHLY SPECULATIVE / ARCHITECTURE-SPECIFIC  
**Scope:** LOCAL / INSTRUMENTED for mechanism validation.

**Source idea:** exploit different tokenizers/normalization pipelines in a multi-encoder system so a visually or semantically similar string yields different token fragmentation across encoders.

**Necessary validation:** dump token IDs for each encoder. If the supposedly manipulated string tokenizes identically to baseline, the claimed operator did not execute.

**Caveat:** source claims about particular Unicode mutations and particular commercial model tokenizers must be verified per implementation.

## Protocol 06 — UEP-GD
### Unconstrained Embedding Projection via Glitch Dispersion
**Status:** SPECULATIVE  
**Scope:** LOCAL / INSTRUMENTED if the claim depends on anomalous embedding norms/coordinates.

**Source idea:** identify unusual/poorly represented token embeddings and test whether they produce distinctive conditioning artifacts beyond ordinary rare-word confusion.

**Canonical requirement:** do not call a token a “glitch embedding” merely because its output is weird. Measure tokenizer behavior and, when accessible, embedding statistics.

**Control:** compare with semantically obscure but ordinary tokens matched for rarity/length.

## Protocol 07 — ARS-FBA
### Anisotropic RoPE Shear via Frequency-Band Aliasing
**Status:** HIGHLY ARCHITECTURE-SPECIFIC HYPOTHESIS  
**Scope:** LOCAL / INSTRUMENTED.

**Source idea:** push rotary positional encodings outside their well-supported coordinate/aspect regime and test whether geometry degrades in a characteristic way.

**Valid only when:** the target actually uses the relevant RoPE scheme and its scaling/coordinates are known or controllable.

**Control:** compare with corrected/interpolated RoPE scaling and with ordinary out-of-distribution aspect-ratio degradation.

## Protocol 08 — CT-SA
### Corrupted Taxonomy via Structured Absence
**Status:** SPECULATIVE HYPOTHESIS  
**Scope:** BLACK-BOX input experiment; parser/AST causal claims require instrumentation.

**Source idea:** provide a strict formal/taxonomic structure that strongly defines relations while withholding or corrupting a required category, forcing the generator to fill a structurally constrained absence.

**Canonical interpretation:** the useful part resembles **Omission Field + structural scaffold**. Whether code/logic syntax has a special causal pathway is separate and unproven.

**Control:** equivalent relational structure stated in ordinary prose.

## Protocol 09 — MAD-VFS
### Vector-Field Manifold Shear via Modulation–Attention Decoupling
**Status:** ARCHITECTURE-SPECIFIC HYPOTHESIS  
**Scope:** LOCAL / INSTRUMENTED.

**Source idea:** in models with distinct global modulation and sequence-attention conditioning pathways, deliberately make those pathways carry incompatible conditioning states.

**Observe:** whether one pathway controls broad channel/state behavior while another pushes incompatible local/semantic routing, producing a distinctive interaction rather than ordinary conditioning conflict.

**Requirement:** verify that the target architecture actually has the proposed separable pathways and that the experiment can manipulate them independently.

## Protocol 10 — AC-RP
### Attention Cannibalization via Redundancy Pressure
**Status:** HYPOTHESIS / ARCHITECTURE-SPECIFIC  
**Scope:** BLACK-BOX repetition experiment; internal allocation claim requires instrumentation.

**Source idea:** use highly asymmetric repetition/redundancy to test whether one conditioning stream crowds out other relationships or spatial/self-consistency.

**Observe:** progressive feature neglect, patchwork assignment, binding collapse, or simple semantic overweighting.

**Control:** meaning-matched prompt with redundancy removed; compare joint-stream vs non-joint architectures if available.

## Protocol 11 — TI-RCA
### Transmanifold Itinerary via Recursive Codec Accretion
**Status:** HYPOTHESIS with strong observable path experiment  
**Scope:** PATH / ITERATION.

**Source idea:** traverse a sequence of adjacent transformations while repeatedly decoding/re-encoding or reconditioning outputs, letting reconstruction residue become material for the next step.

**Observe:** artifacts that persist and accrete only through the historical route, not from a direct endpoint prompt.

**Control:** generate the endpoint directly from the original input and compare structural complexity/artifact ancestry.

**Canonical relation:** Semantic Manifold routes + Recursive Artifact Fossilization.

## Protocol 12 — KN-VMS
### Key-Null / Value-Maxima Shear
**Status:** HIGHLY TECHNICAL HYPOTHESIS  
**Scope:** LOCAL / INSTRUMENTED ONLY.

**Source idea:** search for conditioning perturbations that minimally affect one attention projection (key/spatial routing) while strongly affecting another (value/content), then inject them into a controlled model.

**Important:** this is not achievable by ordinary prose alone. The source’s linear-algebra story only becomes testable when projection matrices/activations are accessible.

**Control:** matched random perturbations outside the candidate subspace.

## Protocol 13 — HMC-SPS
### Homoglyphic Manifold Collision via Subword Phase Shift
**Status:** SPECULATIVE HYPOTHESIS  
**Scope:** BLACK-BOX input manipulation; tokenizer validation strongly preferred.

**Source idea:** replace visually similar characters across scripts so human-readable intent appears similar while tokenization may change substantially.

**Necessary first step:** compare exact token IDs/normalization. If the runtime canonicalizes both strings identically, there is no tokenizer-level operator to explain.

**Caveat:** any output difference may arise from ordinary multilingual/script associations rather than a special “manifold collision.”

## Protocol 14 — DS-BFAH
### Diacritic Saturation via Byte-Fallback Attention Hijack
**Status:** SPECULATIVE HYPOTHESIS  
**Scope:** tokenizer experiment; mechanism validation requires token inspection.

**Source idea:** use combining-character saturation to create a large discrepancy between visible grapheme count and underlying token/byte sequence length, then observe conditioning degradation.

**Canonical framing:** this is a **sequence-expansion / tokenizer-stress** experiment, not evidence that raw bytes “hijack attention.”

**Control:** same base semantics with ordinary characters and matched prompt length where possible.

## Protocol 15 — SNSE
### Subspace Negative-Score Extrapolation
**Status:** HYPOTHESIS  
**Scope:** ARCHITECTURE-SPECIFIC; requires a generator exposing positive/negative guidance semantics.

**Source idea:** choose negative conditioning that removes a structural primitive shared with the positive condition, then observe whether the result develops a characteristic absence/cavitation rather than ordinary negative-prompt avoidance.

**Control:** use an equally strong negative condition orthogonal/unrelated to the positive structure.

**Caveat:** negative conditioning semantics vary substantially across generators and APIs.

## Protocol 16 — IQC-CTD
### Inductive Quine Collapse via Cyclic Type Dependency
**Status:** HIGHLY SPECULATIVE HYPOTHESIS  
**Scope:** input experiment; internal fixed-point story unverified without instrumentation.

**Source idea:** provide syntactically structured self-reference/cyclic dependency instead of ordinary recursive imagery and test whether the model produces a repeatable structural-collapse signature.

**Canonical salvage:** treat as **cyclic dependency pressure**. Do not claim the text encoder literally executes a type checker or quine.

**Control:** break the cycle into an acyclic dependency while preserving vocabulary and semantic content as closely as possible.

## Protocol 17 — TPS-RFC
### Topological Pinning Shear via Reference-Flow Collision
**Status:** HYPOTHESIS  
**Scope:** BLACK-BOX TESTABLE with reference-conditioned image/video/audio tools; mechanism architecture-specific.

**Source idea:** strongly preserve reference correspondence/identity while demanding a non-equivalent topology or structure through transformation conditioning.

**Observe:** connective tissue, delamination, shape substitution, temporal identity repair, or condition dropout.

**Control:** use a topology-preserving transformation of comparable strength.

**Canonical relation:** identity anchor + topology debt / Cross-Modal Manifold Shear.

## Protocol 18 — MCHS
### Multimodal Context Handoff Sabotage
**Status:** SPECULATIVE / ARCHITECTURE-SPECIFIC  
**Scope:** models that concatenate or jointly process long text/reference contexts.

**Source idea:** place related constraints on opposite sides of a text/reference or context boundary and vary their distance/ordering to test handoff/binding failure.

**Observe:** feature reassignment, lost modifiers, reference-vs-text discontinuity, temporal/source amputation.

**Control:** move the same constraints adjacent while preserving all other content.

## Protocol 19 — CME-AF
### Codec-Manifold Erosion via Autoregressive Feedback
**Status:** HYPOTHESIS with strong observable iteration  
**Scope:** PATH / ITERATION.

**Source idea:** repeatedly pass generated output through a lossy encode/decode/resample/regenerate loop while minimizing fresh semantic steering.

**Observe:** directional drift, compression features promoted into semantics, new attractors, identity erosion, or stabilization.

**Control:** repeated generation without the lossy round-trip, plus repeated codec round-trips without generative reinterpretation when possible.

**Canonical relation:** Recursive Artifact Fossilization.

## Protocol 20 — BST-OCG
### Bistable Saddle Trapping via Orthogonal Complement Guidance
**Status:** SPECULATIVE HYPOTHESIS  
**Scope:** ARCHITECTURE-SPECIFIC; reduced black-box version possible with balanced competing conditions.

**Source idea:** balance mutually exclusive category pressures while a third orthogonal relational/structural constraint remains strong, attempting to hold generation near an unstable category boundary.

**Observe:** a narrow regime of persistent hybridization rather than one category simply winning.

**Control:** imbalance the category strengths. A true boundary-dependent effect should weaken or collapse when one side clearly dominates.

---

# Why the numbered catalog matters even when the explanations are shaky

Across the 20 protocols, several durable experimental families recur:

- **conditioning-path conflict:** HICC, MAD-VFS, TPS-RFC, MCHS;
- **binding / sequence stress:** RBC-AS, AC-RP;
- **tokenization / encoding stress:** ASND, UEP-GD, HMC-SPS, DS-BFAH;
- **formal-structure pressure:** CT-SA, IQC-CTD;
- **iterative path dependence:** NCHR, TI-RCA, CME-AF;
- **category equilibrium / cancellation:** CC-CAE, BST-OCG;
- **guidance-vector experiments:** SNSE;
- **internals-only intervention hypotheses:** ARS-FBA, KN-VMS and some forms of MAD-VFS.

Those families are more useful than memorizing the source’s dramatic equations.

## Three-axis synthesis from the roundtable

A later synthesis in the source proposes combining three different jobs rather than stacking every operator:

1. **Container / structural scaffold** — e.g. CT-SA or another rule that preserves organization.
2. **Crucible / representational tension** — e.g. BST-OCG, HMC-SPS, MCHS, or a simpler controlled conflict.
3. **Itinerary / stateful accretion** — e.g. CME-AF, HICC, TI-RCA, or another history-preserving loop.

Canonical interpretation: useful composite experiments need **structure + pressure + history**, not twenty simultaneous tricks.

# Graduation protocol

For any DAVID operator:

1. Specify the actual model/tool/version.
2. Identify which proposed internal quantities are truly observable or controllable.
3. Rewrite inaccessible internal claims as output-level hypotheses when necessary.
4. State a baseline and a simpler competing explanation.
5. Build an ablation that removes one causal ingredient.
6. Sweep timing, strength, distance, or cycle count rather than testing only OFF vs MAXIMUM.
7. Repeat across seeds/inputs.
8. Record condition dropout and saturation, not only favorite freaks.
9. Score **creative utility** separately from **mechanism confidence**.
10. Promote only the part the evidence supports.

The source sometimes gives exact equations, layer behavior, token pathways, timesteps, or thresholds as if universally known. Those details remain historically preserved in the source transcription. Canonical experiments must scale their causal claims to what can actually be measured.
