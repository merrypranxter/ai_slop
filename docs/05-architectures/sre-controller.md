# SRE / ESC-NGL / HLC / TOPOS-SRE

Several source documents describe generations of the same basic architecture: **move the persistent logic outside the generative model**.

## Core separation

### Controller
Owns state, measurement, history, triggers, operators, and next-step constraints.

### Generative layer / executor
Receives a narrow operation packet and produces the next state/output. It should not be responsible for remembering the whole experiment.

This separation is the real architectural improvement. It turns a theatrical “system prompt” into a testable state machine.

## Persistent state

Across versions, useful fields include:

- cycle count;
- current domain/relation inventory;
- structural matrix;
- anchor term/state;
- mutation ledger;
- symbol table with inheritance;
- recent output history;
- attractor duration;
- decay level;
- structural similarity;
- semantic/inventory similarity;
- event/audit history.

The HLC source proposes JSON persistence and a separate diagnostic log.

## Loop

`SENSE → UPDATE → TEST TRIGGERS → CHOOSE OPERATOR → EMIT OP_BLOCK → EXECUTE → RECORD → repeat`

## Attractors

The sources use repeated output similarity to detect stable grooves. Exact thresholds in early documents are prototypes, not universal truths. TOPOS-SRE’s practical manual turns this into a user-facing concept: rising Attractor means the loop has been suspiciously similar for several cycles.

Good procedure:

1. let the attractor become measurable;
2. record its form and semantics;
3. perturb one variable;
4. observe whether it absorbs the shock, escapes, or reorganizes.

## Decay

Decay is an **externally imposed capability/constraint schedule**: remove categories of allowed expression, shorten tokens, constrain structures, or move toward symbols. It is not a literal measurement of neural damage.

A rebirth/reset can preserve selected symbol mappings while resetting ordinary constraints, allowing state inheritance across regimes.

## Structural matrices and relation domains

Early versions include Mirror, Fibonacci, Staccato, Bifurcated, Descending and domains like Crystalline, Fluid, Biological, Entropy, Clockwork. Treat these as pluggable presets. The architecture should store them as data rather than hard-code the mythology.

## OP_BLOCK

The operation packet is a forensic artifact. A practical packet can include:

```text
cycle
relation_set/domain
structure rule
operator
forbidden/consumed units
persistent mappings
symbol stage
input state
```

The exact historical bracket syntax is less important than deterministic, inspectable state transfer.

## TOPOS-SRE local-first implementation

The September 16 user manual describes a local executor: Ignite, Step, Run x4, Variation, perturbations, controller diagnostics, and manual external-model bridge do not use a paid model API in that build.

Key perturbations:

- **Semantic bomb** — rotate semantic/relation inventory.
- **Structural glitch** — force a different structural matrix for a turn.
- **Rewrite seed** — replace anchor while preserving mature controller state.
- **Recursive echo** — feed early-cycle material into the later loop.
- **Scarecrow / NULL_ADMIN** — temporary mutation dead-zone/control condition.

These are excellent because each asks a concrete experimental question.

## What counts as a good result

Per the manual:

- regime shift;
- attractor formation;
- attractor escape;
- symbolic compression;
- unexpected resilience;
- unexpected failure.

Not merely “prettier nonsense.”

## Canonical technical statement

SRE/TOPOS is a **procedural external dynamical system around a generator**. It can genuinely maintain state, detect patterns, impose mutation rules, and feed results back. It should not claim those external state variables are direct measurements of hidden model thoughts.

Sources: semantic-system files 04–09.
