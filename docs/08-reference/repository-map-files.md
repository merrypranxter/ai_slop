# Repository Map Files — Audit and Role

This file covers the small README/map/instruction documents that do not contain independent mechanisms but still matter for provenance, reading order, and maintenance. They are intentionally separated from the source-by-source mechanism audit so nobody has to wonder whether they were ignored.

## `ai_readable/art/README.md`
**Status:** ROUTING METADATA  
Maps seven art source files to their searchable transcriptions and explains that the normalized copies preserve originals.  
**Canonical role:** provenance/navigation only. The substantive art documents are audited individually in `source-audit.md`.

## `ai_readable/audio_suno/README.md`
**Status:** ROUTING METADATA  
Maps the Suno/audio source PDFs and the Smol Slop specimen into the seven numbered searchable files.  
**Canonical role:** provenance/navigation only.

## `ai_readable/general/README.md`
**Status:** ROUTING METADATA  
Maps the five general-foundation sources into the searchable layer.  
**Canonical role:** provenance/navigation only.

## `ai_readable/personality_prompts/README.md`
**Status:** IMPORTANT ROUTING / VERSION METADATA  
Provides the intended reading order for the Temporary Minds research lineage, source mapping, and an important deduplication note: the three Cognitive Mutation Laboratory source exports were verified as the same session, with the text export used as the canonical transcription body and the PDFs retained as duplicate source evidence.  
**Canonical role:** supports `docs/04-cognitive-systems/temporary-minds.md`, `docs/04-cognitive-systems/support-architecture.md`, and provenance/version history.

## `ai_readable/semantic_systems/README.md`
**Status:** IMPORTANT ROUTING METADATA  
Defines the intended reading order across Ghost/GLSL, direct-model intervention discussion, semantic-engineering development, controller architecture, Semantic Manifold design, and TOPOS-SRE material. It also records the exact source-to-transcription map and states that the supplied external URL was preserved rather than fetched during transcription.  
**Canonical role:** provenance and architecture-reading order.

## `ai_readable/video/README.md`
**Status:** EMPTY / PLACEHOLDER  
No standalone video source has been added yet. The current canonical video guidance is synthesized from cross-media sources, especially the general technical roundtable and visual process material.  
**Canonical role:** marks a genuine corpus gap rather than pretending a dedicated source exists.

## `originals/README.md`
**Status:** PRIMARY ARCHIVE MAP  
Maps the September 13 and September 16 intake originals to their searchable transcriptions and records duplicate/merged source relationships.  
**Canonical role:** archive provenance. Do not replace this with a shorter canonical summary; this file is useful evidence about where each original went.

## `new_to_be_processed_by_copilot_agent/readme.txt`
**Status:** ACTIVE INTAKE CONTRACT  
States the user’s core repository-maintenance instruction: preserve originals, do not leave information stranded in incoming PDFs/docs, and rearrange information by where it belongs rather than keeping document boundaries intact. It also records that processed batches are archived under `originals/`.

**Canonical implementation:** `docs/08-reference/intake-workflow.md` turns that instruction into a repeatable procedure. This intake readme should remain short and stable because it is the drop-folder instruction future agents are most likely to encounter first.

## Legacy folder readmes

The small legacy `art/readme.txt`, `general/readme.txt`, and `suno_slop/prompting/readme.txt` files are source-era folder labels. Their contents are represented by the numbered `01-*` transcriptions and by the mapping READMEs above. They contain no additional independent mechanism material.

## Why these stay separate from mechanism docs

These files answer **where did this come from, what order should I read it in, and how should a new intake be handled?** They do not answer **what mechanism should I use?**

Keeping that distinction prevents routing metadata from being mistaken for creative or technical authority while still satisfying the repo’s preservation rule: small documents count too.
