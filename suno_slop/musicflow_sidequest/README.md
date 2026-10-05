# MusicFlow Side Quest

This folder is a separate lab inside the Suno/audio area. It is **not Suno prompting**. MusicFlow exposes several different third-party music models, each with its own input grammar and behavior.

## Goal

Reverse-engineer each model empirically:
- what each input field actually controls
- prompt order / recency effects
- bracket and section syntax
- lyric literalness
- arrangement / timing obedience
- instrumentation obedience
- negative prompts and exclusions
- weird phonetic behavior
- multi-voice / cast behavior
- meter, BPM, key, and structural control
- what the MusicFlow wrapper exposes or hides

Do not assume one MusicFlow grammar. Treat each selectable model as a separate animal.

## Models seen in the MusicFlow selector (2026-10-05)

- 11 Music (Eleven Music family; MusicFlow does not expose the exact Eleven backend version)
- MiniMax 1.0 / Music-01
- MiniMax 2.5
- MiniMax 2.6
- HeartMuLa
- Lyria 3

## Controls visible in the 11 Music screen

- `s 100` = requested duration in seconds
- `# 1` = number of outputs / variations to generate
- These are not temperature / CFG / weirdness controls.

## First strong finding: 11 Music

The first generated specimen behaved very differently from Suno. It treated a long mixed prompt as an ordered performance brief. Bracketed directions were mostly not spoken, while ordinary prose/lyric lines were performed in sequence. Specific later vocal instructions overrode an earlier abstract "no vocals" instruction.

Working hypothesis:

GLOBAL CONTRACT -> ORDERED ARRANGEMENT DIRECTIONS -> LOCAL PERFORMANCE CUES -> PERFORMED TEXT

Eleven's own current prompting guidance supports this interpretation: it recommends narrating the arrangement chronologically ("start with", "after four bars", "then bring in") and says the model responds strongly to explicit production vocabulary, BPM/key, exclusions, and timing.

See `eleven_music/grammar_v0.1.md` and `eleven_music/prompts/nightmare_v2.txt`.

## Audio storage

Put MusicFlow-generated audio under `audio/` **without renaming the original files**. Keep source filenames intact so generations can be compared against screenshots/prompts later.
