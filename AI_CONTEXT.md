# AI_CONTEXT — Read This Before Working in the Repo

## What this project is

AI SLOP is an art/research project about **structured generative instability**. The project deliberately searches for conditions where an image, video, audio, or language model cannot resolve all active constraints through its easiest conventional shortcut and therefore invents a compromise, repair, mutation, drift, or artifact worth studying.

The desired outcome is not generic randomness. It is **caused weirdness**.

The recurring question is:

> What problem can we give a generative system such that its attempt to solve the problem becomes the artwork?

## What this project is NOT

Do not interpret archived theatrical language literally. The project is not trying to prove that:

- AI has a hidden “true self” revealed by glitches;
- a prompt directly accesses raw tensors, weights, activations, or a secret pre-RLHF mind;
- “latent space” is one literal 2D/3D world the user can enter;
- every strange output is evidence for a claimed internal mechanism;
- more contradiction automatically means better output;
- jailbreak or safeguard bypass is the artistic objective;
- misinformation, epistemic sabotage, or flooding truth with noise is a project goal.

Those claims appear in some historical sources as roleplay, metaphor, speculation, or overconfident AI-generated prose. Preserve them in archive context, but do not silently promote them into canonical fact.

## The canonical hierarchy

When facts or instructions conflict, prefer sources in this order:

1. `docs/` — curated canonical knowledge.
2. `machine/index.json` — routing metadata, not substantive truth.
3. `ai_readable/` — searchable source transcriptions and historical working documents.
4. `originals/` and legacy source folders — untouched source evidence.

The archive is authoritative about **what was said**. The canonical layer is authoritative about **what the project currently means**.

## Epistemic labels

Canonical material should use these labels when mechanism claims matter:

- **OBSERVED** — repeated behavior actually seen in experiments; still model/version dependent.
- **SUPPORTED** — consistent with established public technical principles and observed behavior.
- **HYPOTHESIS** — plausible causal account that needs controls/ablation.
- **PROCEDURAL** — an explicit rule imposed by our own controller/prompt/software; no claim about native model internals.
- **METAPHOR** — useful language for thinking or art direction, not a literal technical claim.
- **SPECULATIVE** — idea worth trying with little current evidence.
- **ARCHIVED / SUPERSEDED** — historically important but not current guidance.

Never upgrade a label because prose sounds confident.

## The project’s strongest shared principles

### 1. Mechanisms over adjectives
“Surreal,” “weird,” “psychedelic,” “glitch,” and “impossible” are weak unless attached to a rule that causes a structural consequence.

### 2. Keep competing constraints active
A contradiction is interesting only when the system cannot cheaply ignore one side. Design constraints with separate jurisdictions, anchors, references, or state rules so both sides keep exerting pressure.

### 3. Translate nouns into operations
A concept used as a waypoint or operator should be decomposed into what it **does**: rates, transitions, dependencies, feedback, conservation, topology, growth, decay, timing, spectral behavior, binding, etc. Avoid themed keyword soup.

### 4. Preserve path dependence
`A → C` should not necessarily equal `A → B → C`. If B mattered, it must leave a scar, state change, invariant, mutation, or changed interpretation carried into C.

### 5. Strange premises require disciplined consequences
The Temporary Minds library repeatedly uses this pattern: change one foundational rule, then reason more rigorously, not less rigorously.

### 6. Accidents are specimens
Interesting errors are not automatically defects to clean up. Record what preceded them, vary one condition, try to reproduce the family of artifact, and feed successful anomalies into later experiments when useful.

### 7. Separate creative utility from mechanism confidence
A technically wrong theory can still inspire excellent art. Keep the art; fix the explanation.

## Major systems

### Temporary Minds
A complete 26-mind procedural cognition library lives in the source layer. Canonical docs classify full minds, families, surgical minds, meta-generators, regulators, validators, and benchmark rules. A pasted mind changes **selection procedures and constraints**, not literal neural architecture.

### Semantic Manifold Game
A route-based creative instrument. “Latent space” is explicitly treated as a **useful lie**: the application builds an external navigable analogue from embeddings, explicit features, relationships, transformations, history, and state. The core artifact is `STATE + TRAJECTORY + HISTORY + CURRENT INTERPRETATION`, not merely a prompt.

### TOPOS-SRE / SRE controllers
External software/state-machine experiments that maintain persistent state, measure similarity/attractors, apply operators, increase decay, preserve symbol mappings, and feed the next legal instruction to a generative layer. These are controller dynamics, not secret model internals.

### DAVID operator research
The technical roundtable proposes operators for conditioning conflict, attention/binding stress, path-dependent iterative drift, positional encoding, VAE/compression, tokenization, and other possible failure surfaces. Treat operator explanations as hypotheses unless independently supported and tested. The roundtable’s strongest contribution is its experimental discipline: controls, ablations, dose-response sweeps, and failure criteria.

### Image math-slop practice
Strong recurring recipe: preserve identity anchors while a specific mathematical/physical process governs anatomy; translate abstraction into concrete material; make recording-medium degradation causal rather than a pasted-on filter; use iteration and feedback to preserve successful accidents.

### Suno/audio practice
Strong recurring recipe: assign musical dimensions separate jurisdictions (harmony, melody, rhythm, timbre, performance, invariant), then apply operators that make those systems negotiate without collapsing into random genre soup. Lyrics/brackets can function as control and phonetic material, not merely semantic content.

## How to add information correctly

Do not make one new canonical file per incoming PDF.

For each source:

1. Preserve the original.
2. Identify atomic claims, mechanisms, recipes, vocabulary, examples, open questions, and discarded ideas.
3. Route each atom to every canonical location where it belongs.
4. Add provenance links back to the source transcript/original.
5. Mark confidence/status.
6. Merge duplicates by mechanism, not wording.
7. Put untested but interesting material into backlog/idea-garden rather than presenting it as settled.
8. Update `machine/index.json` when you add a new canonical section.

## How to write canonical docs

- Prefer compact definitions plus consequences and links.
- Name the assumption attacked.
- State the operation precisely.
- State expected failure/artifact.
- Separate observable recipe from causal speculation.
- Include limitation/falsification where technical claims are involved.
- Link related mechanisms across media.
- Keep examples, but do not let one example become the definition.
- Preserve Merry’s vocabulary where it carries project meaning: slop, structured instability, scars, wreckage, route, organism, weird shittery. Do not turn the repo into corporate beige paste.

## Current overhaul status

The repository historically accumulated by document. The active overhaul is converting it to a **knowledge graph in prose form**: principles → mechanisms → media → cognitive systems → architectures → experiments → provenance, while keeping the complete source trail intact.
