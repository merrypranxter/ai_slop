# Prompt Composition as a Compiler Layer

The repo contains hundreds of prompts, but the canonical design rule is that a prompt should be the **compiled representation of a mechanism**, not the mechanism itself.

## Build order

1. Define the target medium and actual controllable dimensions.
2. Choose the operator.
3. Choose invariants/anchors.
4. Translate the operator into consequences for those dimensions.
5. Add material/production/capture detail only where it supports the mechanism.
6. Add negative constraints only to block predictable escape routes.
7. Compile into the target model’s format.

## What not to do

Do not begin with a sack of adjectives and retroactively invent an explanation.

Do not assume technical words are magic tokens.

Do not bury the load-bearing rule under 2,000 words of persona theater unless the theater itself is the art experiment.

Do not claim a textual command literally changes hidden architecture.

## Prompt density

Dense prompts can be useful because they keep several constraints available, but density also causes condition dropout, ambiguity, or generic averaging. Treat length as an experimental variable, not a universal “more tokens = more slop” rule.

## Good prompt sentence shape

Prefer causal/instructional relations:

- “X remains fixed while Y changes according to Z.”
- “When threshold T is crossed, A loses property P and B inherits it.”
- “The same surface must be continuous with both foreground and background.”
- “Motif A is duplicated with a small phase offset; reinforcement/cancellation controls orchestration.”

Those do more work than “hyperdimensional fractal surreal impossible.”

## Reuse prompts correctly

When a prompt creates a useful accident:

- save the exact generation conditions;
- identify the smallest rule likely responsible;
- test variants;
- promote the rule into the mechanism registry if it survives;
- preserve the original prompt as a case study rather than treating it as sacred incantation.
