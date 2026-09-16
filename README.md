# AI SLOP — Structured Instability Lab

This repository is a research-and-art notebook for **making generative systems do interesting things when ordinary representational shortcuts stop working cleanly**.

The project calls that territory **AI slop**: glitches, semantic collisions, unstable identity, impossible continuity, model repair artifacts, strange phonetics, topology failures, temporal drift, accidental structures, and other emergent results produced by difficult constraints. The goal is not random garbage and not “make it weird.” The goal is **structured instability**.

## Start here

- [`AI_CONTEXT.md`](AI_CONTEXT.md) — compact orientation for any AI or collaborator entering the repo.
- [`docs/README.md`](docs/README.md) — canonical documentation map.
- [`docs/00-project-map.md`](docs/00-project-map.md) — how ideas, media, systems, and archives fit together.
- [`docs/01-principles/structured-instability.md`](docs/01-principles/structured-instability.md) — the central experimental method.
- [`docs/01-principles/constraint-governance.md`](docs/01-principles/constraint-governance.md) — the “wrong simulator / Governance Engine” design model extracted from the early research.
- [`docs/02-mechanisms/operator-registry.md`](docs/02-mechanisms/operator-registry.md) — deduplicated cross-media operator catalog.
- [`docs/02-mechanisms/david-technical-hypotheses.md`](docs/02-mechanisms/david-technical-hypotheses.md) — complete DAVID Protocol 01–20 hypothesis registry, cleaned up and caveated.
- [`docs/06-experimentation/experimental-method.md`](docs/06-experimentation/experimental-method.md) — controls, ablations, dose-response, replication, and artifact-family testing.
- [`docs/06-experimentation/run-log-template.md`](docs/06-experimentation/run-log-template.md) — reusable lab record.
- [`docs/08-reference/source-audit.md`](docs/08-reference/source-audit.md) — what every substantive source contributes and where it was routed.
- [`docs/08-reference/glossary.md`](docs/08-reference/glossary.md) — canonical meanings of project language.
- [`docs/08-reference/intake-workflow.md`](docs/08-reference/intake-workflow.md) — how future source dumps get absorbed without recreating the chaos.
- [`machine/index.json`](machine/index.json), [`machine/operators.json`](machine/operators.json), [`machine/david_protocols.json`](machine/david_protocols.json), [`machine/sources.json`](machine/sources.json) — machine-readable routing indexes.

## The repo has two authority layers

### Canonical layer — `docs/`
Curated, decomposed documentation organized by **what an idea does**: principle, mechanism, medium, cognitive system, architecture, experiment, or reference function.

A single source may contribute to many canonical documents. A single canonical document may synthesize many sources. Claims are labeled by epistemic status so brainstorming does not quietly become “technical fact.”

### Source / archive layer — `ai_readable/`, `originals/`, and legacy source folders
These preserve the research trail: complete transcriptions, PDFs, raw conversations, prompt experiments, discarded branches, theatrical manifesto material, and historical versions.

The archive is authoritative about **what was said**. The canonical layer is authoritative about **what the project currently means and how to use it**.

Nothing is discarded merely because it is messy. Mess belongs in the archive; distilled machinery belongs in `docs/`.

## Core rule

> Do not ask only “what weird thing should the model make?” Ask: **what problem can we give the generative system such that its attempt to solve the problem becomes the artwork?**

That means preferring governing relations, transformations, developmental rules, path dependence, conflicting but still-active constraints, and measurable perturbations over decorative stacks of “surreal / psychedelic / glitch / fractal” adjectives.

A related early-research framing calls the generator a **Governance Engine**: not a literal architecture claim, but a useful design model in which the artwork is the compromise produced by mismatched mandates that cannot all resolve conventionally.

## Intellectual honesty

“Latent space” is useful project language, but this repo does **not** assume that a prompt gives direct access to a model’s hidden activations, weights, safeguards, or one literal navigable internal map. When a mechanism is only a plausible explanation for observed behavior, it is labeled **HYPOTHESIS**. When it is merely a useful metaphor or untested idea, it is labeled accordingly.

Likewise, old source documents sometimes contain jailbreak rhetoric, claims about bypassing safeguards, anthropomorphic “true machine self” language, or manifesto-style fantasies about epistemic sabotage. Those materials remain preserved as historical sources; they are **not project objectives or technical claims**.

## Main research tracks

- **Image:** identity anchors, anatomy-as-process, topology, material anchoring, medium degradation, iterative feedback.
- **Video:** temporal identity, correspondence failure, topology through time, path-dependent transformation, motion/causal contradictions.
- **Audio / Suno:** separated musical jurisdictions, structural contradiction, phonetic engines, tuning/meter/timbre conflicts, route-based composition.
- **Temporary Minds:** 26 installable procedural cognition systems plus regulators, validators, and benchmark machinery.
- **Semantic systems:** external controllers, path ledgers, semantic-manifold navigation, TOPOS-SRE, and GLSL state visualization.
- **DAVID / model-mechanism research:** a complete 20-protocol hypothesis registry covering conditioning conflict, iteration, binding, tokenization, codec drift, guidance, topology/reference pressure, and instrumented-model experiments.
- **Lens research:** thinker/science palettes used as relation generators, with philosophy, established science, contested hypotheses, and invented personas kept epistemically distinct.

## Intake rule

New source material can be dropped into `new_to_be_processed_by_copilot_agent/`. Preserve the original, verify or create a searchable transcription, then decompose its information into the canonical structure. Update the source audit and routing indexes.

**Do not merely create another giant transcription and call it organized.**

The source trail matters. So does making the damn thing usable.
