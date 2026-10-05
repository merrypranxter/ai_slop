# SLOP-SEQ-001A — HARD INTERRUPT

This is the first controlled point mutant of SLOP-SEQ-001. Everything stays fixed except **one nucleotide**.

## Mutation

- Base position: **30** (1-indexed)
- DNA: **G -> T**
- Codon 10: **CAG -> CAT**
- Parent instruction: **COMPETING_PULSE**
- Mutant instruction: **HARD_RHYTHMIC_INTERRUPT**

Parent section begins by establishing a base pulse and then adds a second valid rhythmic truth. The mutant instead interrupts that pulse architecture abruptly at the same location. All later codons are identical, so any downstream differences are path-dependent consequences of this single substitution.

## Parent local cassette

`TAG CAG CCC CAC CTC ACA ACT AGT GTA GTC GGG TAG`

## Mutant local cassette

`TAG CAT CCC CAC CTC ACA ACT AGT GTA GTC GGG TAG`

## Experimental question

Does one nucleotide that changes **coexisting pulse -> hard interruption** produce a musically legible family difference in both:

1. the SLOP-SEQ / Suno phenotype; and
2. the independent Seq2Music DNA sonification?

This is a clean ablation: no environment change, no extra mutation, no codebook change.
