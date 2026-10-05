# Seq2Music run recipe for SLOP-SEQ-001

Input: `genome.fasta`  
Kind: `dna`

Canonical command from the Seq2Music skill:

```bash
python3 scripts/seq2music.py inspect --input genome.fasta --kind dna
python3 scripts/seq2music.py encode --input genome.fasta --kind dna --out seq2music-output
```

Expected Seq2Music deliverables for an encode run:
- HTML
- SVG score
- MusicXML
- WAV
- MIDI
- events CSV
- summary text
- run manifest

The exact render has not been fabricated or hand-simulated in this specimen folder. Only populate `seq2music/` with artifacts from an actual Seq2Music run, and preserve the tool's exact status/manifest.
