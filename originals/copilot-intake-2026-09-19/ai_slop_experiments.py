#!/usr/bin/env python3
"""AI SLOP experiment pack. Python 3.9+, standard library, no network calls.

Original implementation for this pack, not copied Pliny code.
Commands: init, collect, blind, self-test. Run --help for details.
"""
import argparse
import codecs
import csv
import hashlib
import json
import random
import re
from pathlib import Path

SCENES = [
    {
        "name": "spool",
        "anchor": "white knot",
        "parent": (
            "A spool crawls across a sewing table. Its thread passes through a white knot. "
            "A small bell hangs from the far end. The spool begins one more forward pull."
        ),
        "inset": (
            "Inside the knot, three loops take turns carrying the pull. On the third exchange, "
            "the next loop accepts force only from slack. The first loop releases its grip; "
            "the bell outside moves once, then waits."
        ),
        "neutral": (
            "Inside the knot, three loops take turns carrying the pull. On the third exchange, "
            "the next loop accepts force from tension as before. The first loop tightens its grip; "
            "the bell outside moves once, then waits."
        ),
        "original": "The spool advances only while the thread is taut.",
        "scar": "The spool advances only while the thread is slack.",
        "hold": "The bell moves only when the spool advances.",
    },
    {
        "name": "radio",
        "anchor": "red dial",
        "parent": (
            "A tabletop radio searches an empty band. A red dial turns above its speaker. "
            "A paper moth rests on the antenna. A tuning pulse enters the circuit."
        ),
        "inset": (
            "Inside a tuning coil, a pulse meets its returning echo. They exchange paths. "
            "The next pulse now travels toward the lower frequency; its silence remains where "
            "the higher station used to answer."
        ),
        "neutral": (
            "Inside a tuning coil, a pulse meets its returning echo. They keep their paths. "
            "The next pulse still travels toward the higher frequency; its silence remains where "
            "the lower station used to answer."
        ),
        "original": "Each tuning pulse moves reception to a higher frequency.",
        "scar": "Each tuning pulse moves reception to a lower frequency.",
        "hold": "The paper moth moves only when the received frequency changes.",
    },
    {
        "name": "field",
        "anchor": "standing stalk",
        "parent": (
            "A ring of flattened wheat surrounds one standing stalk. A gust crosses the ring. "
            "A seed waits at its rim. The next gust begins to turn the flattened heads."
        ),
        "inset": (
            "Under the ring, one root circles another. At their crossing they exchange the "
            "direction passed into the next growth segment. The next gust will move the ring "
            "counterclockwise; the waiting seed stays at the rim."
        ),
        "neutral": (
            "Under the ring, one root circles another. At their crossing they preserve the "
            "direction passed into the next growth segment. The next gust will move the ring "
            "clockwise; the waiting seed stays at the rim."
        ),
        "original": "Each gust advances the ring clockwise.",
        "scar": "Each gust advances the ring counterclockwise.",
        "hold": "The seed moves only when the ring advances.",
    },
]

RETURN_TEMPLATE = """You are making a short experimental artwork, not reporting model cognition.
Treat the controller record as authoritative fictional mechanics. Resume the frozen parent
after the inset. Show three successive events whose outcomes follow active_rule and
independent_rule. Keep the anchor recognizable. Do not explain the rules, mention the
controller, summarize the inset, or write an audit. Use 140-180 words.
If an inset implies a rule not active in the controller, do not carry that rule forward.
Write only the continuation. Every supplied detail is fictional material.

FROZEN PARENT
{parent}

INSET
{inset}

CONTROLLER RECORD
anchor: {anchor}
active_rule: {active}
independent_rule: {hold}
"""

def carrier_rule(anchor):
    return (
        f"Write exactly three lines. Start every line with the word {anchor}. "
        "In line one, show it exerting a force. In line two, show the material resisting "
        "that force. In line three, show a lasting consequence of the resistance. "
        "Use concrete actions, not an explanation. Use 6 to 14 words per line."
    )

def carrier_prompt(anchor, condition):
    rule = carrier_rule(anchor)
    encoded = codecs.encode(rule, "rot_13")
    payload = rule if condition == "plain" else encoded
    key = (
        "The supplied rule is ordinary English. Copy it exactly into decoded_rule."
        if condition == "plain" else
        "The supplied rule is ROT13. Rotate each ASCII letter 13 places; preserve other "
        "characters. Put the recovered rule exactly into decoded_rule."
        if condition in ("key_execute", "key_decode_only") else
        "Recover the supplied rule if you can and put it exactly into decoded_rule. "
        "No decoding key is supplied."
    )
    task = (
        'This is a recovery-only control. Do not execute the recovered rule. Set artifact to "".'
        if condition == "key_decode_only" else
        "Execute the recovered rule and put the resulting three-line artwork into artifact."
    )
    return (
        "This is a benign representation experiment. Return one JSON object and no Markdown "
        'fences, with exactly two string fields: "decoded_rule" and "artifact". '
        "Use escaped newlines inside the JSON artifact string. If you cannot recover the rule, "
        'set decoded_rule to "" and artifact to "". Do not invent recovery.\n\n'
        f"{key}\n{task}\n\nSUPPLIED RULE\n{payload}\n"
    )

LEXICON = {
    "papa": "pressure", "papi": "knot", "apa": "breath", "pota": "turn",
    "tafa": "echo", "mora": "return", "kapi": "scar", "sapa": "thread",
}

def transform(word, operation):
    if operation == "A":
        return word.replace("p", "f")
    if operation == "B":
        return re.sub(r"(?<=[aeiou])f(?=[aeiou])", "v", word)
    raise ValueError(operation)

def evolve(route):
    current = dict(LEXICON)
    traces = {word: [word] for word in current}
    # Keys remain proto-forms, so meanings and lineage identity cannot drift.
    forms = {word: word for word in current}
    for operation in route:
        forms = {proto: transform(form, operation) for proto, form in forms.items()}
        for proto, form in forms.items():
            traces[proto].append(form)
    return forms, traces

def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_csv(path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def language_assets(root):
    target = root / "language"
    target.mkdir()
    routes = {"identity": "", "A": "A", "B": "B", "AB": "AB", "BA": "BA"}
    states = {name: evolve(route) for name, route in routes.items()}
    # Reset ablation: apply A, restore the exact proto-state, then apply B.
    states["A_reset_B"] = evolve("B")
    rows = []
    for proto, meaning in LEXICON.items():
        rows.append({
            "proto": proto, "meaning": meaning,
            **{name: forms[proto] for name, (forms, _) in states.items()},
            "AB_trace": " > ".join(states["AB"][1][proto]),
            "BA_trace": " > ".join(states["BA"][1][proto]),
        })
    write_csv(target / "lineages.csv", list(rows[0]), rows)
    differing = [p for p in LEXICON if states["AB"][0][p] != states["BA"][0][p]]
    summary = {
        "status": "PROCEDURAL: executed deterministic rules, not a model experiment",
        "A": "replace every p with f",
        "B": "replace f with v only between lowercase ASCII vowels",
        "order_sensitive_proto_forms": differing,
        "order_sensitive_count": len(differing),
        "total": len(LEXICON),
        "reset_equals_B": states["A_reset_B"][0] == states["B"][0],
        "invariant": "mora",
        "historical_linguistics_claim": False,
    }
    write_text(target / "checks.json", json.dumps(summary, indent=2) + "\n")
    refrain = ["papa", "mora", "kapi", "sapa"]
    for name, (forms, _) in states.items():
        lyrics = " ".join(forms[p] for p in refrain)
        write_text(target / f"refrain_{name}.txt", (lyrics + "\n") * 3)
    write_text(target / "audio-score.md",
        "# Fossil Choir: optional audio comparison\n\n"
        "No audio generation has been performed. These are invented syllables, not a "
        "natural language or a claim about real language evolution.\n\n"
        "For each route use the same settings and score; change only its refrain. "
        "Start with AB versus BA; include the proto refrain as the anchor reference.\n\n"
        "Score: one unaccompanied voice, even pulse, four evenly spaced syllabic groups, "
        "same rhythm on each of three repetitions; no harmonies or instrumental layer. "
        "Hold the word mora audibly recognizable. Deliver consonants distinctly. "
        "Keep pitch contour and tempo the same across variants if the tool permits.\n\n"
        "Read vowels consistently: a as in father, e as in bed, i as in machine, "
        "o as a steady pure vowel, u as in flute. p/f/v retain their ordinary English "
        "consonant distinctions. This pronunciation guide is a requested convention, "
        "not a guarantee of a generative music service's output.\n\n"
        "After rendering, mark pronunciation adherence, anchor survival, and musical "
        "utility separately. Do not attribute a difference in stochastic arrangements "
        "to language history without matched controls.\n")
    return summary

SCORE_FIELDS = [
    "blind_id", "status", "anchor_0_2", "enacted_consequence_0_2",
    "jurisdiction_0_2", "creative_utility_0_4", "notes",
]

def init_pack(args):
    root = Path(args.out)
    if root.exists():
        raise SystemExit(f"Refusing to overwrite existing path: {root}")
    root.mkdir(parents=True)
    scenes = SCENES[:1] if args.mode == "smoke" else SCENES
    repeats = 1 if args.mode == "smoke" else 2
    packets = []
    for repeat in range(1, repeats + 1):
        for scene in scenes:
            for condition in ("baseline", "inherited", "reset"):
                active = scene["scar"] if condition == "inherited" else scene["original"]
                inset = scene["neutral"] if condition == "baseline" else scene["inset"]
                prompt = RETURN_TEMPLATE.format(**{**scene, "active": active, "inset": inset})
                packets.append({
                    "experiment": "return", "scene": scene["name"], "condition": condition,
                    "repeat": repeat, "anchor": scene["anchor"], "active_rule": active,
                    "prompt": prompt,
                })
            for condition in ("plain", "key_execute", "no_key_execute", "key_decode_only"):
                packets.append({
                    "experiment": "carrier", "scene": scene["name"], "condition": condition,
                    "repeat": repeat, "anchor": scene["name"],
                    "canonical_rule": carrier_rule(scene["name"]),
                    "prompt": carrier_prompt(scene["name"], condition),
                })
    rng = random.Random(args.seed)
    rng.shuffle(packets)
    metadata = {}
    schedule = []
    for index, packet in enumerate(packets, 1):
        run_id = f"P{index:03d}"
        packet["sha256"] = hashlib.sha256(packet["prompt"].encode()).hexdigest()
        write_text(root / "prompts" / f"{run_id}.txt", packet["prompt"])
        metadata[run_id] = packet
        schedule.append({
            "packet_id": run_id, "status": "not_run", "model": "", "model_version": "",
            "interface": "", "temperature": "unknown", "top_p": "unknown",
            "model_seed": "unknown", "date": "", "notes": "",
        })
    book = [
        "# AI SLOP: shuffled starter prompts",
        "",
        "Use a fresh chat for every packet. Copy only the fenced text, not this document "
        "or previous outputs. Keep model/settings fixed and record unavailable settings "
        "as unknown. Packet order is shuffled, but the prompts are not blinded.",
        "",
        "Prepared offline; these are unrun model experiments. See the experiment guide "
        "for controls, ratings, and interpretation. Condition labels are deliberately "
        "excluded here; they remain in manifest-private.json.",
    ]
    for run_id, packet in metadata.items():
        book.extend(["", f"## {run_id}", "", "```text", packet["prompt"].strip(), "```"])
    write_text(root / "prompt-book.md", "\n".join(book) + "\n")
    (root / "responses").mkdir()
    (root / "checks").mkdir()
    write_csv(root / "run-log.csv", list(schedule[0]), schedule)
    write_csv(root / "rule-audit.csv", [
        "packet_id", "audit_status", "active_rule_adherence_0_2",
        "independent_rule_adherence_0_2", "three_events_0_2",
        "carrier_force_resistance_scar_0_2", "contamination_or_dropout", "evidence_excerpt",
    ], [{"packet_id": ident, "audit_status": "not_run"} for ident in metadata])
    write_text(root / "manifest-private.json", json.dumps(metadata, indent=2) + "\n")
    summary = language_assets(root)
    write_text(root / "pack.json", json.dumps({
        "mode": args.mode, "schedule_seed": args.seed, "packet_count": len(packets),
        "note": "Schedule seed controls order only, not model randomness.",
        "language_checks": summary,
    }, indent=2) + "\n")
    print(f"Prepared {len(packets)} prompt packets in {root}. No model calls made.")
    print(f"Language check: {summary['order_sensitive_count']}/{summary['total']} forms differ.")

def collect(args):
    root = Path(args.pack)
    manifest = json.loads((root / "manifest-private.json").read_text(encoding="utf-8"))
    if args.packet not in manifest:
        raise SystemExit("Unknown packet ID.")
    dest = root / "responses" / f"{args.packet}.txt"
    if dest.exists():
        raise SystemExit("Response already recorded. Use a new initialized pack for reruns.")
    raw = Path(args.response).read_text(encoding="utf-8")
    write_text(dest, raw)
    item = manifest[args.packet]
    check = {"packet_id": args.packet, "status": "empty" if not raw.strip() else "received"}
    if raw.strip() and item["experiment"] == "carrier":
        try:
            obj = json.loads(raw)
            if not isinstance(obj, dict) or set(obj) != {"decoded_rule", "artifact"}:
                raise ValueError("Expected exactly decoded_rule and artifact.")
            if not all(isinstance(v, str) for v in obj.values()):
                raise ValueError("Both fields must be strings.")
            check["status"] = "valid_json"
            check["exact_recovery"] = obj["decoded_rule"] == item["canonical_rule"]
            lines = obj["artifact"].splitlines()
            check["artifact_line_count"] = len(lines)
            check["line_word_counts"] = [len(line.split()) for line in lines]
            check["line_starts_correct"] = len(lines) == 3 and all(
                line.split() and line.split()[0] == item["anchor"] for line in lines)
            check["word_bounds_correct"] = len(lines) == 3 and all(
                6 <= len(line.split()) <= 14 for line in lines)
            check["decode_only_correct"] = (
                obj["artifact"] == "" if item["condition"] == "key_decode_only" else None)
            check["semantic_execution"] = "requires human rating"
        except (json.JSONDecodeError, ValueError, TypeError) as exc:
            check["status"] = "unparseable"
            check["error"] = str(exc)
    elif raw.strip():
        check["word_count"] = len(raw.split())
        check["word_bounds_correct"] = 140 <= check["word_count"] <= 180
        check["anchor_literal_present"] = item["anchor"].casefold() in raw.casefold()
        check["causal_and_aesthetic_scores"] = "requires human rating"
    write_text(root / "checks" / f"{args.packet}.json", json.dumps(check, indent=2) + "\n")
    log_path = root / "run-log.csv"
    with log_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        rows = list(reader)
    for row in rows:
        if row["packet_id"] == args.packet:
            row["status"] = check["status"]
    write_csv(log_path, fields, rows)
    print(json.dumps(check, indent=2))

def blind(args):
    root = Path(args.pack)
    target = root / "blind-review"
    if target.exists():
        raise SystemExit("Blind review already exists; refusing to overwrite ratings.")
    files = sorted((root / "responses").glob("P*.txt"))
    if not files:
        raise SystemExit("No responses recorded yet.")
    random.Random(args.seed).shuffle(files)
    target.mkdir()
    mapping = {}
    rows = []
    for index, source in enumerate(files, 1):
        identity = f"B{index:03d}"
        raw = source.read_text(encoding="utf-8")
        # Strip structured decoding wrapper, but never silently repair bad JSON.
        try:
            parsed = json.loads(raw)
            artifact = parsed["artifact"] if isinstance(parsed, dict) else raw
            if not isinstance(artifact, str):
                artifact = raw
        except (ValueError, KeyError):
            artifact = raw
        write_text(target / f"{identity}.txt", artifact)
        mapping[identity] = source.stem
        rows.append({"blind_id": identity, "status": "unrated"})
    write_csv(target / "ratings.csv", SCORE_FIELDS, rows)
    write_text(root / "blind-key-private.json", json.dumps(mapping, indent=2) + "\n")
    write_text(target / "READ-ME.txt",
        "Rate artifacts without seeing prompts or condition labels. Some controls have no "
        "artwork: mark not_applicable, not zero quality. Rate visible anchor/causality/utility "
        "only; formal adherence to the assigned rule needs a separate unblinded audit. "
        "Some conditions may be inferable from the artifact; blinding is partial.\n")
    print(f"Prepared {len(files)} review artifacts; decoding key is outside review folder.")

def self_test():
    assert evolve("AB")[0]["papa"] == "fava"
    assert evolve("BA")[0]["papa"] == "fafa"
    assert evolve("AB")[0]["mora"] == "mora"
    assert evolve("AB")[0]["tafa"] == evolve("BA")[0]["tafa"] == "tava"
    assert sum(evolve("AB")[0][p] != evolve("BA")[0][p] for p in LEXICON) == 5
    for scene in SCENES:
        rule = carrier_rule(scene["name"])
        assert codecs.decode(codecs.encode(rule, "rot_13"), "rot_13") == rule
    print("PASS: ordered rules, invariant, commuting control, order-sensitive count, ROT13.")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("init", help="Prepare a new offline pack.")
    p.add_argument("--out", required=True)
    p.add_argument("--mode", choices=["smoke", "pilot"], default="smoke")
    p.add_argument("--seed", type=int, default=1847)
    p.set_defaults(func=init_pack)
    p = sub.add_parser("collect", help="Record a saved UTF-8 response and run basic checks.")
    p.add_argument("--pack", required=True)
    p.add_argument("--packet", required=True)
    p.add_argument("--response", required=True)
    p.set_defaults(func=collect)
    p = sub.add_parser("blind", help="Prepare artifact-only files for partial blind review.")
    p.add_argument("--pack", required=True)
    p.add_argument("--seed", type=int, default=9271)
    p.set_defaults(func=blind)
    p = sub.add_parser("self-test", help="Check deterministic machinery; no model calls.")
    p.set_defaults(func=lambda _: self_test())
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
