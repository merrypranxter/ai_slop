# AI SLOP Research Scouting - Integration Notes
## 2026-09-19 checkpoint

**Source basis:** `AI-SLOP-research-cycle-2026-09-19.pdf`, compared against `merrypranxter/ai_slop` at commit `63e887551e6e19dab35e3b287a2226e91f1d0e17`.

These are routing notes for the project, not a replacement for the full scouting report or its living ledger.

## What changed

This cycle produced **11 selected findings and zero new canonical operators**. The useful delta is concrete implementations, validators, regulators, and media adapters that make existing AI SLOP machinery executable, measurable, or harder to fool.

Do not inflate the ontology prematurely:

- **Protocol Speciation** remains a candidate procedural design under Symbolic Compression + Token Tax + Separated Jurisdictions.
- **Protocol-Mismatch Collective** remains a candidate procedural design under Separated Jurisdictions + Forced Aliasing.
- **Silent Scar** is an experiment/validation label under Hysteretic Transformation / Artifact Fossilization, not a new memory operator.

## Highest-priority synthesis

### Perceptual Wound -> Silent Scar -> Behavior Archive

1. **Lenia sensory occlusion / Perceptual Wound**
   - Change what an organism can sense without deleting its physical state.
   - Maintain separate physical-state and perceptual-availability fields.
   - First comparison: no mask vs state erasure vs unnormalized mask vs normalized sensory occlusion.
   - Log heading, position, connected components, spatial overlap, and recovery.
   - Evidence/utility: **E4 / U5**.
   - Public simulation repository exists; reproduction not yet performed.

2. **NCA attractor analysis / Silent Scar**
   - Visible recovery is not enough.
   - Save full-state trajectories before and after perturbation, then apply the same standardized second injury.
   - A scar claim survives only if future response differs from matched uninjured controls after controlling for visible-state differences.
   - Evidence/utility: **E4 / U5**.
   - Public experiment notebooks/model material exist.

3. **AutoQD / Behavior Archive**
   - Archive artifacts by how they behave under intervention, not only by visual embedding.
   - Compare image embeddings, hand-designed recovery descriptors, and learned intervention-response descriptors.
   - Keep quality and behavioral novelty as separate axes.
   - Preserve history/scar state whenever it changes future behavior.
   - Evidence/utility: **E4 / U5** on tested control tasks; transfer-to-art remains only a hypothesis.
   - Public implementation exists.

**Project consequence:** this is the first chain from the cycle worth building. It operationalizes the existing idea that an artifact can "remember the wound" without promoting a new mystical memory concept.

## Second strong synthesis

### Protocol evolution -> codebook mismatch -> transmission test

- **GlossoGen**
  - Private information + character-budget pressure + optional between-round protocol negotiation.
  - Replay/forks/agent swaps allow newcomer transmission tests.
  - Gibberish is not success unless it preserves coordination/generalization.
  - Evidence/utility: **E3 / U5**.
  - MIT-licensed platform with logs, swaps/forks, tests, and documentation.

- **Communication-heterogeneous NCA**
  - Agents can share the same objective while interpreting neighbor messages through mismatched codebooks.
  - This creates coordination conflict without competing preferences.
  - Important confounds: interpolated permutations may change message amplitude; vote inversion must be ablated separately.
  - Evidence/utility: **E3 / U5**.
  - Architecture/equations available; runnable implementation not yet established.

**Proposed sequence:** let a compact protocol evolve because it is useful, damage the translation boundary, then test whether a replacement partner can learn the mutated protocol.

## The 11 selected findings

| Finding | AI SLOP role | Evidence / utility | Immediate status |
|---|---|---:|---|
| Lenia sensory occlusion | Perception-only wound | E4 / U5 | **Build first** |
| GlossoGen | Pressure-driven private protocol + transmission | E3 / U5 | Candidate Protocol Speciation |
| MusicLayout | Editable intermediate temporal score before rendering | E3 / U5 | Music adapter; checkpoint availability unclear |
| Latent-Control Heads (LatCH) | Measurable latent audio target curves | E3 / U5 | Audio adapter; full release not established |
| Diff2Mix | Explicit per-track effects/production parameters | E3 / U4 | Mixing adapter; full checkpoint unclear |
| NCA attractor analysis | Hidden-dynamics recovery / Silent Scar | E4 / U5 | **Build early** |
| Communication-heterogeneous NCA | Shared goal + mismatched codebooks | E3 / U5 | Candidate Protocol-Mismatch Collective |
| AutoQD | Behavioral descriptor learning for archives | E4 / U5 | **Build with Lenia** |
| SAE random-baseline sanity checks | Learned-vs-random interpretability controls | E4 / U5 as hygiene | Validator, not generator |
| Stable Video Infinity | Generator-specific error bank | E4 / U4 | Regulator |
| IDAttn | Timed isolation and reunion of attention jurisdictions | E3 / U4 | Implementation lead |

## Media adapters worth keeping

### MusicLayout
Compile temporal laws into an inspectable segment/family schema before audio exists. Keep the schema as causal record. Test original vs shuffled vs single-field-edited vs deliberately conflicting layouts. Score temporal adherence separately from musical preference.

### LatCH
Translate a mathematical/living-system trajectory into a low-dimensional target curve such as intensity or beat behavior, then guide latent audio generation toward it. Start with a scalar intensity curve before dense pitch constraints.

### Diff2Mix
Separate composition from production behavior. Treat a reference mix as an explicit effects-parameter proposal, mutate selected knobs while preserving stems, and keep the parameter log.

## Validators and regulators

### SAE random-basis controls
A semantically interpretable-looking direction is not automatically a native concept. Blind-rate learned and random directions at matched perturbation norms, then separately test target behavior and collateral damage. A creatively useful knob may survive even if the semantic explanation does not.

### Stable Video Infinity error banks
Use the generator's own rollout failures as the repair distribution instead of only generic corruptions. For AI SLOP, explicitly separate:
- failures to repair,
- failures to preserve as scars,
- and "stability" caused by freezing rather than successful motion.

### IDAttn
Separated Jurisdictions gains a concrete implementation question: **when should isolated regions communicate again?** Compare global prompting, permanent isolation, and scheduled isolation/reunion. Measure local obedience, non-target change, and global coherence separately.

## Repository routing

### ADD
- perception-only perturbations;
- full-state recovery / second-probe tests;
- behavior-sensitive archive descriptors;
- explicit music-layout, latent-control, and effects-parameter adapters;
- model-specific error-bank regulator;
- timed isolation/reunion implementation lead.

### UPDATE
- Topic 01 mechanistic-interpretability docs with learned-vs-random SAE controls;
- Topic 02 attention-routing docs with edit-occurrence vs edit-correctness distinctions;
- attractor/memory docs with full-state dynamics and second-probe assays;
- video docs with identity, motion, and freezing tradeoffs.

### MERGE
- failure-profile proximity into Alien Distance Metric examples;
- Protocol Speciation into Symbolic Compression + Token Tax + Separated Jurisdictions;
- Protocol-Mismatch Collective into Separated Jurisdictions + Forced Aliasing;
- Silent Scar into Hysteretic Transformation / Artifact Fossilization as a validation protocol;
- ASAL++ / AutoQD into existing search-selection architecture, keeping goal generation and descriptor learning distinct.

### ARCHIVE / REJECT
Do not promote:
- "infinite video never drifts";
- "visual recovery proves full recovery";
- "a named SAE feature proves a native concept";
- "emergent gibberish proves a language";
- intrinsic superiority of a prompt language without controlled evidence;
- anthropomorphic interpretations of simulated avoidance;
- new labels whose only novelty is metaphor, repo naming, or a port.

## Proposed build order from this cycle

1. **Lenia occlusion prototype**
2. **Silent Scar assay**
3. **AutoQD behavior archive**
4. **Protocol evolution experiment**
5. **Protocol mismatch experiment**
6. **Music/audio adapters after the core works**

## Release blockers / unresolved questions

- MusicLayout trained weights.
- LatCH released control heads.
- Full Diff2Mix release/checkpoint.
- IDAttn implementation/checkpoint.
- SAE evaluation harness.
- Protocol mismatch causal confounds.
- Spatial blindness in sorted-profile recovery metrics.
- Shuffled-layout gains that weaken naive adherence claims.
- Motion-vs-freezing confounds in video consistency metrics.
- Recovery of the missing scouting skill and earlier canonical research ledger.

## Graduation rule for future scouting

A finding should move through:

**candidate -> implementation -> supported project mechanism -> new operator**

- Candidate -> implementation: runnable intervention with recorded configuration.
- Implementation -> supported mechanism: matched comparison attributing the effect to the intervention.
- Supported mechanism -> new operator: capability cannot be represented adequately as an implementation, composition, regulator, or validator of existing machinery.
- Any status -> revised/archived: preserve the evidence and the reason; never erase negative results.

## Compact working memory

- Perceptual wounds can leave behavioral scars.
- Archive behavior, not just appearance.
- Private languages must earn their weirdness through coordination and transmission.
- Interpretability knobs need stupid baselines.
- Repair and scar preservation are separate objectives.
- Separated jurisdictions need permeability schedules.

**Bottom line:** do not build eleven new gods. Build the **perceptual-wound / silent-scar / behavior-archive machine**, then let the evidence decide what deserves promotion.
