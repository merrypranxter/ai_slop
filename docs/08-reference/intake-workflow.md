# Source Intake Workflow

This is the maintenance procedure for turning a new dump of PDFs, docs, chats, experiments, or notes into usable repository knowledge **without flattening the source or duplicating the old mess**.

## The rule

**Do not organize by document. Organize by information function.**

A single incoming document may contribute to philosophy, operators, media practice, architectures, experiment design, glossary terms, provenance, and backlog at the same time. Split it accordingly.

Likewise, ten documents may contain versions of the same mechanism. Merge the mechanism canonically while preserving every source in the archive.

## Intake sequence

### 1. Preserve the original

Put the untouched source in the dated `originals/copilot-intake-YYYY-MM-DD/` archive. Do not rewrite, sanitize, or overwrite it.

### 2. Create or verify a searchable source copy

Place the searchable transcription or normalized text under the appropriate `ai_readable/` section. Preserve enough source identity to map back to the original.

A transcription is **not** canonicalization. It only makes the source searchable.

### 3. Atomize the source

Extract information into functional atoms such as:

- principle;
- operator/mechanism;
- executable prompt or recipe;
- media-specific implementation;
- software architecture;
- experimental method;
- terminology;
- example/case study;
- open question;
- speculative hypothesis;
- correction/supersession;
- archive-only rhetoric or flavor.

Do not assume one paragraph has only one destination.

### 4. Assign epistemic status

Use the project labels from `docs/01-principles/epistemic-status.md`.

Especially separate:

- a procedure we explicitly impose;
- an observed output pattern;
- a technical mechanism claim;
- a metaphor;
- a speculative explanation;
- historical theater.

A confident tone in a source is not evidence.

### 5. Route every reusable atom

Possible destinations include:

- `docs/01-principles/` — project laws and design models;
- `docs/02-mechanisms/` — reusable operators and technical hypotheses;
- `docs/03-media/` — image/video/audio implementation;
- `docs/04-cognitive-systems/` — Temporary Minds and support systems;
- `docs/05-architectures/` — software/state/model architecture;
- `docs/06-experimentation/` — controls, logging, benchmarks, reproducibility;
- `docs/07-prompts/` — compiled prompt patterns;
- `docs/08-reference/` — glossary, provenance, palettes, source disposition;
- `docs/09-backlog/` — unresolved but interesting material.

If the information legitimately belongs in five places, route it to five places. Prefer concise cross-links over copy-pasting the same long explanation.

### 6. Merge by mechanism, not wording

Before creating a new canonical mechanism, search for an existing one that performs the same transformation.

Possible outcomes:

- **NEW** — genuinely distinct;
- **MERGED** — same core operation under another name;
- **FAMILY MEMBER** — useful specialized version;
- **SUPERSEDED** — replaced by a better formulation;
- **DEMOTED** — useful as a surgical operator, not a whole system;
- **FLAVOR ONLY** — generates framing/aesthetic pressure, not a mechanism;
- **ARCHIVE ONLY** — preserved but not operationalized.

### 7. Record provenance and disposition

Update:

- `docs/08-reference/source-audit.md` — what the source is for and where it went;
- `docs/08-reference/provenance-map.md` — which major canonical ideas it supports;
- `machine/sources.json` — machine-readable routing/status if a new substantive source was added.

### 8. Update machine indexes

If the intake adds or changes canonical systems, update the relevant machine-readable files:

- `machine/index.json`;
- `machine/operators.json`;
- `machine/david_protocols.json` when applicable;
- `machine/experiment.schema.json` only when the run-record contract itself changes.

Machine files route; `docs/` remains authoritative for meaning and caveats.

### 9. Run the bullshit check

Before calling intake complete, ask:

- Did an AI-generated source claim access to hidden weights/activations without instrumentation?
- Did theatrical jailbreak language get mistaken for an actual mechanism?
- Did a scientific metaphor become a factual causal claim?
- Did an exact threshold from one proposed experiment get generalized universally?
- Did a persona get mistaken for a cognitive procedure?
- Did a decorative theme get mistaken for concept transduction?
- Did we preserve a cool result while correcting a weak explanation?

If yes, fix the canonical layer; leave the historical source intact.

### 10. Close the intake

An intake is complete when:

- the original is preserved;
- searchable source text exists;
- every substantive document has an explicit disposition;
- reusable information has a canonical destination;
- competing/superseded claims are labeled;
- machine routing is current;
- no new giant orphan transcription is masquerading as organization.

## What not to do

Do not delete sources merely because they duplicate a newer transcription. Do not create a new canonical folder named after every PDF. Do not rewrite the entire source into one summary and discard the internal structure. Do not assume every source idea deserves promotion.

The archive keeps the evolutionary mess. The canonical layer keeps the machinery.
