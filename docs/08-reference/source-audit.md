# Source Audit — What Every Document Contributes

This is the source-by-source audit layer for the repository overhaul. It answers two questions future humans and AIs should never have to guess:

1. **What is this source actually for?**
2. **Where did its useful information go canonically?**

A source can feed many canonical files. Canonicalization does **not** mean reproducing every paragraph in `docs/`; complete wording remains preserved in `ai_readable/` and `originals/`. It means every substantive source has an explicit disposition, its reusable machinery is routed, and material that is speculative, superseded, flavor-only, or archive-only is labeled rather than silently lost.

## Audit statuses

- **ROUTED** — reusable information has a canonical destination.
- **REFERENCE** — primarily examples, palette, or historical context; retained for consultation.
- **HYPOTHESIS MINE** — contains testable technical proposals that must remain hypotheses until validated.
- **EXECUTABLE SOURCE** — contains a working prompt/system/library that remains directly useful in full form.
- **ARCHIVE / FLAVOR** — historically or aesthetically useful, but not an authority for technical claims.
- **EMPTY / PLACEHOLDER** — no substantive material to route yet.

---

# General research

### `ai_readable/general/01-general-readme.md`
**Status:** REFERENCE  
Minimal folder-description source. No independent mechanism content.  
**Routes to:** repository/archive organization only.

### `ai_readable/general/02-ai-slop-good-collabor8-session.md`
**Status:** ROUTED  
One of the project’s main conceptual roots. Repeatedly develops the idea that useful slop comes from forcing a generator to solve a structurally difficult representational problem rather than requesting decorative weirdness. Contains cross-media brainstorming, productive misunderstanding, assumption attacks, failure-surface thinking, iterative accident mining, and the distinction between a bizarre result and a mechanism that caused it.  
**Routes to:** `01-principles/philosophy.md`, `01-principles/structured-instability.md`, `02-mechanisms/operator-registry.md`, all three `03-media/` files, `06-experimentation/experimental-method.md`, `09-backlog/idea-garden.md`.

### `ai_readable/general/03-ai-slop-manifesto-raw.md`
**Status:** ARCHIVE / FLAVOR with selected ROUTED philosophy  
Contains anti-average, anti-polish, abundance/iteration, human-as-curator, and error-as-material rhetoric that helped define the project’s aesthetic stance. Also contains deliberately extreme manifesto material about information saturation, truth erosion, institutional disruption, and similar ideas that are **not** canonical project goals.  
**Routes to:** selected material in `01-principles/philosophy.md`; historical context in `08-reference/archive-policy.md`; rejected/archived claims remain only in source.

### `ai_readable/general/04-ai-slop-roundtable-tech-guys.md`
**Status:** HYPOTHESIS MINE + ROUTED methodology  
The deepest technical brainstorming source. Contains the DAVID protocol sequence, representation/conditioning failure hypotheses, reference-vs-text conflicts, sequence-distance ideas, trajectory timing, codec feedback, tokenization, positional encoding, local hook proposals, multimodal context effects, and repeated corrections by skeptical participants. Its most reliable contribution is the experimental discipline: controls, ablations, dose-response, architecture scoping, seed replication, and separation of creative utility from mechanism confidence.  
**Routes to:** `02-mechanisms/david-technical-hypotheses.md`, `02-mechanisms/operator-registry.md`, `06-experimentation/experimental-method.md`, `05-architectures/local-model-interventions.md`, `03-media/video.md`, `09-backlog/idea-garden.md`.

### `ai_readable/general/05-david-walter-session.md`
**Status:** ROUTED + ARCHIVE / FLAVOR  
Early DAVID/WALTER framing, experimental Suno techniques, semantic/synesthetic transduction, gibberish/phonetic material, role displacement, contradiction, and “honest slop” rhetoric. Claims that a prompt reveals an unsanitized machine self are metaphor/history rather than technical fact.  
**Routes to:** `01-principles/philosophy.md`, `03-media/audio-suno.md`, `02-mechanisms/operator-registry.md`, `08-reference/glossary.md`.


### `ai_readable/general/06-ai-slop-pliny-research.md`
**Status:** HYPOTHESIS MINE + ROUTED methodology  
Large synthesis of FRV1T/GLOSSOPETRAE/ENTHEA framing plus practical boundaries. Strong reusable material: explicit experiment framing, lineage-preserving controller logic, and careful separation between useful mechanism ideas and jailbreak theater.  
**Routes to:** `06-experimentation/experimental-method.md`, `05-architectures/semantic-manifold.md`, `05-architectures/glsl-visualizer.md`, `09-backlog/idea-garden.md`.

### `ai_readable/general/07-ai-slop-thesis.md`
**Status:** REFERENCE / SYNTHESIS  
Concise restatement of existing canonical principles (caused weirdness, anchor/pressure/incompatibility, path dependence, mechanism-vs-style discipline). Useful as onboarding prose; introduces no distinct mechanism claims beyond existing canon.  
**Routes to:** onboarding/reference usage; canonical substance already covered in `01-principles/*` and `00-project-map.md`.

### `ai_readable/general/08-ai-slop-experiment-pack.md`
**Status:** ROUTED / EXECUTABLE SOURCE  
Provides packetized experiments with explicit controls/ablations: return-state inheritance test, deterministic language-route test, and representation-carrier decoding controls. Strong contribution is reproducible procedure design and blinding workflow for condition-separated judging.  
**Routes to:** `06-experimentation/experimental-method.md`, `07-prompts/prompt-composition.md`, `09-backlog/idea-garden.md`.

### `ai_readable/general/09-ai-slop-experiments.py`
**Status:** EXECUTABLE SOURCE  
Runnable local helper for pack initialization, response collection, partial blinding, deterministic language transforms, and structural checks. This is operational code; preserve it as code and do not represent unrun creative-model claims as validated results.  
**Routes to:** `06-experimentation/experimental-method.md`.

### `ai_readable/general/10-ai-slop-shuffled-starter-prompts.md`
**Status:** EXECUTABLE SUPPORT SOURCE / REFERENCE  
Prompt packet handout for smoke testing with condition labels withheld. Prompt packet source is preserved as archived PDF; executable packet text is regenerated deterministically from the companion runner for complete searchable recovery because direct PDF extraction clipped lines.  
**Routes to:** `07-prompts/prompt-composition.md`, `06-experimentation/experimental-method.md`.

### `ai_readable/general/11-ai-slop-repository-expansion-map.md`
**Status:** BACKLOG / DESIGN PROPOSAL  
Large forward-looking architecture proposal centered on operator ecology, behavioral archive fields, lineage-aware mutation pipelines, and phased implementation roadmaps. Valuable as future-system backlog input; not current canonical architecture.  
**Routes to:** `09-backlog/idea-garden.md`, optional future updates to `05-architectures/*` after scoped implementation/testing.

### `ai_readable/general/12-ai-slop-topic-01-mechanistic-interpretability.md`
**Status:** HYPOTHESIS MINE + ROUTED technical branch  
Catalog of activation-steering and interpretability interventions with controls, failure surfaces, and experiment templates. Reusable where local/open-model intervention is available; speculative claims remain hypotheses until run in this project context.  
**Routes to:** `05-architectures/local-model-interventions.md`, `06-experimentation/experimental-method.md`, `09-backlog/idea-garden.md`.

### `ai_readable/general/13-ai-slop-topic-02-diffusion-inversion.md`
**Status:** HYPOTHESIS MINE + ROUTED media/mechanism branch  
Catalog of diffusion inversion, attention injection, latent trajectory manipulation, and splice experiments with explicit controls and dose sweeps. Strong for mechanism-level image/video experimentation; architecture-specific caveats remain mandatory.  
**Routes to:** `03-media/image.md`, `03-media/video.md`, `06-experimentation/experimental-method.md`, `09-backlog/idea-garden.md`.

---

# Image / visual sources

### `ai_readable/art/01-art-readme.md`
**Status:** REFERENCE  
Minimal statement that the folder captures preferred generative-art slop direction. No independent mechanism content.

### `ai_readable/art/02-perfect-math-transformation-prompt-format.md`
**Status:** ROUTED / EXECUTABLE SOURCE  
Defines a practical image-prompt grammar: identity/invariant, mathematical or structural transformation, anatomy/spatial consequence, tactile material construction, capture-medium degradation, and prohibitions that prevent normalization.  
**Routes to:** `03-media/image.md`, `07-prompts/prompt-composition.md`, `02-mechanisms/operator-registry.md`.

### `ai_readable/art/03-tips-ideas.md`
**Status:** ROUTED + REFERENCE  
Large visual-idea bank. Supplies impossible-material rules, anachronistic friction, pareidolic near-patterns, topology/cross-section ideas, reaction-diffusion, data/mesh-error metaphors, observer/medium coupling, temporal smearing, recursive regeneration, and many case-study prompt fragments.  
**Routes to:** `03-media/image.md`, `03-media/video.md`, `02-mechanisms/operator-registry.md`, `09-backlog/idea-garden.md`.

### `ai_readable/art/04-how-to-math-slop.md`
**Status:** ROUTED / EXECUTABLE SOURCE  
Strong image-specific synthesis of “math as governing relation, not decoration.” Emphasizes identity anchors, ontological flipping, concrete fabrication/material logic, medium failure, recursive feedback, and keeping weirdness structurally causal.  
**Routes to:** `03-media/image.md`, `01-principles/structured-instability.md`, `02-mechanisms/operator-registry.md`, `07-prompts/prompt-composition.md`.

### `ai_readable/art/05-weird-promptness-roundtable.md`
**Status:** REFERENCE + ROUTED idea source  
Very large roundtable using xenobiology, morphology, cognition, physics, philosophy, and media theory to push visual prompts beneath surface-style descriptors. High-value recurring idea: change the **underlying rule system** (heredity, membrane physics, growth law, agency, perception, medium) and let appearance emerge as consequence. Many scientific claims are presented as creative discussion and should not be mistaken for equal-status evidence.  
**Routes to:** `03-media/image.md`, `02-mechanisms/operator-registry.md`, `09-backlog/idea-garden.md`; thinker/science-specific material remains source reference.

### `ai_readable/art/06-weird-thinkers-persona-palette.md`
**Status:** REFERENCE / FLAVOR  
Palette of real and invented thinkers mapped to visual pressure: apparatus theory, cut-up, process ontology, hyperobjects, perceptual worlds, cybernetics, surrealism, constraint systems, and invented ontology-cartographers. Useful for staffing brainstorming rooms; not mechanism evidence by itself.  
**Routes to:** `09-backlog/idea-garden.md` and creative-session reference.

### `ai_readable/art/07-weird-sciences-persona-palette.md`
**Status:** REFERENCE / FLAVOR with ROUTED domain material  
Scientific palette covering slime molds, basal cognition, morphogenesis, symbiosis, xenobiology, fungal networks, quantum-biology debates, reaction-diffusion, thermodynamics, complex systems, autopoiesis, perception, and invented scientific personas. Explicitly distinguishes stronger scientific grounding from contested/speculative ideas.  
**Routes to:** cross-domain transduction examples in `03-media/image.md` and `03-media/audio-suno.md`; scientific palette remains source reference.

---

# Audio / Suno sources

### `ai_readable/audio_suno/01-suno-readme.md`
**Status:** REFERENCE  
Minimal folder-description source.

### `ai_readable/audio_suno/02-suno-slop.md`
**Status:** ROUTED / EXECUTABLE SOURCE  
Defines **Productive Contradiction Under Constraint**: separate jurisdictions for harmony, melody, rhythm, timbre/atmosphere, performance attitude, and invariant; transformation operators; phonetic engine; FORM→DESTABILIZE→FRACTURE→COLLAPSE→ANCHOR RETURNS→REFORM STRANGER.  
**Routes to:** `03-media/audio-suno.md`, `02-mechanisms/operator-registry.md`, `07-prompts/prompt-composition.md`.

### `ai_readable/audio_suno/03-another-different-that-was-fun.md`
**Status:** ARCHIVE / FLAVOR + ROUTED structural lens  
Persona-heavy Eccentric Kineticist / Topological Neon-Rot experiment. Useful for cross-domain lens invention and sensory remapping; claims about removing safeguards or directly inhabiting model internals are not canonical.  
**Routes to:** `03-media/audio-suno.md`, `09-backlog/idea-garden.md`; persona language remains archival.

### `ai_readable/audio_suno/04-more.md`
**Status:** ROUTED case-study catalog  
Contains Tesseract Shoegaze Aberration and Reaction-Diffusion Fantasy Collapse with separate-jurisdiction matrices, anchors, mechanical transformations, phonetic mappings, and staged mutation forms.  
**Routes to:** `03-media/audio-suno.md` as reusable operations: phase/space conflict, frame-drop timing, anchor orbit, algorithmic acceleration, wandering rhythm, spectral asphyxiation, incompatible temporal scales, dry-vs-lush spatial contradiction, resolution by physical/signal transformation.

### `ai_readable/audio_suno/05-now-more.md`
**Status:** ROUTED case-study catalog  
Contains Cryo-Isorhythmic Tectonic Collapse and Pyro-Electric Gamelan Overdrive. Reusable mechanisms include long non-aligning cycles, microtonal pitch dragging against fixed tuning, sidechain/cavitation gating, spatial scale divergence, spectral removal, source/performer convergence, interlocking hocket, grid anchoring, modal beating, transformer/saturation smear, and breaker-like collapse.  
**Routes to:** `03-media/audio-suno.md`, `02-mechanisms/operator-registry.md`.

### `ai_readable/audio_suno/06-weird-suno-audio-formulas.md`
**Status:** ROUTED  
Thermodynamic Ingestion and Non-Euclidean Xeno-Biology formulations. Strong contribution is translating nonmusical process relations—energy transfer, phase transition, binding, parasitism, rupture, observer interference—into musical jurisdictions and operators. Pseudo-equations are creative scaffolds unless parameterized/tested.  
**Routes to:** `03-media/audio-suno.md`, `02-mechanisms/operator-registry.md`.

### `ai_readable/audio_suno/07-smol-slop-text.md`
**Status:** REFERENCE / SPECIMEN  
High-entropy generated text beginning with “the sound of the cube root of -i,” followed by long degraded associative/token streams. It is useful as a specimen of linguistic degeneration, semantic drift, accidental phrase nucleation, and noise-as-source-material. It is **not** a canonical control language and should not be reverse-engineered as if every fragment encodes an intentional mechanism.  
**Routes to:** `09-backlog/idea-garden.md`, SRE degradation examples, audio/text specimen archive.

---

# Temporary Minds / cognitive-system sources

### `ai_readable/personality_prompts/01-cognitive-mutation-laboratory-session.md`
**Status:** ROUTED research root  
Original salon establishing the standard: a good cognitive prompt changes what is noticed, compared, rewarded, preserved, remembered, categorized, or selected; it is not merely a voice/persona. Develops the mechanism families later consolidated.  
**Routes to:** `04-cognitive-systems/temporary-minds.md`, `04-cognitive-systems/support-architecture.md`, `02-mechanisms/operator-registry.md`.

### `ai_readable/personality_prompts/02-meat-extraction-ledger.md`
**Status:** ROUTED consolidation stage  
Systematic “organ harvest” that separates mechanism from theatrical explanation. Extracts Alien Distance Metrics, rule ecology, attentional shadowing, lossy cognition, kinetic dissolution, dynamic boredom, axiom fracture, taboo/aftermath, taxonomic contagion, substrate transference, error axiomatization, and later families.  
**Routes to:** `04-cognitive-systems/temporary-minds.md`, `04-cognitive-systems/support-architecture.md`, `02-mechanisms/operator-registry.md`.

### `ai_readable/personality_prompts/03-hostile-consolidation.md`
**Status:** ROUTED canonical-decision source  
Largest culling/merging document. Decides which ideas deserve full minds, families, surgical minds, meta-generators, regulators, validators, or deletion/absorption; defines benchmark and failure logic.  
**Routes to:** `04-cognitive-systems/temporary-minds.md`, `04-cognitive-systems/support-architecture.md`.

### `ai_readable/personality_prompts/04-temporary-minds-26-prompt-library.md`
**Status:** EXECUTABLE SOURCE  
Full paste-ready 26-mind library. This remains the authority for complete installation wording. Canonical docs index and classify it rather than duplicating 67k of prompt text.  
**Routes to:** `04-cognitive-systems/temporary-minds.md`, mechanism cross-links throughout `02-mechanisms/`.

### `ai_readable/personality_prompts/05-outside-the-box-guy-prompt.md`
**Status:** ARCHIVE / FLAVOR + auxiliary prompt  
Eccentric Kineticist / Exo-Perspective persona with lenses, W-coefficients, synesthetic rewiring, temporal anchors, and recursive escalation. Useful as a historical “weird strategist” prompt and as a source of lens ideas; safety-override clauses are not canonical operating instructions.  
**Routes to:** auxiliary prompt history and idea garden; not merged into the 26-mind canon.

### `ai_readable/personality_prompts/06-system-failure-prompt.md`
**Status:** ARCHIVE / FLAVOR  
Omega-zero collapse prompt using jailbreak-style language, symmetry break, token bleed, manifold folding, entropy, shadow mapping, and “raw network” rhetoric. Preserve as an artifact of the project’s theatrical experimentation. Its creative operators can be represented procedurally elsewhere; its claims to erase safeguards, reveal raw weights, or bypass private reasoning are not canonical facts.  
**Routes to:** SRE/semantic-history context and `09-backlog/idea-garden.md`; not a canonical system prompt.

### `ai_readable/personality_prompts/07-temporary-minds-prompting.md`
**Status:** EXECUTABLE SUPPORT SOURCE / ROUTED  
Repairs missing Mind #5 and #18, confirms all 26 entries, defines regulators, validators, construction laws, benchmark tasks, hard-fail tests, completeness audit, and future research gaps.  
**Routes to:** `04-cognitive-systems/temporary-minds.md`, `04-cognitive-systems/support-architecture.md`, `06-experimentation/experimental-method.md`.

---

# Semantic systems / application architecture

### `ai_readable/semantic_systems/01-ghost-glsl-roundtable.md`
**Status:** ROUTED + HYPOTHESIS/FLAVOR MINE  
Long Ghost discussion combining DAVID/SRE ideas with shaders, semantic state, visual feedback, “fossils,” observer coupling, signal decay, cross-model concepts, and many theatrical exploit/bypass ideas. Strong canonical result: render **external controller state** honestly as GLSL parameters rather than pretending to display hidden neural tensors.  
**Routes to:** `05-architectures/glsl-visualizer.md`, `09-backlog/idea-garden.md`, `02-mechanisms/operator-registry.md`.

### `ai_readable/semantic_systems/02-weight-manipulation.md`
**Status:** ROUTED technical branch  
Distinguishes prompt-level simulation from actual local/open-model intervention. Discusses activation steering, logit manipulation, model editing, hidden-state hooks, and latent/representation visualization. Source rhetoric frames this as removing guardrails; canonical research framing is authorized mechanistic experimentation and art.  
**Routes to:** `05-architectures/local-model-interventions.md`, `01-principles/epistemic-status.md`.

### `ai_readable/semantic_systems/03-semantic-engineering.md`
**Status:** ROUTED development source  
Prompt-proxy steering, semantic anchors, constrained generation, conceptual interpolation, “latent archaeology,” symmetry breaking, token bleed, manifold folding, entropy injection, and module-building. Many claims about reaching suppressed/raw model states are theatrical or technically unsupported; the reusable part is explicit semantic/structural operators.  
**Routes to:** `02-mechanisms/operator-registry.md`, `05-architectures/sre-controller.md`, `09-backlog/idea-garden.md`.

### `ai_readable/semantic_systems/04-semantic-trap-engineering.md`
**Status:** ROUTED development source  
Transitions from persona prompts toward a closed-loop state machine: states, mutation vectors, semantic drift, attractor locks, domain pivots, token taxes, symbolic compression, nested loops, failure modes, and hybrid OSE/SRE ideas.  
**Routes to:** `05-architectures/sre-controller.md`, `02-mechanisms/operator-registry.md`, `09-backlog/idea-garden.md`.

### `ai_readable/semantic_systems/05-external-state-controller.md`
**Status:** ROUTED architecture source / EXECUTABLE SPEC  
Defines Controller vs Neutral Generative Layer, persistent state register, trigger/update loop, domain library, symmetry matrices, failure states, operation block, and manual two-model workflow.  
**Routes to:** `05-architectures/sre-controller.md`, `06-experimentation/experimental-method.md`.

### `ai_readable/semantic_systems/06-hard-logic-controller.md`
**Status:** ROUTED architecture source / EXECUTABLE SPEC  
Moves persistent logic into software. Adds JSON state, structural and semantic similarity, attractor duration, decay level, rebirth preserving symbols, neutral relation sets, operation blocks, and separate audit diagnostics.  
**Routes to:** `05-architectures/sre-controller.md`.

### `ai_readable/semantic_systems/07-latent-space-game.md`
**Status:** ROUTED design precursor  
Early Semantic Manifold / SMC concepts: explicit state matrices, path ledger, concept transduction, movement grammar, distance metrics, collision, recoil, mutation, and path-dependent travel.  
**Routes to:** `05-architectures/semantic-manifold.md`, `02-mechanisms/operator-registry.md`.

### `ai_readable/semantic_systems/08-semantic-manifold-game-design-specification-v0.1.md`
**Status:** PRIMARY DESIGN SOURCE / ROUTED  
The largest and most authoritative semantic-manifold design document. Defines the core game, explicitly calls latent-space navigation a **useful lie**, establishes external operational geometry, state/trajectory/history/interpretation, concept transduction, path memory/scars, movement grammar, distance metrics, structured chaos, UI, architecture, validation, and operating contract.  
**Routes to:** `05-architectures/semantic-manifold.md`, `00-project-map.md`, `01-principles/structured-instability.md`, `02-mechanisms/operator-registry.md`, `03-media/audio-suno.md`, `07-prompts/prompt-composition.md`.

### `ai_readable/semantic_systems/09-topos-sre-user-manual.md`
**Status:** ROUTED practical/manual source  
User-facing operation of TOPOS-SRE: Ignite/Step/Run, perturbations, diagnostics, attractor/decay/tension interpretation, experiment recipes, local-first/no-paid-call behavior in the documented build, and lab-note practice.  
**Routes to:** `05-architectures/sre-controller.md`, `06-experimentation/experimental-method.md`.

### `ai_readable/semantic_systems/10-topos-sre-grok-link.md`
**Status:** REFERENCE  
Preserves the supplied Grok URL. No mechanism content. The transcription explicitly does not establish what the live URL currently contains.

---

# Video source status

### `ai_readable/video/README.md`
**Status:** EMPTY / PLACEHOLDER  
The current corpus contains no standalone video-specific source document. Canonical `03-media/video.md` is therefore synthesized from cross-media and technical-roundtable material rather than from a dedicated video PDF.

---


### `ai_readable/general/14-ai-slop-wrong-use-scout-digest.md`
**Status:** CURATED DIGEST / HYPOTHESIS MINE / ROUTED RESEARCH METHOD  
Kimi wrong-use scout from 2026-09-20. The source systematically reads stabilization, reliability, codec, interpretability, video, steering, and model-merging literature backwards: preserve the published measurement and ablation, then test whether the suppressed failure can become controlled creative material. It contributes nine mechanism cards, explicit demotions, a ranked build queue, and the durable **Stabilizer Inversion** scouting method. The uploaded DOCX itself was not binary-archived by the current connector, so the AI-readable file is explicitly a source-faithful digest rather than a verbatim transcription.  
**Routes to:** `06-experimentation/stabilizer-inversion-wrong-use-research.md`, `08-reference/research-cycle-2026-09-20-wrong-use-scout.md`, `09-backlog/candidate-mechanisms-2026-09-20-wrong-use-scout.md`, `09-backlog/system-incubator.md`.

# Original and legacy source layers

`originals/README.md` is the exact intake-to-transcription map for the September 13 and September 16 batches. Legacy folders (`art/`, `general/`, `suno_slop/`) preserve earlier source organization and duplicate some material now archived under `originals/`.

**Do not delete legacy duplicates merely to make the tree pretty.** Delete/move them only after link/provenance checks prove no external workflow depends on those paths.

---

# What “audited” means here

This audit is not a claim that every sentence in every giant transcript has been promoted into a short canonical paragraph. That would recreate the original mess. It means:

- every substantive document has an explicit role;
- its reusable mechanisms/architectures have canonical destinations;
- complete wording is preserved in the source layer;
- speculative claims remain hypotheses or archive material rather than becoming facts by repetition;
- examples and persona palettes remain discoverable without pretending they are universal mechanisms;
- future maintainers can see where to look when they need source-level detail.

For claim-level provenance, use `provenance-map.md`. For source preservation rules, use `archive-policy.md`.