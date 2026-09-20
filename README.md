```text
??????????????????????????????????????????????????????????????????????????????
??                                                                          ??
??      ?????       ????????      ???????   ??        ???????   ???????     ??
??     ??   ??         ??        ??         ??       ??   ??   ??   ??     ??
??     ???????         ??         ??????    ??       ??   ??   ???????     ??
??     ??   ??         ??              ??   ??       ??   ??   ??          ??
??     ??   ??      ????????      ???????   ???????   ???????   ??          ??
??                                                                          ??
??              S T R U C T U R E D   I N S T A B I L I T Y               ??
??                    W E I R D N E S S   W I T H   R E C E I P T S        ??
??                                                                          ??
??????????????????????????????????????????????????????????????????????????????
```

# AI SLOP
## Structured Instability Laboratory

> `[ SIGNAL ACQUIRED :: GENERATIVE FAILURE UNDER CONTROLLED CONDITIONS ]`

![status](https://img.shields.io/badge/status-active%20research-ff1493)
![media](https://img.shields.io/badge/media-image%20%7C%20video%20%7C%20audio%20%7C%20text-7b2cff)
![method](https://img.shields.io/badge/method-controls%20%7C%20ablations%20%7C%20dose%20sweeps-00cfe8)
![ethos](https://img.shields.io/badge/ethos-weirdness%20with%20receipts-b6ff00)

> **A generative-model research/art lab for controlled failure, path dependence, cross-media mutation, stateful creative systems, and reproducible weirdness.**

This repository started from the extremely scientific question **“what weird shit happens if I make the model solve the wrong problem?”** and has grown into a fairly serious experimental framework.

It is **not a prompt dump** and it is not a claim that generative models are secretly haunted.

AI SLOP studies what happens when a generative system is given constraints, histories, representations, or control signals that cannot all be satisfied through the usual easy shortcut — and then treats the model’s repair attempt, compromise, drift, scar, mutation, or artifact as the specimen.

The north star is:

> **What problem can we give a generative system such that its attempt to solve the problem becomes the artwork?**

---

## What “AI slop” means here

The phrase is used affectionately for **caused weirdness**:

- binding failures that stay structured;
- identity preserved under hostile geometry;
- path-dependent scars;
- recursive artifacts that fossilize across passes;
- contradictory musical jurisdictions;
- temporal drift and correspondence failure;
- semantic near-misses that obey a new rule;
- codec, attention, guidance, and controller failures that can be measured instead of merely described.

Random garbage is easy. The interesting region is where the system is still trying to obey enough of the task that its failure has anatomy.

The basic loop is:

<code>ordinary assumption -> precise intervention -> competing pressures -> attempted resolution -> emergent artifact -> measurement -> ablation -> preserve / mutate / reject</code>

---

## Why this is a research repo, not just “lol prompts”

A cool output is not automatically evidence for the story we tell about it.

The project separates **creative utility** from **mechanism confidence**. Technical ideas are expected to survive ordinary baselines, isolated-variable tests, repeated runs, dose-response sweeps, ablations, matched controls or sham interventions, path/history logging, failure recording, and falsification criteria.

If the theory is wrong but the artifact fucking rules, the artifact can stay. The explanation gets demoted.

Canonical method: [experimental method](docs/06-experimentation/experimental-method.md).

---

## Current live state

| Track | Status | What exists now |
|---|---|---|
| **Semantic Fossil Instrument** | **GRADUATED / runnable** | External-state path-dependence system with active state, immutable route ancestry, causal fossil ledgers, checkpoints, reset ablations, deterministic replay, archives, and creative compilers. |
| **Perceptual Wound -> Silent Scar** | **ACTIVE experiment** | Matched intervention/recovery harnesses testing whether transient injury leaves functional history detectable under a standardized second injury. |
| **Temporary Minds** | **CANONICAL library** | 26 procedural cognition systems plus validators, regulators, family generators, merge/discard history, and stress tests. |
| **Semantic Manifold / SRE / TOPOS** | **ARCHITECTURE layer** | External state, route ledgers, semantic navigation, attractor/decay logic, explicit controllers, and GLSL state visualization. |
| **DAVID mechanism research** | **HYPOTHESIS registry** | 20 technical protocols plus broader failure-surface work across conditioning, iteration, binding, tokenization, codecs, guidance, reference pressure, and local-model intervention. |
| **Wrong-Use / Stabilizer Inversion** | **NEW canonical research method** | Mine reliability/stabilization papers for the exact failures their fixes suppress; inherit the measurements and ablations, then test controlled inversions. |
| **Research incubator** | **RESEARCH-ACCUMULATING** | Candidate systems and mechanism clusters are deliberately preserved without pretending every new paper deserves a new operator. |

Live board: [system incubator](docs/09-backlog/system-incubator.md)  
Research cycles: [research intake index](docs/08-reference/research-intake-index.md)

---

## The newest method: Stabilizer Inversion

A surprisingly productive research pattern emerged from the September 20 wrong-use scout:

> **Every anti-drift device is documented by what it suppresses.**

Reliability papers often do the boring experimental work for us: they identify the failure, measure it, find the threshold, publish the ablation, and build the fix.

AI SLOP keeps the instrumentation and asks a different question:

<code>documented failure -> stabilizer -> measurement -> ablation -> controlled inversion -> dose sweep -> artifact family</code>

The first scout surfaced candidates including cyclic-denoising attractor cartography, attention-sink amputation / parking-lot occupation, frequency-band guidance jurisdictions, video anchor inversion and controlled error accumulation, dead-code injection / scheduled codec vocabulary mutation, induction-head lesion and positional arbitration shifts, semantic entropy as breeding pressure, contradictory steering-vector stacks, and loss-barrier-verified model merging.

These are **not silently canonized as proven operators**. They live in the backlog until tested.

Method: [Stabilizer Inversion / wrong-use research](docs/06-experimentation/stabilizer-inversion-wrong-use-research.md)  
Latest scout: [2026-09-20 wrong-use scout](docs/08-reference/research-cycle-2026-09-20-wrong-use-scout.md)  
Candidate queue: [wrong-use candidate mechanisms](docs/09-backlog/candidate-mechanisms-2026-09-20-wrong-use-scout.md)

---

## Main research tracks

### Image

Identity anchors, topology, anatomy-as-process, material anchoring, classifier-free-guidance failure surfaces, iterative image-to-image drift, cyclic denoising, reference-vs-transformation pressure, and recording-medium artifacts that arise from an actual degradation chain rather than a decorative “VHS filter.”

Start with [image methods](docs/03-media/image.md).

### Video

Temporal identity, correspondence failure, object permanence, topology through time, chunk boundaries, accumulated generation error, history corruption, anchor placement, occlusion/reappearance, and stateful interventions.

Start with [video methods](docs/03-media/video.md).

### Audio / Suno

Separated musical jurisdictions, tuning/meter/timbre conflict, phonetic engines, route-based composition, codec hierarchies, recurrent mutation, and the question of which musical layer gives way first when incompatible priors remain active.

Start with [audio / Suno methods](docs/03-media/audio-suno.md).

### Text / local models

Temporary cognitive systems, attention/position effects, circuit lesions, semantic entropy, steering, context arbitration, symbolic compression, external controllers, and local/open-weight experiments where the intervention can actually be instrumented.

Start with [Temporary Minds](docs/04-cognitive-systems/temporary-minds.md) and [local-model interventions](docs/05-architectures/local-model-interventions.md).

### Stateful creative systems

A major theme of the repo is that the interesting artifact is often not one output. It is:

<code>STATE + TRAJECTORY + HISTORY + SCARS + CURRENT INTERPRETATION</code>

That is where the Semantic Manifold, SRE/TOPOS, Perceptual Wound work, and Semantic Fossil Instrument connect.

---

## Core machinery

The cross-media operator registry contains reusable operations such as:

**Primitive Deletion · Error Axiomatization · Property Unbundling · Alien Distance Metrics · Synthetic Transducers · Synthetic Valence · Minority-Axis Sovereignty · Separated Jurisdictions · Anchor + Mutation Field · Recall Mutation · Semantic Recoil · Descendant Fitness · Forced Aliasing · Meta-Genomic Speciation · Material Anchoring · Causal Artifact Chains · Recursive Artifact Fossilization · Attractor Lock -> Perturb**

The point is not the names. Every operator must reduce to an actual transition rule.

Registry: [cross-media operator registry](docs/02-mechanisms/operator-registry.md)  
Machine-readable lookup: [machine/operators.json](machine/operators.json)

---

## Epistemic discipline

| Label | Meaning |
|---|---|
| **OBSERVED** | behavior actually seen in repeated experiments; still model/version dependent |
| **SUPPORTED** | consistent with strong public technical evidence and observed behavior |
| **HYPOTHESIS** | plausible causal account that still needs controls/ablation |
| **PROCEDURAL** | behavior explicitly imposed by our own prompt/controller/software |
| **METAPHOR** | useful conceptual language, not a literal architecture claim |
| **SPECULATIVE** | worth trying, little current evidence |
| **ARCHIVED / SUPERSEDED** | historically useful, not current guidance |

This repo does **not** treat “latent space” as a literal hidden world a prompt can freely walk through. It does not claim prompts directly rewrite weights or secret internal safety layers. It does not treat hallucination as proof of a model’s “true self.”

The archive contains old theatrical language that says shit like that because the project history is preserved. The canonical layer cleans up the causal claims without sterilizing the creative ideas.

---

## Repository anatomy

| Path | Job |
|---|---|
| [AI_CONTEXT.md](AI_CONTEXT.md) | Fast orientation and operating rules for any AI/collaborator entering the repo |
| [docs/](docs/) | Canonical curated knowledge: principles -> mechanisms -> media -> systems -> experiments -> references/backlog |
| [machine/](machine/) | Machine-readable routing, registries, schemas, and incubator state |
| [experiments/](experiments/) | Runnable experiment harnesses |
| [ai_readable/](ai_readable/) | Searchable source transcriptions/digests |
| [originals/](originals/) | Preserved original source files |
| [art/](art/) / [general/](general/) / [suno_slop/](suno_slop/) | Legacy source organization retained for provenance |
| [new_to_be_processed_by_copilot_agent/](new_to_be_processed_by_copilot_agent/) | Intake chute for new material |

The rule is: **a source is evidence, not a folder destiny.** One PDF can feed ten canonical files; ten PDFs can collapse into one mechanism.

---

## Start here

**If you are a human:**  
Read [the project map](docs/00-project-map.md), then the [operator registry](docs/02-mechanisms/operator-registry.md), then whichever media/system branch interests you.

**If you are an AI or coding agent:**  
Read [AI_CONTEXT.md](AI_CONTEXT.md) first. It contains the hierarchy, epistemic rules, routing logic, and the “do not turn this back into document soup” warning.

**If you want runnable work:**  
Start with [experiments/semantic_fossil/](experiments/semantic_fossil/) and [experiments/perceptual_wound/](experiments/perceptual_wound/).

**If you want the current research frontier:**  
Open [research-intake-index.md](docs/08-reference/research-intake-index.md) and [system-incubator.md](docs/09-backlog/system-incubator.md).

---

## Adding new research

New material should enter through the intake workflow rather than becoming another orphaned mega-document.

Preserve the source, create/verify searchable text, extract atomic claims and mechanisms, route them into the canonical structure, record provenance, mark epistemic status, merge duplicates by **mechanism rather than wording**, and park untested ideas in the incubator.

Workflow: [intake workflow](docs/08-reference/intake-workflow.md)  
Source audit: [source audit](docs/08-reference/source-audit.md)

---

## Suggested GitHub About metadata

**Description**

> Experimental generative-AI lab for structured instability: controlled failure, path dependence, cross-media operators, stateful systems, and reproducible weirdness.

**Topics**

<code>generative-ai</code> · <code>generative-art</code> · <code>computational-creativity</code> · <code>ai-art</code> · <code>ai-music</code> · <code>generative-music</code> · <code>video-generation</code> · <code>diffusion-models</code> · <code>transformers</code> · <code>multimodal-ai</code> · <code>mechanistic-interpretability</code> · <code>model-steering</code> · <code>model-behavior</code> · <code>prompt-engineering</code> · <code>creative-coding</code> · <code>experimental-ai</code> · <code>quality-diversity</code> · <code>state-machines</code> · <code>human-ai-collaboration</code> · <code>reproducible-research</code>

---

## One sentence version

**AI SLOP is a laboratory for making generative systems fail in structured, measurable, reusable ways — then turning the wreckage into art, instruments, and better questions.**
