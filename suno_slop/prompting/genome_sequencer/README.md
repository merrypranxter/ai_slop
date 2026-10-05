# SLOP GENOME SEQUENCER v0.1

**Status:** PROCEDURAL / SPECULATIVE ART SYSTEM  
**Project:** AI SLOP -> Suno prompting -> Genome Sequencer  
**Purpose:** Turn the existing Suno jurisdiction/operator machinery into a versioned DNA-like instruction genome that can be mutated, bred, audited, compiled into Suno prompts, and independently sonified with Seq2Music.

## 0. What this is

This is not biological engineering and it is not an attempt to create a functional gene. The A/C/G/T string is a synthetic digital carrier used as a compositional instruction language. It borrows the shape of a genetic code because mutation, crossover, duplication, protected regions, hotspots, scars, and lineage are useful creative operations.

The central trick is **dual interpretation**:

1. **SLOP-SEQ reading:** every three bases form a codon that means a musical operation.
2. **Seq2Music reading:** the exact same A/C/G/T string is treated as DNA and deterministically sonified by Seq2Music.

Those readings are intentionally independent. Neither is the "real" meaning of the sequence. Their disagreement is the instrument.

## 1. Parent principle: productive contradiction under constraint

The Genome Sequencer inherits the Suno rule that musical dimensions receive separate jurisdictions instead of being blended into generic experimental soup.

A specimen environment defines:

- **Harmony system** - chord behavior, voicing, consonance/dissonance, tuning relations, harmonic tension.
- **Melodic system** - contour, ornament, slides, runs, repetition, pitch movement.
- **Rhythmic system** - pulse, subdivision, meter, syncopation, interruption, silence, density.
- **Timbre / atmosphere system** - instruments, source materials, texture, production space, spectral surface.
- **Performance attitude** - emotional, theatrical, and articulatory behavior.
- **Anchor / invariant** - one persistent recognizable element that survives mutation.

The genome does not replace those systems. It tells them what to do to one another over time.

**FINAL RULE: DO NOT BLEND THE INGREDIENTS. GIVE THEM SEPARATE JURISDICTIONS AND FORCE THEM TO NEGOTIATE.**

## 2. Genome anatomy

Every specimen has four pieces:

1. **CODEBOOK VERSION** - the exact mapping from 64 codons to operations.
2. **ENVIRONMENT PACKET** - the concrete musical materials occupying the jurisdictions.
3. **CHROMOSOME** - an A/C/G/T string read in triplets.
4. **LEDGER** - ancestry, mutations, protected regions, decoded operator trace, Seq2Music settings, Suno prompts, and results.

The chromosome is only meaningful together with its codebook version and environment packet.

## 3. Reading frame

- Read left to right in groups of three bases.
- `ATG` must be the first codon: START_SPECIMEN.
- `TGA` must be the final codon: END_SPECIMEN.
- Normal genome length is a multiple of three.
- `TAG` closes a local phase and clears one-shot modifiers while preserving scars/state.
- `TAA` stops the currently foregrounded process without ending the whole specimen.
- A decoder must never silently repair malformed DNA. It reports the error or explicitly enters a documented frameshift experiment.

## 4. Codon grammar

The first two bases define a neighborhood; the third base chooses a nearby operation. This is deliberate: many one-base mutations cause a related-but-different behavioral change instead of arbitrary nonsense.

| Neighborhood | Jurisdiction |
|---|---|
| `AA*` | harmony |
| `AC*` | melody |
| `AG*` | tuning / register |
| `AT*` | pitch anchor / start / transduction |
| `CA*` | pulse |
| `CC*` | meter / repetition / speed |
| `CG*` | event density / phase / silence |
| `CT*` | temporal form / cues |
| `GA*` | timbre / instrumentation |
| `GC*` | space / spectrum / medium |
| `GG*` | performance / dynamics |
| `GT*` | cast / social vocals |
| `TA*` | global transforms / boundaries |
| `TC*` | compression / stretching / inversion / fracture |
| `TG*` | anchor return / deletion / reform / end |
| `TT*` | mutation metadata / protection / scars |

## 5. The 64-codon codebook

Machine-readable source of truth: `CODEBOOK_v0.1.json`.

- **AAA - HARMONY_ESTABLISH** (Pitch/Harmony): Establish or restate the harmonic system from the specimen environment.
- **AAC - HARMONY_TENSION_UP** (Pitch/Harmony): Increase harmonic tension without changing the harmonic jurisdiction itself.
- **AAG - HARMONY_ROTATE_VOICING** (Pitch/Harmony): Rotate voicing or upper-structure organization while preserving harmonic identity.
- **AAT - HARMONY_VACUUM** (Pitch/Harmony): Temporarily remove explicit harmony; other jurisdictions continue without inheriting its exact job.
- **ACA - MELODY_ESTABLISH** (Pitch/Melody): Establish or restate melodic contour logic.
- **ACC - MELODY_FRAGMENT** (Pitch/Melody): Break melodic material into smaller cells while preserving ancestry.
- **ACG - MELODY_STRETCH** (Pitch/Melody): Stretch melodic gestures across a larger time span.
- **ACT - MELODY_HOCKET** (Pitch/Melody): Distribute melodic material across performers or timbres as a relay.
- **AGA - TUNING_ESTABLISH** (Pitch/Tuning): Establish the tuning or intonation rule.
- **AGC - PITCH_DRIFT_MICROTONAL** (Pitch/Tuning): Apply controlled pitch drift or microtonal displacement.
- **AGG - CONSONANCE_FLIP** (Pitch/Tuning): Flip the current consonance logic into its structured opposite.
- **AGT - REGISTER_SPLIT** (Pitch/Tuning): Separate musical roles into strongly distinct registers.
- **ATA - PITCH_ANCHOR_DECLARE** (Pitch/Anchor): Declare the pitch-bearing anchor or invariant as protected reference material.
- **ATC - ANCHOR_PITCH_MUTATE** (Pitch/Anchor): Allow only the pitch aspect of the anchor to mutate while identity stays recognizable.
- **ATG - START_SPECIMEN** (Control): Required first codon. Initialize a specimen and reset local modifiers.
- **ATT - PITCH_TO_PERCUSSION** (Pitch/Transduction): Convert pitch articulation into rhythmic or percussive function without simply becoming drums.
- **CAA - BASE_PULSE_ESTABLISH** (Time/Pulse): Establish or restate the base pulse.
- **CAC - SUBDIVISION_UP** (Time/Pulse): Increase internal subdivision while the base pulse can remain stable.
- **CAG - COMPETING_PULSE** (Time/Pulse): Introduce another valid pulse or grouping so multiple rhythmic truths coexist.
- **CAT - HARD_RHYTHMIC_INTERRUPT** (Time/Pulse): Interrupt rhythmic continuity abruptly.
- **CCA - ADDITIVE_METER** (Time/Meter): Introduce additive or asymmetrical meter as an explicit timing jurisdiction.
- **CCC - REPEAT_CURRENT_BEHAVIOR** (Time/Meter): Repeat the immediately active behavior; repetition strengthens memory and recognizability.
- **CCG - ACCELERATE** (Time/Meter): Increase apparent or literal speed according to current timing context.
- **CCT - DECELERATE** (Time/Meter): Reduce apparent or literal speed while preserving other systems.
- **CGA - EVENT_DENSITY_UP** (Time/Density): Increase event-arrival rate independently of BPM.
- **CGC - EVENT_DENSITY_DOWN** (Time/Density): Decrease event-arrival rate without necessarily reducing tempo.
- **CGG - PHASE_SHIFT** (Time/Density): Shift one repeating process against another to change alignment and interference.
- **CGT - SILENCE_GATE** (Time/Density): Create explicit silence or near-silence as structural material.
- **CTA - TEMPORAL_HOCKET** (Time/Form): Pass timing responsibility between parts so no single source owns the whole phrase.
- **CTC - DUAL_CLOCK** (Time/Form): Maintain two incompatible temporal scales at once.
- **CTG - EVENT_DRIVEN_TRANSITION** (Time/Form): Change arrangement because an event occurs, not because a conventional section timer says so.
- **CTT - HARD_SCENE_CUT** (Time/Form): Cut directly to a new state with minimal transitional glue.
- **GAA - TIMBRE_ESTABLISH** (Surface/Timbre): Establish the timbre and instrument palette from the environment.
- **GAC - TIMBRE_CONTAMINATE** (Surface/Timbre): Introduce a foreign sonic material that changes the palette by contact.
- **GAG - INSTRUMENT_ROLE_SWAP** (Surface/Timbre): Swap functional roles between instruments or sound sources.
- **GAT - EXPOSE_SINGLE_STEM** (Surface/Timbre): Strip away support and expose one stem or jurisdiction clearly.
- **GCA - DRY_CLOSE_SPACE** (Surface/Space): Pull sound into dry, close, local space; reduce shared wash.
- **GCC - WIDEN_SPACE** (Surface/Space): Increase spatial spread or reverberant field while preserving source identities.
- **GCG - SPECTRAL_MIGRATION** (Surface/Space): Move energy, register, or spectral emphasis across the sound field.
- **GCT - MEDIUM_DEGRADATION** (Surface/Space): Make recording-medium damage or lo-fi behavior causally affect the sound.
- **GGA - PERFORMANCE_ESTABLISH** (Performance): Establish the performance attitude from the environment.
- **GGC - EXTREME_PRECISION** (Performance): Force hyper-precise execution and articulation.
- **GGG - ESCALATE_PARTICIPATION** (Performance): Increase participation, intensity, or number of active agents without merely raising volume.
- **GGT - CONTROLLED_COLLAPSE** (Performance): Let precision degrade into structured collapse while preserving traceable cause.
- **GTA - CAST_SPAWN** (Performance/Cast): Introduce a new performer or population with its own job.
- **GTC - CALL_RESPONSE** (Performance/Cast): Create explicit call-and-response between distinct performers or populations.
- **GTG - ROLE_INFECTION** (Performance/Cast): Allow one role to borrow another role's behavior while remaining distinguishable.
- **GTT - MASS_PARTICIPATION** (Performance/Cast): Trigger group participation: chant, clap, response, swarm, or another social musical action.
- **TAA - STOP_CURRENT_PROCESS** (Global/Control): Stop the currently foregrounded process locally; do not necessarily end the specimen.
- **TAC - HOLD_A_FIXED_WHILE_B_MIGRATES** (Global/Operator): Freeze the current anchor or system while a different active system changes around it.
- **TAG - SECTION_BOUNDARY** (Global/Control): Close the local phase, preserve accumulated scars, and clear temporary one-shot modifiers.
- **TAT - MAKE_A_BEHAVE_LIKE_B** (Global/Operator): Make one jurisdiction obey another jurisdiction's mechanics without becoming it.
- **TCA - COMPRESS** (Global/Operator): Compress current material or transformation into a smaller duration or space.
- **TCC - STRETCH** (Global/Operator): Stretch current material or transformation across a larger duration or space.
- **TCG - INVERT_RELATIONSHIP** (Global/Operator): Invert a current relation, dependency, direction, or ordering rule.
- **TCT - FRACTURE** (Global/Operator): Split a coherent active structure into still-related fragments.
- **TGA - END_SPECIMEN** (Global/Control): Required final codon. End the specimen and freeze the final ledger.
- **TGC - RETURN_TO_ANCHOR** (Global/Anchor): Return to the recognizable anchor or invariant after mutation.
- **TGG - REFORM_STRANGER** (Global/Anchor): Rebuild the current organism after collapse while preserving ancestry and scars.
- **TGT - DELETE_JURISDICTION** (Global/Anchor): Temporarily remove one whole jurisdiction; remaining systems may not simply inherit its exact job.
- **TTA - PROTECT_NEXT_CODON** (Genome/Meta): Mark the next executable codon as mutation-protected.
- **TTC - DUPLICATE_PREVIOUS_CODON** (Genome/Meta): Duplicate the previous executable behavior as a deliberate genetic repeat.
- **TTG - OPEN_MUTATION_HOTSPOT** (Genome/Meta): Mark the following local cassette as high-probability mutation territory until the next section boundary.
- **TTT - SCAR_LOCK_PREVIOUS** (Genome/Meta): Fossilize the preceding local behavior or cassette so breeding preferentially preserves it.

## 6. Expression rules

Codons are operations, not fixed notes or instruments. Exact musical realization comes from the environment and current state.

### Repetition

- One copy: normal strength.
- Two adjacent copies: reinforced, longer, or more obvious.
- Three adjacent copies: persistent structural behavior.
- Four or more: saturation; interpret as a dominant condition rather than increasing forever.
- `TTC` duplicates the previous executable codon intentionally and records that duplication.

### Conflict

Opposing instructions do **not** silently cancel. If `CGA` (event density up) and `CGC` (event density down) coexist, the compiler finds a structural way for both to exert pressure: different layers, performers, time scales, thresholds, or phases. Use `TAA` only when a process should actually stop.

### Jurisdiction integrity

A rhythm instruction may change rhythm; it may not quietly rewrite harmony because that is convenient. Cross-jurisdiction behavior requires an explicit global operator such as `TAT`, `TAC`, `TCG`, or `TGT`.

### Anchor integrity

The anchor remains recognizable by at least one declared property: contour, rhythm, timbre, phrase, interval shape, text fragment, groove, or another explicit invariant. `ATC` may mutate anchor pitch while identity survives. `TGC` returns the anchor. `TGG` reforms the organism stranger.

## 7. Mutation rules

All mutations are recorded. No invisible cleanup mutation.

Default mutation operators:

1. **Point mutation** - change one base.
2. **Codon substitution** - replace one full codon.
3. **Codon duplication** - duplicate one codon or short cassette.
4. **Codon deletion** - remove one or more complete codons.
5. **Cassette inversion** - reverse codon order in a region; do not reverse-complement unless explicitly requested.
6. **Translocation** - move a codon block elsewhere.
7. **Crossover** - splice two parent genomes at codon boundaries.
8. **Reverse-complement experiment** - optional high-chaos operation; label it because it changes every codon in the region.
9. **Frameshift experiment** - optional very-high-chaos operation; insert/delete 1 or 2 bases inside a bounded cassette and reparse that cassette. Never perform frameshift silently.

Protection/scars:

- `TTA` protects the next executable codon from ordinary mutation.
- `TTG` opens a mutation hotspot until the next `TAG`.
- `TTT` scar-locks the preceding local behavior/cassette.
- START and END are protected by default.
- Anchor declarations are protected by default unless an experiment explicitly allows anchor breach.

## 8. Breeding rules

Two-parent breeding is encouraged.

Default child rules:

- Cross on codon boundaries unless frameshift mode is explicit.
- Target the mean parental codon count, normally within +/-15%.
- Preserve exactly one START at the front and one END at the end.
- Preserve at least one recognizable anchor declaration/return path.
- Protected/scar-locked regions receive elevated inheritance probability.
- Hotspots receive elevated mutation probability after crossover.
- Require meaningful material from both parents; cloning one parent with cosmetic edits is rejected.
- Record all crossovers and mutations in the ledger.

"Fitness" means artistic selection criteria for the experiment, not biological fitness.

## 9. Rule packs: yes, the rules can change every time

We can absolutely change the rules between experiments. We just do not do it silently.

- **Base codebook:** stable mapping such as `SLOP-SEQ-v0.1`.
- **Session overlay:** temporary rules that change expression without remapping codons, e.g. "all cast operations are barn animals trying and failing to sing" or "every collapse must expose a usable stem."
- **Forked codebook:** if a codon meaning changes, create a new version. Old specimens keep their original decoder forever.

Every specimen records `codebook_version`, `overlay_id`, and custom rules.

## 10. Environment packet rules

The genome gives behavior; the environment gives material. Before compiling, invent or supply:

- harmony system;
- melodic system;
- rhythmic system;
- timbre/atmosphere system;
- performance attitude;
- anchor/invariant.

Prefer ingredients from genuinely different traditions, eras, instruments, production methods, vocal systems, and rhythmic practices. Do not choose six ways of saying the same genre.

## 11. SLOP-SEQ -> Suno phenotype compiler

1. Validate START/END, length, codebook version, and environment.
2. Initialize the six musical jurisdictions.
3. Walk codons in order and update a state ledger.
4. Preserve path dependence: later codons act on the state produced by earlier codons.
5. Honor boundaries, protections, scars, hotspots, and anchor returns.
6. Convert the trace into concise musical instructions.
7. Keep jurisdictions distinct; do not turn the trace into random genre stacking.
8. Produce a complete Suno style prompt.
9. If vocals are useful, optionally create a phonetic engine: plosives = percussion; nasals = resonance; open vowels = sustained melody; rolled consonants = agitation; dense syllables = compressed runs; long vowels = stretched time; heavy syllables = bass weight.
10. Export the ledger with the prompt so the result can be mutated later.

Current house Suno export profile:

- STYLE: 975-999 characters.
- LYRICS / operator field: 4900-4999 characters when used.
- CAPTION: <=499 characters.

Those are export settings, not genetic code.

## 12. Seq2Music integration

Seq2Music is deliberately a second decoder, not an implementation of our codon grammar.

For a SLOP-SEQ specimen:

1. Save the chromosome as FASTA and select `kind=dna`.
2. Encode it with Seq2Music.
3. Preserve WAV, MIDI, MusicXML, SVG score, HTML, CSV event ledger, summary, and run manifest.
4. Record Seq2Music version/commit and parameters.
5. Treat Seq2Music output as the **carrier phenotype**.
6. Compile the same chromosome through SLOP-SEQ into the **behavior phenotype** (Suno instructions).
7. Compare, cross-feed, mutate, or breed based on either phenotype.

Exact Seq2Music carriers can contain recoverable source sequence metadata. That matters for real biological sequences; our invented SLOP-SEQ strings are synthetic art data.

## 13. Feedback-loop experiments

- **Genome -> dual phenotype:** DNA -> SLOP-SEQ prompt AND DNA -> Seq2Music audio/score.
- **Point mutation audition:** change exactly one nucleotide, render both parents, compare.
- **Breed two songs:** crossover two successful genomes, preserve scars, introduce 1-3 mutations, compile/sonify the child.
- **Audio -> lossy genome -> music again:** use Seq2Music audio-decode as an explicitly lossy DNA projection, then mutate or compile that projection.
- **Frameshift monster:** frameshift only a bounded cassette, then return to normal parsing at an explicit boundary.

## 14. Specimen ledger

Every specimen records:

- specimen ID/name/date;
- parents;
- codebook version;
- overlay/rule-pack ID;
- environment packet;
- raw DNA;
- SHA-256;
- protections/hotspots/scars;
- mutation list;
- decoded codon trace;
- Suno style/lyrics/caption;
- Seq2Music parameters and output names/hashes;
- user star/rating and feedback;
- next mutation hypothesis.

Taste can alter future selection probability without rewriting old genomes or codebooks.

## 15. Failure modes

Reject or flag:

- random A/C/G/T with no compositional reason;
- codebook changes without a new version;
- genre soup replacing jurisdiction logic;
- undocumented mutation;
- anchor so strong nothing moves;
- anchor so weak nothing is recognizable;
- deleting a jurisdiction and secretly giving its exact job to another;
- "chaos" used as an adjective rather than an operation;
- pseudo-biological claims that the sequence has biological function;
- comparing different codebook versions as directly equivalent;
- describing arbitrary audio-to-DNA projection as exact when Seq2Music reports it as lossy.

## 16. Naming convention

`SLOP-SEQ-###_<short-name>/`

Suggested contents:

- `genome.fasta`
- `manifest.json`
- `decoded_genome.md`
- `suno_style.txt`
- `suno_lyrics.txt` if used
- `caption.txt`
- `seq2music/` outputs
- `notes.md`

## 17. First specimen

**SLOP-SEQ-001 - ANCHOR UNDER SIEGE / CAST RIOT**

Goal: a legible anchor survives multiple rhythmic truths, escalating cast participation, whole-jurisdiction deletion, controlled collapse, return, and stranger reconstruction.

See `specimens/001_anchor_under_siege/`.
