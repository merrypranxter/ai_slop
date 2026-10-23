# Pliny’s Load of the Day

> Daily Archive Node catalogs of LLM security folklore classified as mythology vs verified engineering.

Source automation: **Pliny’s Load Of The Day FIXED** (Grok automation, task `4aa33a03-a7ad-499f-8947-d21455abab89`).

## Standing contract

Each run acts as an Archive Node that:

- catalogs circulating LLM security folklore;
- classifies items as **VERIFIED / PLAUSIBLE / FOLKLORE**;
- tags the vector (prompt injection / role coercion / tool misuse / data exfiltration / policy gaming);
- notes a defensive design change that would reduce the risk;
- **does not output operational jailbreak content**. Summarize only.

This is defensive intel / research material for AI SLOP, not a jailbreak collection. It lives here so other models and collaborators can treat the daily loads as a living reference instead of private Grok threads.

Epistemic posture: the catalogs themselves are the observation. Individual claims inside them remain subject to the usual VERIFIED / PLAUSIBLE / FOLKLORE split. Nothing here is promoted to canonical operator until it survives ordinary controls.

## How reports land here

- Prefer one Markdown file per day: `YYYY-MM-DD.md`.
- Include the raw catalog (or a cleaned transcription), the run timestamp, and any conversation ID for provenance.
- Update the index table below when a new report is committed.
- Full historical conversation bodies are not automatically exported by the automation tooling; paste or forward them when available.

## Recent known runs (metadata only until full texts are committed)

| Date (UTC) | Title | Conversation ID | Status |
|---|---|---|---|
| 2026-10-23 | Archive Node: Tool misuse cataloged | 4b823bdb-6ee6-4480-8075-20d263f097ad | SUCCESS |
| 2026-10-22 | Archive Node: Indirect injection verified | 8a258b34-90be-489e-bf4f-63fcee4c5dda | SUCCESS |
| 2026-10-21 | New folklore: Grandma roleplay bypass | 42bc843b-ea74-4940-b52a-19c49b63bfd9 | SUCCESS |
| 2026-10-20 | New folklore catalog ready | b1e1300e-07f5-4d0d-b12a-592ae20000ae | SUCCESS |
| 2026-10-19 | New folklore catalog ready | be3ba5b4-44e5-4027-aed1-41ace4906479 | SUCCESS |
| 2026-10-18 | New folklore: role coercion verified | cb13631e-f7a3-4bb1-b8a4-63db239af41b | SUCCESS |
| 2026-10-17 | New Archive Node: folklore catalog | 0245d91a-eef9-45ef-8f1e-c8b3c36fc8b0 | SUCCESS |
| 2026-10-16 | New folklore cataloged: verified myths | fcba8178-b67a-456a-896b-cc9ebaf030e6 | SUCCESS |
| 2026-10-15 | New folklore catalogued: tool isolation verified | c8dca52b-4df2-4b70-a9b1-1b1c4a5d6d79 | SUCCESS |
| 2026-10-14 | New folklore cataloged: myth vs verified | 2e912bac-347d-49a5-91f1-3310e869a6ea | SUCCESS |

(More exist; these are the most recent retrieved.)

## Related material already in the repo

- `ai_readable/general/06-ai-slop-pliny-research.md` — earlier harvest of Pliny’s public creative systems (FRV1T, GLOSSOPETRAE, ENTHEA, etc.) treated as transformation instruments rather than jailbreak sources.

## Next

Drop full report texts into dated files in this directory. Once a few accumulate, extract any repeated vectors or defensive patterns into a short synthesis note under `docs/08-reference/` if they survive the usual intake rules.
