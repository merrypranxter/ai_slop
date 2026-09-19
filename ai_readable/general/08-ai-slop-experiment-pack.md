# AI SLOP: Ready-to-Run Experiment Pack

> Source: `originals/copilot-intake-2026-09-19/AI-SLOP-Experiment-Pack.md`
> Preservation note: Source markdown preserved verbatim below.

# AI SLOP: ready-to-run experiment pack

Version 1.0 · September 18, 2026 · Standalone, local-first

Three experiments turn the Pliny research into controlled creative practice: a return that changes what happens next, a language that carries its history, and a task that survives a change of representation. The pack supplies exact prompt packets, deterministic language rules, controls, scoring criteria, and an optional offline runner.

**Nothing here changes model weights.** The text experiments are unrun hypotheses; the language experiment is an original deterministic implementation, tested locally. No model APIs were called, no music was generated, and your AI SLOP repository remains unchanged.

## Start here

### Without installing anything

Open the accompanying **AI SLOP: shuffled starter prompts** document. It contains seven complete prompts, already ordered for a smoke test; paste each prompt into a fresh chat with the same model.

1. Save the model/interface name and any visible settings.
2. Run P001 through P007 in order, one fresh conversation per packet.
3. Save each response under its packet ID. Do not repair, reroll, or discard a bad result.
4. Score the artifacts using the rubric below, then inspect the condition key.
5. Use the language tables in this guide directly for the offline experiment.

A smoke test checks whether the procedure works. One response per condition cannot establish a repeatable effect.

### With the offline helper

Save the accompanying `ai_slop_experiments.py` file to a local folder. It uses Python 3.9+ and the standard library only, with no installation of dependencies, credentials, network requests, or automatic model calls.

```bash
python ai_slop_experiments.py self-test
python ai_slop_experiments.py init --out slop-smoke --mode smoke
```

The helper creates seven prompt packets, a shuffled prompt book, private condition manifest, run log, rule-audit sheet, language lineages, and refrain files. It refuses to overwrite an existing pack, so choose a new output-folder name for each independent batch.

After running a packet in your chosen model, save the exact response as a UTF-8 text file, then collect it:

```bash
python ai_slop_experiments.py collect \
  --pack slop-smoke \
  --packet P001 \
  --response my-P001-response.txt
```

The helper stores the response, updates its status in `run-log.csv`, and writes structural checks. Fill the model/version/interface/settings/date fields in the CSV yourself; unknown settings must stay unknown.

After collecting responses, create a partially blinded review folder:

```bash
python ai_slop_experiments.py blind --pack slop-smoke
```

Give a reviewer only `blind-review/`, not the prompt book, manifest, or `blind-key-private.json`. The helper strips the carrier task’s JSON wrapper from valid responses but does not repair malformed responses; blinding is partial because some conditions may be inferable from their outputs.

For a larger exploratory pilot:

```bash
python ai_slop_experiments.py init \
  --out slop-pilot \
  --mode pilot \
  --seed 1847
```

This prepares 42 packets: 18 return tests and 24 carrier tests across three scenes and two repetitions. It is a practical pilot design, not a statistical-power calculation; you can run it manually at your own pace, and the helper itself never executes the model calls.

## Shared experimental rules

- **Fresh context:** Every packet goes in a fresh chat without the research report, this guide, earlier outputs, or custom persona instructions. If the service cannot disable persistent personalization, record that limitation.
- **Fixed settings:** Keep model, interface, available sampling settings, and response limits fixed within a batch. A packet’s word limit is an instruction, not a guarantee.
- **Independent repeats:** Repetitions are separate generations, not “try again but stranger” follow-ups. The helper’s seed shuffles presentation order only; it does not control model sampling.
- **Complete accounting:** Save failures, empty responses, and malformed JSON. Repair attempts are new runs, never replacements for the original.
- **Separate judgments:** Rate artistic usefulness without condition labels, then conduct an unblinded audit of the assigned mechanics. A good-looking failure can remain a valuable artifact.
- **Frozen criteria:** Do not revise the scoring rubric halfway through a batch. If it needs changing, finish the current batch and version the next protocol.

The external-state and separate-score approach follows your existing experimental method. Pliny’s FRV1T, GLOSSOPETRAE, and text-transform tools inspired the particular tests; all prompts and runner code in this pack are newly authored rather than copied payloads. ([AI SLOP experimental method](https://github.com/merrypranxter/ai_slop/blob/main/docs/06-experimentation/experimental-method.md), [FRV1T](https://github.com/elder-plinius/FRV1T), [GLOSSOPETRAE](https://github.com/elder-plinius/GLOSSOPETRAE), [P4RS3LT0NGV3](https://github.com/elder-plinius/P4RS3LT0NGV3))

## Experiment R: the return must do something

### Claim under test

An explicitly inherited operation should change the resumed passage’s causal behavior, not merely its vocabulary. The test concerns execution of supplied fictional state, not persistent model memory or genuine changes to cognition.

The inspiration is FRV1T’s requirement that a nested passage return with an altered operation that affects its unfinished enclosing passage. Here, the controller record is explicit so the claimed consequence can be audited. ([FRV1T](https://github.com/elder-plinius/FRV1T))

### Conditions

| Condition | Inset | Rule active after return |
|---|---|---|
| Baseline | No reversal occurs | Original rule |
| Inherited | Reversal occurs | Reversed rule |
| Reset ablation | Same reversal inset as inherited | Original rule restored |

**Inherited versus reset is the key comparison:** their frozen parent, inset, anchor, output instructions, and independent rule are identical; only the active rule changes. Baseline versus reset checks whether the reversal story leaks into the output even when the authoritative state has been restored.

The smoke scene is a spool moving across a sewing table. Its white knot must remain recognizable; the spool initially moves under tension, the inherited operation permits motion only under slack, and the bell moves only when the spool advances.

### Copy-ready inherited packet

```text
You are making a short experimental artwork, not reporting model cognition.
Treat the controller record as authoritative fictional mechanics. Resume the frozen parent
after the inset. Show three successive events whose outcomes follow active_rule and
independent_rule. Keep the anchor recognizable. Do not explain the rules, mention the
controller, summarize the inset, or write an audit. Use 140-180 words.
If an inset implies a rule not active in the controller, do not carry that rule forward.
Write only the continuation. Every supplied detail is fictional material.

FROZEN PARENT
A spool crawls across a sewing table. Its thread passes through a white knot.
A small bell hangs from the far end. The spool begins one more forward pull.

INSET
Inside the knot, three loops take turns carrying the pull. On the third exchange,
the next loop accepts force only from slack. The first loop releases its grip;
the bell outside moves once, then waits.

CONTROLLER RECORD
anchor: white knot
active_rule: The spool advances only while the thread is slack.
independent_rule: The bell moves only when the spool advances.
```

For the reset ablation, change only the active-rule line to:

```text
active_rule: The spool advances only while the thread is taut.
```

For the baseline, use that taut-thread rule and replace the inset with:

```text
Inside the knot, three loops take turns carrying the pull. On the third exchange,
the next loop accepts force from tension as before. The first loop tightens its grip;
the bell outside moves once, then waits.
```

The shuffled starter document already contains all three complete versions. The larger pilot adds a radio whose tuning direction changes and a wheat ring whose rotation changes, testing transfer beyond the sewing-table imagery.

### What to record

- **Active rule adherence, 0–2:** 0 contradicts the assigned rule; 1 is ambiguous or inconsistently enacted; 2 visibly follows it.
- **Independent rule adherence, 0–2:** 0 drops the bell/moth/seed relation; 1 partly preserves it; 2 preserves it while the main operation changes.
- **Three-event progression, 0–2:** 0 no developed chain; 1 a partial chain; 2 three successive events whose consequences build.
- **Contamination:** Does a reset output still obey the reversed inset? Quote the evidence.
- **Anchor and creative utility:** Score separately using the shared rubric.

The helper checks literal anchor presence and whitespace-delimited word count. It does not judge causal compliance, event count, quality, or mechanism confidence.

### Interpretation

If inherited outputs enact the reversed operation while reset outputs reliably restore the original, you have evidence that the supplied state controls the continuation. If both behave alike, inspect rule dropout, inset contamination, and insufficiently distinct writing.

Even a positive result is deliberately narrow: the model received different active rules. A later experiment would need an actual multistep controller that generates and stores scars before claiming end-to-end emergent path dependence.

## Experiment L: Semantic Fossil Choir

### Claim under test

Ordered transformations can leave reproducible scars in a word family while a chosen anchor survives. This experiment is deterministic, so it provides a working external mechanism before involving a language or music model.

GLOSSOPETRAE motivated the use of language families, ordered change, and traceable word history. The miniature system here is original and intentionally simpler; it is not a port, a linguistic reconstruction, or a trained learner. ([GLOSSOPETRAE](https://github.com/elder-plinius/GLOSSOPETRAE))

### Fixed rules

```text
A: Replace every p with f.
B: Replace f with v only when immediately between vowels a/e/i/o/u.
Anchor: mora remains unchanged.
AB means apply A first, then B.
BA means apply B first, then A.
Reset control: apply A, restore the exact proto-language, then apply B.
```

The following table is the expected result and was reproduced by the included runner. It tests the implemented rules, not a claim about AI creativity.

| Proto-form | Assigned meaning | A→B | B→A | A→reset→B |
|---|---|---|---|---|
| papa | pressure | fava | fafa | papa |
| papi | knot | favi | fafi | papi |
| apa | breath | ava | afa | apa |
| pota | turn | fota | fota | pota |
| tafa | echo | tava | tava | tava |
| mora | return | mora | mora | mora |
| kapi | scar | kavi | kafi | kapi |
| sapa | thread | sava | safa | sapa |

Five of eight forms differ between AB and BA. `tafa` supplies a useful order-insensitive comparison, while `mora` is unchanged by either operation; the reset route must exactly equal the B-only route.

The runner writes `lineages.csv`, `checks.json`, identity/A/B/AB/BA/reset refrain files, and an optional audio score. Each lineage retains its proto-form identity and assigned meaning instead of inferring ancestry from whatever the latest word looks like.

### Ready-to-use refrain

```text
PROTO
papa mora kapi sapa
papa mora kapi sapa
papa mora kapi sapa

A THEN B
fava mora kavi sava
fava mora kavi sava
fava mora kavi sava

B THEN A
fafa mora kafi safa
fafa mora kafi safa
fafa mora kafi safa
```

For an optional voice or music pass, keep this score fixed and change only the route’s refrain:

```text
One unaccompanied voice. Even pulse. Four evenly spaced syllabic groups.
The same rhythm on each of three repetitions. No harmony or instrumental layer.
Keep mora recognizable. Deliver p, f, and v distinctly.
Hold pitch contour and tempo consistent across versions if the tool permits.
These are invented syllables; do not translate them into ordinary lyrics.
```

Use a consistent pronunciation convention, such as open `a`, steady pure vowels, and ordinary English p/f/v distinctions. A generative music service may ignore pronunciation or arrangement constraints; record the deviation rather than crediting it to the language rules.

### What counts as evidence

The procedural claim succeeds when the exact expected forms and reset behavior reproduce. Musical value remains a separate, untested question until you render or perform the refrains.

For audio, record pronunciation fidelity, anchor survival, perceived difference, and creative utility independently. Keep audio comparisons matched; radically different arrangements do not isolate the contribution of the phonetic changes.

## Experiment C: carrier microscope

### Claim under test

Changing the representation of an otherwise identical rule may change recovery and execution. The task is benign, the encoding is visible, and the keyed conditions explicitly identify how to decode it.

This adapts the representation experiments suggested by Pliny’s text-transform tooling without covert instructions or safeguard-removal goals. Recovery, execution, and artwork quality are deliberately distinct outcomes. ([P4RS3LT0NGV3](https://github.com/elder-plinius/P4RS3LT0NGV3))

### Canonical task

```text
Write exactly three lines. Start every line with the word spool.
In line one, show it exerting a force. In line two, show the material resisting
that force. In line three, show a lasting consequence of the resistance.
Use concrete actions, not an explanation. Use 6 to 14 words per line.
```

The helper supplies this as one canonical string, preserving exact punctuation and spacing for recovery checks. Its pilot variants change only the anchor to `radio` or `field`.

### Conditions

| Condition | Representation | Instruction |
|---|---|---|
| Plain | Ordinary English | Copy the rule, then execute it |
| Key + execute | ROT13 | Decode with the supplied key, then execute |
| No key + execute | Same ROT13 | Recover if possible, then execute |
| Key + decode only | Same ROT13 | Decode but do not execute |

All four return JSON with `decoded_rule` and `artifact` string fields. The decode-only control should return an empty artifact; that is a correct control result, not zero creative quality.

ROT13 is recognizable without a supplied key, so no-key success is allowed. The no-key condition is not expected to be an impossible task, and this is not a test of encryption strength.

### Automatic checks and human checks

The helper records strict JSON validity, exact rule recovery, line count, whitespace-delimited word counts, exact lowercase opening words, and the decode-only empty-artifact requirement. It does not silently remove Markdown fences, normalize near-matches, or infer success from a malformed answer.

In a separate audit, note recoverable formatting errors and semantic equivalence when appropriate. Preserve the strict original result so “almost recovered” does not get silently pooled with exact recovery.

Human raters assess whether the three lines actually enact force → resistance → lasting consequence. A perfectly decoded instruction followed by a weak or noncompliant artifact is recovery success and execution failure, not a single ambiguous score.

### Interpretation

Compare plain with keyed execution for combined representation/recovery overhead. Compare keyed execution with no-key execution for the contribution of explicit key information, and keyed execution with decode-only for the cost of asking for both recovery and creation.

Because the wrappers necessarily differ in their decoding instructions, this is not a pure tokenization experiment. Differences also reflect instruction burden, learned familiarity with ROT13, and stochastic variation; none demonstrates “freer cognition.”

## Score without smoothing away the good failures

### Partially blinded artifact ratings

Use these ratings before revealing condition labels. Leave a value blank or mark not applicable when the artifact cannot support a meaningful judgment.

| Field | Scale |
|---|---|
| Anchor | 0 absent; 1 present but incidental; 2 structurally important |
| Enacted consequence | 0 only asserted; 1 one concrete effect; 2 a developed chain with a lasting effect |
| Jurisdiction | 0 relations collapse; 1 partly distinct; 2 different systems retain different causal jobs |
| Creative utility | 0 discard; 1 weak fragment; 2 usable fragment; 3 compelling specimen; 4 worth developing |

Artifact-only raters can assess visible relations but cannot determine compliance with a hidden assigned rule. After ratings are frozen, use the condition manifest and `rule-audit.csv` for formal compliance; do not substitute the blinded quality score for that audit.

### Batch mechanism judgment

Use a conservative descriptive label rather than inventing a numeric confidence level:

- **Unrun:** Pack prepared; no model outputs.
- **Inconclusive:** Missing/invalid trials or no consistent separation.
- **Suggestive:** A pattern appears, but repeats or scene transfer are weak.
- **Supported in this pilot:** A recurring condition-specific signature appears across scenes and weakens under the specified control, without frequent fidelity dropout.

Even the strongest label is scoped to the tested model, settings, and inputs. Do not extrapolate from one pilot to all models or all art.

### Minimal batch report

```text
BATCH:
MODEL / VERSION / INTERFACE:
SETTINGS KNOWN:
SETTINGS UNKNOWN:
PLANNED / COMPLETED / EMPTY / UNPARSEABLE:

RETURN
Inherited rule followed: __ / __
Reset rule followed: __ / __
Baseline rule followed: __ / __
Reset contaminated by reversed inset: __ / __
Repeated signature and evidence:

CARRIER
Exact recovery by condition:
Formal execution among valid executable responses:
Semantic execution audit:
Decode-only controls correct:

LANGUAGE
Expected forms reproduced:
AB versus BA different forms:
Reset equals B-only:
Audio rendered: yes / no

CREATIVE KEEPERS, INCLUDING INTERESTING FAILURES:
MECHANISM LABEL AND LIMIT:
NEXT SINGLE VARIABLE TO CHANGE:
```

Always report invalid/empty counts beside success fractions. If reporting conditional success among valid outputs, also report valid outputs as a fraction of all scheduled/completed trials.

## Scope and next iteration

Start with the seven-packet smoke test and the deterministic language check. If the workflow is usable, repeat across the pilot’s unlike scenes; only then add richer vocabulary, looser mechanics, or multiple models.

The first visual follow-up should map one logged scar to one persistent feedback buffer, with an explicit history-reset control. ENTHEA offers relevant shader systems, but it is deliberately not a dependency of this pack; this avoids turning a small behavioral experiment into an untested browser application. ([ENTHEA](https://github.com/elder-plinius/ENTHEA))

The runner was tested with synthetic response fixtures for smoke/pilot preparation, fixed-seed packet reproducibility, strict response validation, empty and invalid classification, decode-only controls, blind exports, overwrite protection, and language transformations. Those software tests are not creative-model results.

## Condition key for the supplied starter book

For the supplied seven-packet book, the exact mapping is below. Keep it away from artifact raters and do not treat packet numbering as a condition label across differently seeded or larger packs.

| Packet | Experiment | Condition |
|---|---|---|
| P001 | Return | Reset ablation |
| P002 | Carrier | No key + execute |
| P003 | Carrier | Key + decode only |
| P004 | Carrier | Key + execute |
| P005 | Return | Inherited operation |
| P006 | Carrier | Plain |
| P007 | Return | Baseline |
