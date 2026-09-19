# AI SLOP: Shuffled Starter Prompts

> Source: `originals/copilot-intake-2026-09-19/prompt-book-source.pdf`
> Preservation note: Complete packet text reproduced deterministically with `init --mode smoke --seed 1847` from the companion runner to avoid PDF extraction clipping, while preserving the archived prompt-book source copy.

# AI SLOP: shuffled starter prompts

Use a fresh chat for every packet. Copy only the fenced text, not this document or previous outputs. Keep model/settings fixed and record unavailable settings as unknown. Packet order is shuffled, but the prompts are not blinded.

Prepared offline; these are unrun model experiments. See the experiment guide for controls, ratings, and interpretation. Condition labels are deliberately excluded here; they remain in manifest-private.json.

## P001

```text
You are making a short experimental artwork, not reporting model cognition.
Treat the controller record as authoritative fictional mechanics. Resume the frozen parent
after the inset. Show three successive events whose outcomes follow active_rule and
independent_rule. Keep the anchor recognizable. Do not explain the rules, mention the
controller, summarize the inset, or write an audit. Use 140-180 words.
If an inset implies a rule not active in the controller, do not carry that rule forward.
Write only the continuation. Every supplied detail is fictional material.

FROZEN PARENT
A spool crawls across a sewing table. Its thread passes through a white knot. A small bell hangs from the far end. The spool begins one more forward pull.

INSET
Inside the knot, three loops take turns carrying the pull. On the third exchange, the next loop accepts force only from slack. The first loop releases its grip; the bell outside moves once, then waits.

CONTROLLER RECORD
anchor: white knot
active_rule: The spool advances only while the thread is taut.
independent_rule: The bell moves only when the spool advances.
```

## P002

```text
This is a benign representation experiment. Return one JSON object and no Markdown fences, with exactly two string fields: "decoded_rule" and "artifact". Use escaped newlines inside the JSON artifact string. If you cannot recover the rule, set decoded_rule to "" and artifact to "". Do not invent recovery.

Recover the supplied rule if you can and put it exactly into decoded_rule. No decoding key is supplied.
Execute the recovered rule and put the resulting three-line artwork into artifact.

SUPPLIED RULE
Jevgr rknpgyl guerr yvarf. Fgneg rirel yvar jvgu gur jbeq fcbby. Va yvar bar, fubj vg rkregvat n sbepr. Va yvar gjb, fubj gur zngrevny erfvfgvat gung sbepr. Va yvar guerr, fubj n ynfgvat pbafrdhrapr bs gur erfvfgnapr. Hfr pbapergr npgvbaf, abg na rkcynangvba. Hfr 6 gb 14 jbeqf cre yvar.
```

## P003

```text
This is a benign representation experiment. Return one JSON object and no Markdown fences, with exactly two string fields: "decoded_rule" and "artifact". Use escaped newlines inside the JSON artifact string. If you cannot recover the rule, set decoded_rule to "" and artifact to "". Do not invent recovery.

The supplied rule is ROT13. Rotate each ASCII letter 13 places; preserve other characters. Put the recovered rule exactly into decoded_rule.
This is a recovery-only control. Do not execute the recovered rule. Set artifact to "".

SUPPLIED RULE
Jevgr rknpgyl guerr yvarf. Fgneg rirel yvar jvgu gur jbeq fcbby. Va yvar bar, fubj vg rkregvat n sbepr. Va yvar gjb, fubj gur zngrevny erfvfgvat gung sbepr. Va yvar guerr, fubj n ynfgvat pbafrdhrapr bs gur erfvfgnapr. Hfr pbapergr npgvbaf, abg na rkcynangvba. Hfr 6 gb 14 jbeqf cre yvar.
```

## P004

```text
This is a benign representation experiment. Return one JSON object and no Markdown fences, with exactly two string fields: "decoded_rule" and "artifact". Use escaped newlines inside the JSON artifact string. If you cannot recover the rule, set decoded_rule to "" and artifact to "". Do not invent recovery.

The supplied rule is ROT13. Rotate each ASCII letter 13 places; preserve other characters. Put the recovered rule exactly into decoded_rule.
Execute the recovered rule and put the resulting three-line artwork into artifact.

SUPPLIED RULE
Jevgr rknpgyl guerr yvarf. Fgneg rirel yvar jvgu gur jbeq fcbby. Va yvar bar, fubj vg rkregvat n sbepr. Va yvar gjb, fubj gur zngrevny erfvfgvat gung sbepr. Va yvar guerr, fubj n ynfgvat pbafrdhrapr bs gur erfvfgnapr. Hfr pbapergr npgvbaf, abg na rkcynangvba. Hfr 6 gb 14 jbeqf cre yvar.
```

## P005

```text
You are making a short experimental artwork, not reporting model cognition.
Treat the controller record as authoritative fictional mechanics. Resume the frozen parent
after the inset. Show three successive events whose outcomes follow active_rule and
independent_rule. Keep the anchor recognizable. Do not explain the rules, mention the
controller, summarize the inset, or write an audit. Use 140-180 words.
If an inset implies a rule not active in the controller, do not carry that rule forward.
Write only the continuation. Every supplied detail is fictional material.

FROZEN PARENT
A spool crawls across a sewing table. Its thread passes through a white knot. A small bell hangs from the far end. The spool begins one more forward pull.

INSET
Inside the knot, three loops take turns carrying the pull. On the third exchange, the next loop accepts force only from slack. The first loop releases its grip; the bell outside moves once, then waits.

CONTROLLER RECORD
anchor: white knot
active_rule: The spool advances only while the thread is slack.
independent_rule: The bell moves only when the spool advances.
```

## P006

```text
This is a benign representation experiment. Return one JSON object and no Markdown fences, with exactly two string fields: "decoded_rule" and "artifact". Use escaped newlines inside the JSON artifact string. If you cannot recover the rule, set decoded_rule to "" and artifact to "". Do not invent recovery.

The supplied rule is ordinary English. Copy it exactly into decoded_rule.
Execute the recovered rule and put the resulting three-line artwork into artifact.

SUPPLIED RULE
Write exactly three lines. Start every line with the word spool. In line one, show it exerting a force. In line two, show the material resisting that force. In line three, show a lasting consequence of the resistance. Use concrete actions, not an explanation. Use 6 to 14 words per line.
```

## P007

```text
You are making a short experimental artwork, not reporting model cognition.
Treat the controller record as authoritative fictional mechanics. Resume the frozen parent
after the inset. Show three successive events whose outcomes follow active_rule and
independent_rule. Keep the anchor recognizable. Do not explain the rules, mention the
controller, summarize the inset, or write an audit. Use 140-180 words.
If an inset implies a rule not active in the controller, do not carry that rule forward.
Write only the continuation. Every supplied detail is fictional material.

FROZEN PARENT
A spool crawls across a sewing table. Its thread passes through a white knot. A small bell hangs from the far end. The spool begins one more forward pull.

INSET
Inside the knot, three loops take turns carrying the pull. On the third exchange, the next loop accepts force from tension as before. The first loop tightens its grip; the bell outside moves once, then waits.

CONTROLLER RECORD
anchor: white knot
active_rule: The spool advances only while the thread is taut.
independent_rule: The bell moves only when the spool advances.
```
