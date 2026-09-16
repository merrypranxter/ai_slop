# Semantic Manifold Game / SMC

## The useful lie

The source design specification contains one of the most important technical corrections in the repo: **“latent-space navigation” is a useful conversational lie**.

The application does not expose a model’s hidden neural manifold. It constructs an external operational analogue from things we can actually manipulate: semantic embeddings, explicit features, relations, history, transformations, distance functions, model-generated decompositions, and persistent state.

Keep the playful language. Keep the implementation honest.

## The real artifact

The primary object is not a prompt. It is roughly:

`STATE + TRAJECTORY + HISTORY + CURRENT INTERPRETATION`

A Suno prompt, visual prompt, shader specification, or other medium-specific instruction is a **compiled projection** of that object.

## Foundational rule: path dependence

`A → C` must be allowed to differ from `A → B → C`.

Passing through B should change the transported state through operational consequences. A destination is not merely a theme added to the prompt; it is a region exerting transformation pressure on the arriving organism.

## State model

The earlier SMC-1 music prototype uses explicit axes such as:

- tension;
- density;
- entropy;
- spectral position;
- temporal activity;
- valence.

The larger design spec expands state beyond a six-number vector. Canonical implementations should be hybrid and retain:

- semantic representation;
- structural traits;
- medium-specific traits;
- invariants;
- scars;
- route history;
- uncertainty;
- current interpretation;
- provenance of transformations.

Do not force everything meaningful into one fake-precise scalar.

## Concept transduction

A concept such as TARDIGRADE, THIN-FILM INTERFERENCE, BISOUS, RABIES, STRING BIKINI, or DÉJÀ VU should not enter as thematic garnish.

Pipeline:

`concept → actual behaviors/relations → target-medium affordances → candidate state changes → selected transformation`

Example from the design logic: thin-film interference is not merely “iridescent.” Multiple reflected waves interact; tiny thickness differences alter phase; wavelengths reinforce/cancel; viewing condition changes apparent output. Those relations can become motif offsets, cancellation/reinforcement, spectral filtering, or parameter-sensitive orchestration.

## Navigation grammar

The design spec defines a large family of movement verbs, including:

- direct transit;
- midpoint;
- geodesic;
- scenic route / via;
- parallel transport;
- orbit / hover;
- overshoot / trajectory extension;
- collision;
- slingshot;
- inversion;
- swan dive;
- path continuation.

These are different operations, not colorful synonyms for “blend X and Y.”

## Distance metrics

Changing the ruler changes the neighborhood. Metrics may include semantic, failure, causal, energy, viscosity-like, bureaucratic-friction, synthetic-sensory, or other explicitly defined relations.

Temporary Mind #15 provides the clean general architecture for alien metrics and turnover.

## Scars and recoil

The route should be able to carry:

- permanent variable shifts;
- transformed invariants;
- recall scars;
- changed interpretation of earlier waypoints;
- accumulated degradation;
- accidental structures promoted to persistent features.

Relevant Temporary Minds: #23 Recall Mutation and #25 Semantic Recoil.

## UI philosophy

The design spec argues for two surfaces:

- **PLAY** — natural casual commands; the player drives without forms everywhere.
- **LAB** — explicit state, route, metrics, transformations, diagnostics, comparisons.

The application should infer a structured operation from casual language while allowing later inspection/editing.

## Ownership rule

Persistent state belongs to software, not to vague conversational memory. The route, ledger, current state, metrics, and saved trajectories should be first-class application data. Models are transformation/interpretation components inside the instrument.

Primary source: `ai_readable/semantic_systems/08-semantic-manifold-game-design-specification-v0.1.md`.
