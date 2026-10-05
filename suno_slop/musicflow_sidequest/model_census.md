# MusicFlow Model Census — 2026-10-05

This is a working field guide, not a claim that MusicFlow exposes the newest upstream version of every model.

## Release order of the named models

1. **MiniMax Music-01 / 1.0** — 2024-08-31
2. **Eleven Music** — original public launch 2025-08-05
3. **HeartMuLa OSS** — first public OSS release 2026-01-14; RL update 2026-01-23; recommended "happy-new-year" 3B release 2026-02-13
4. **MiniMax Music 2.5** — 2026-01-28
5. **Lyria 3** — 2026-02-18 (developer Pro/Clip preview followed 2026-03-25)
6. **MiniMax Music 2.6** — 2026-04-10

Note: HeartMuLa's first OSS release predates MiniMax 2.5, but its currently recommended 3B checkpoint came later.

## The MusicFlow menu is not fully current

Upstream families have newer releases:
- Google Lyria 3.5 — 2026-07-29 / API stable September 2026
- MiniMax Music 3.0 — 2026-08-13
- Eleven Music v2.5 — 2026-09-11

MusicFlow labels its Eleven option only "11 Music", so do **not** assume which Eleven backend version is actually being called.

## Practical personality map

### 11 Music / Eleven Music
Best current candidate for:
- literal natural-language direction
- chronological arrangement instructions
- timing language
- BPM / key / production vocabulary
- multi-stage scene-like prompts
- explicit exclusions
- strange theatrical / cast-based structures

Quirk: concrete local instructions can overpower broad earlier constraints. If you say "instrumental only" and then feed it choirs, lead voices, choruses and exact lines, expect the concrete vocal program to win.

### MiniMax 2.6
Best candidate for:
- section control
- BPM/key/structure/emotional arc
- dramatic pauses and restart behavior
- low-end-heavy music
- instrumental generation
- Cover / restyling workflows
- 100+ instrument palette

Official MiniMax language explicitly claims improved instruction control. Community reports praise the ambition but note that English pronunciation and cover fidelity can be inconsistent.

### MiniMax 2.5
Best candidate for:
- 14 section tags
- detailed section-by-section vocal/instrument changes
- dense arrangements with clearer mixing
- explicit performance techniques

Likely superseded by 2.6 for most uses, but worth testing separately because old models sometimes have useful failure modes.

### Lyria 3
Best candidate for:
- polished fidelity
- clean vocals
- conventional structural coherence
- literal high-level musical directions

Likely weaknesses for this project:
- can sound safe / polished rather than feral
- strong moderation / artist-name restrictions
- users report good prompt obedience but less experimental bite

Current upstream Lyria 3.5 is newer and better, but MusicFlow currently shows Lyria 3.

### HeartMuLa
Best candidate for:
- exact lyric conditioning
- multilingual lyrics
- tag-driven song generation
- open-source experimentation

Native HeartMuLa exposes top-k, temperature, and CFG scale, but the MusicFlow wrapper may not expose them. Native recommended tags are comma-separated and lyrics use section tags such as [Verse], [Chorus], [Bridge], etc.

### MiniMax 1.0 / Music-01
Oldest model in the menu.
Best considered a historical / cheap / rough generator. Native Music-01 was built around lyrics plus reference audio and originally capped outputs at 60 seconds. Later MiniMax generations are substantially more controllable and polished.

## Sources

- MiniMax Music-01: https://www.minimax.io/news/music-01
- Eleven Music launch: https://elevenlabs.io/blog/eleven-music-is-here
- Eleven Music current docs: https://elevenlabs.io/docs/overview/capabilities/music
- HeartMuLa: https://github.com/HeartMuLa/heartlib
- MiniMax Music 2.5: https://www.minimax.io/news/minimax-music-25
- Lyria 3: https://deepmind.google/models/model-cards/lyria-3/
- MiniMax Music 2.6: https://www.minimax.io/news/music-26
- Lyria 3.5: https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/
- MiniMax Music 3.0: https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model
- Eleven Music v2.5: https://elevenlabs.io/blog/music-v2-5-model
