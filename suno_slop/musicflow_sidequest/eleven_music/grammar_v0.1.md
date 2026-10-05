# Eleven Music / "11 Music" Grammar v0.1

Status: **working hypothesis based on first MusicFlow specimen + upstream Eleven Music prompting documentation.**

## Core idea

Treat the one-box prompt as a **band briefing / event score**, not as a Suno style box stapled to a lyrics box.

### Preferred order

1. GLOBAL IDENTITY
2. HARD CONSTRAINTS
3. CAST / INSTRUMENT JOBS
4. RHYTHMIC LAW
5. CHRONOLOGICAL ARRANGEMENT
6. EXACT TEXT TO PERFORM
7. END CONDITION

## Strong syntax

Use explicit chronological verbs:
- START WITH
- ONLY
- AFTER
- THEN
- ENTER
- DROP OUT
- RETURN
- STOP
- HOLD
- CONTINUE
- END ON

Eleven's official guidance specifically says arrangement narration in order is effective.

## Do not create abstract contradictions by accident

Bad:
- "no vocals" globally
- followed later by choir, lead voice, chorus and exact lyrics

The first specimen proves concrete local vocal instructions can dominate the abstract early ban.

Instead write one unambiguous global rule:
- VOCALS REQUIRED
or
- INSTRUMENTAL ONLY

## Separate jobs

Prefer:
- KANJIRA = fixed pulse
- NADASWARAM = glissando lead
- MELLOTRON = quartal field
- CHOIR A = anchor
- CHOIR B = answer
- DAXOPHONE = nonverbal groan layer

Do not ask everything to do everything.

## Translate theory into executable behavior

Instead of only:
"5:7:11 polymeter with phase drift"

also say:
- one layer repeats every 5 pulses
- one every 7
- one every 11
- do not reset them together
- let alignments drift
- preserve a separate 3:2 stomp/clap coupling

Theoretical labels may help, but behavioral instructions are easier to test.

## Negative space

Explicitly name what must be absent:
- no ominous delivery
- no cinematic horror pads
- no smooth blended choir
- no four-on-the-floor simplification
- no final tonic cadence

Eleven's own docs emphasize that words like "just" and explicit exclusions prevent the model from filling empty space with defaults.

## Brackets

Observed in MusicFlow specimen:
- bracketed material was usually treated as direction rather than spoken lyric
- unbracketed lines were performed much more literally

But brackets are not a formal universal programming language. Use familiar role/section labels and short operational directions rather than enormous pseudo-code tags.

## Working one-box architecture

```
[GLOBAL]
genre / energy / mix / duration / vocal-or-instrumental rule

[CAST]
named performers and one job each

[RHYTHM]
explicit pulse behavior

[START]
what exists first + exact performed text

[THEN]
new entrance / subtraction / phase change + exact performed text

[NEXT]
...

[END]
specific final state
```

## Variables to test later

- early vs late contradiction precedence
- bracket vs braces vs plain-language direction
- exact pan instructions
- exact BPM adherence
- odd-meter / polymeter literalness
- click consonant spelling
- whether repeated constraints strengthen or merely waste prompt budget
- how much order controls timeline versus global conditioning
- which MusicFlow backend version "11 Music" actually calls
