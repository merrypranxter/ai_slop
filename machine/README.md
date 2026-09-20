# Machine-Readable Layer

This directory exists so software agents do not have to scrape prose just to discover the repository structure.

**Important:** these files are indexes and schemas. They are not a second competing source of truth. When a compact machine entry conflicts with a canonical explanation in `docs/`, prefer `docs/` and fix the machine file.

## Files

- `index.json` — top-level routing map, authority layers, canonical sections, major systems, and project rules.
- `operators.json` — compact lookup for the canonical cross-media/Temporary-Minds operator set.
- `david_protocols.json` — compact DAVID Protocol 01–20 hypothesis index with scope, family, and minimum test.
- `sources.json` — substantive source disposition and canonical-route lookup.
- `experiment.schema.json` — JSON Schema for structured experiment-run records.
- `semantic_fossil_run.schema.json` — minimum machine-readable run record for Semantic Fossil Instrument executions.
- `semantic_fossil_artifact.schema.json` — stored rendered-artifact record used by artifact-aware fossils.
- `semantic_fossil_transform_request.schema.json` — provider-neutral request packet for local or external generation adapters.
- `system_incubator.json` — compact status/next-step index for promising AI SLOP work that has **not** yet graduated into canonical systems or operators. Canonical explanation lives in `docs/09-backlog/system-incubator.md`.

`index.json` now also routes the live research-intake index, the wrong-use scout, its candidate queue, and the canonical **Stabilizer Inversion** research method. Candidate IDs stay in backlog/incubator until they graduate; do not stuff untested findings into `operators.json` just because a source paper is strong.

## Intended agent flow

1. Read `../AI_CONTEXT.md`.
2. Read `index.json` for routing.
3. Use the smallest relevant machine index to locate the canonical document.
4. Read the canonical document before making substantive claims or modifying the project.
5. Follow provenance back into `ai_readable/` only when source-level wording, history, or unresolved detail matters.
6. When work is intentionally deferred, parked, awaiting energy, or accumulating research before synthesis, check `system_incubator.json` and its canonical Markdown file before inventing a new plan.

## Authority

`docs/` = canonical current meaning.  
`machine/` = routing and compact structured summaries.  
`ai_readable/` = searchable source history.  
`originals/` = untouched source evidence.

Machine files should remain boring, stable, valid JSON, and easy to diff. Put explanation and nuance in `docs/`, not inside giant JSON blobs.
