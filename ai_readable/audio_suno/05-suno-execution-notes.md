# Suno Execution Notes

## Prefer Physical Specificity to Compound Genres

Name instruments, tuning systems, rhythmic practices, tempos, vocal techniques, spaces, and production behavior separately. A list of distinct acoustic instructions gives the model clearer responsibilities than a coined genre label.

Instead of asking for a generic experimental hybrid, specify:

- what establishes harmony;
- what generates melody;
- what controls pulse;
- what occupies the sonic environment;
- how the performer behaves;
- what never changes.

## Use Structural Tags as State Changes

Place bracketed directions where the arrangement should mutate. Tags are most useful when they describe a transition that can be heard, such as:

- `[Anchor established]`
- `[Rhythm drops to half-time]`
- `[Midrange removed]`
- `[Acoustic instruments cut]`
- `[Voice dissolves into static]`
- `[Anchor returns alone]`

Do not overload every line with instructions. Reserve tags for structural events and let each section establish a coherent behavior.

## Treat Lyrics as Performance Data

Standard prose encourages semantic delivery. Nonsense phonetics can instead guide:

- attack speed;
- transient shape;
- vowel duration;
- register and weight;
- repetition density;
- breath and resonance;
- transitions between voice and percussion.

Pair phonetic families with the relevant system. For example, plosives can reinforce clipped percussion, sustained vowels can oppose it with continuous melody, and nasals can merge into a drone anchor.

## Separate Design from Delivery

The full jurisdiction matrix and operator list are design documents. The final Suno input should be a compact rendering of that design:

1. compress the system assignments into a style block;
2. map operators to a small number of structural sections;
3. put performance directions beside the material they control;
4. preserve the invariant through each section;
5. remove decorative explanation that does not produce sound.

## Iterate One Dimension at a Time

When a generation misses the concept, revise the responsible jurisdiction rather than rewriting everything:

- weak identity: make the anchor simpler or more frequent;
- muddy conflict: separate systems by range, space, or timing;
- generic result: replace adjectives with mechanisms;
- conventional song form: strengthen state-change tags;
- ordinary vocals: tighten phonetic rules;
- random result: reduce the number of operators or clarify their triggers.

Keep successful assignments fixed while testing one changed dimension. This makes each generation informative.
