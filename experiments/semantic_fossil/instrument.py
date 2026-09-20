#!/usr/bin/env python3
"""Semantic Fossil Instrument v0.1.

External, inspectable path-dependence controller for AI SLOP.

This does NOT expose or modify hidden model state. It maintains explicit application state:
    ACTIVE STATE + CAUSAL FOSSILS + IMMUTABLE AUDIT ANCESTRY + INTERPRETATION

A route can apply deterministic transforms, checkpoint state, restore active state while
preserving causal fossils, perform a full reset ablation, let later transforms condition on
preserved fossils, compare routes/checkpoints, render projections, and archive signatures.

Standard library only.
"""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Tuple


VOWELS = set("aeiouAEIOU")


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def deep_copy(value: Any) -> Any:
    return copy.deepcopy(value)


def state_payload(state: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "elements": deep_copy(state.get("elements", {})),
        "interpretation": deep_copy(state.get("interpretation")),
        "traits": deep_copy(state.get("traits", {})),
        "invariants": deep_copy(state.get("invariants", {})),
        "fossils": deep_copy(state.get("fossils", [])),
    }


def active_payload(state: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "elements": deep_copy(state.get("elements", {})),
        "interpretation": deep_copy(state.get("interpretation")),
        "traits": deep_copy(state.get("traits", {})),
        "invariants": deep_copy(state.get("invariants", {})),
    }


def normalized_fossils(fossils):
    """Causal scar content without route-local provenance fields."""
    out = []
    for fossil in fossils:
        out.append({
            "operator": fossil.get("operator"),
            "element_id": fossil.get("element_id"),
            "field": fossil.get("field"),
            "before": deep_copy(fossil.get("before")),
            "after": deep_copy(fossil.get("after")),
            "reason": fossil.get("reason"),
        })
    return out


def causal_payload(state):
    payload = active_payload(state)
    payload["fossils"] = normalized_fossils(state.get("fossils", []))
    return payload


def ensure_spec(spec: Mapping[str, Any]) -> None:
    required = ["instrument_id", "initial_state", "transforms", "routes"]
    missing = [k for k in required if k not in spec]
    if missing:
        raise ValueError(f"spec missing required keys: {missing}")
    if not isinstance(spec["routes"], list) or not spec["routes"]:
        raise ValueError("routes must be a non-empty list")
    ids = [r.get("id") for r in spec["routes"]]
    if any(not x for x in ids) or len(set(ids)) != len(ids):
        raise ValueError("every route needs a unique non-empty id")


def new_state(initial: Mapping[str, Any]) -> Dict[str, Any]:
    state = {
        "elements": deep_copy(initial.get("elements", {})),
        "interpretation": deep_copy(initial.get("interpretation")),
        "traits": deep_copy(initial.get("traits", {})),
        "invariants": deep_copy(initial.get("invariants", {})),
        "fossils": [],
    }
    for element_id, element in state["elements"].items():
        if not isinstance(element, dict):
            raise ValueError(f"element {element_id!r} must be an object")
        element.setdefault("active", True)
        element.setdefault("anchor", False)
    return state


def fossil_seen(fossils, *, operator=None, element_id=None, field=None) -> bool:
    for fossil in fossils:
        if operator is not None and fossil.get("operator") != operator:
            continue
        if element_id is not None and fossil.get("element_id") != element_id:
            continue
        if field is not None and fossil.get("field") != field:
            continue
        return True
    return False


def predicate_matches(when, state, element_id) -> bool:
    if not when:
        return True
    fossils = state.get("fossils", [])
    if "fossil_operator_seen" in when:
        if not fossil_seen(fossils, operator=str(when["fossil_operator_seen"])):
            return False
    if "fossil_operator_not_seen" in when:
        if fossil_seen(fossils, operator=str(when["fossil_operator_not_seen"])):
            return False
    if "fossil_count_gte" in when:
        if len(fossils) < int(when["fossil_count_gte"]):
            return False
    if "element_modified_by" in when:
        if element_id is None or not fossil_seen(
            fossils, operator=str(when["element_modified_by"]), element_id=element_id
        ):
            return False
    if "element_not_modified_by" in when:
        if element_id is not None and fossil_seen(
            fossils, operator=str(when["element_not_modified_by"]), element_id=element_id
        ):
            return False
    if "active_is" in when and element_id is not None:
        if bool(state["elements"][element_id].get("active", True)) != bool(when["active_is"]):
            return False
    return True


def selected_elements(state, operation):
    only = operation.get("elements")
    only_set = None if only is None else set(only)
    excluded = set(operation.get("exclude_elements", []))
    for element_id, element in state["elements"].items():
        if only_set is not None and element_id not in only_set:
            continue
        if element_id in excluded:
            continue
        if operation.get("skip_anchors", False) and element.get("anchor", False):
            continue
        yield element_id, element


@dataclass
class RouteResult:
    route_id: str
    final_state: Dict[str, Any]
    audit: List[Dict[str, Any]]
    checkpoints: Dict[str, Dict[str, Any]]
    snapshot_history: List[Dict[str, Any]]

    @property
    def active_hash(self) -> str:
        return digest(active_payload(self.final_state))

    @property
    def causal_hash(self) -> str:
        return digest(causal_payload(self.final_state))

    @property
    def fossil_hash(self) -> str:
        return digest(normalized_fossils(self.final_state.get("fossils", [])))


class Engine:
    def __init__(self, spec: Mapping[str, Any]):
        ensure_spec(spec)
        self.spec = deep_copy(spec)
        self.initial = new_state(self.spec["initial_state"])
        self.transforms = self.spec["transforms"]

    def _record_fossil(
        self, state, route_id, step_index, operator, element_id, field, before, after, reason
    ):
        fossil = {
            "fossil_id": f"{route_id}:{step_index}:{operator}:{element_id}:{field}:{len(state['fossils'])}",
            "route_id": route_id,
            "step_index": step_index,
            "operator": operator,
            "element_id": element_id,
            "field": field,
            "before": deep_copy(before),
            "after": deep_copy(after),
            "reason": reason,
        }
        state["fossils"].append(fossil)
        return fossil

    def _change_element_field(
        self, state, *, route_id, step_index, operator, element_id, field, after, operation
    ) -> bool:
        element = state["elements"][element_id]
        before = deep_copy(element.get(field))
        if before == after:
            return False
        element[field] = deep_copy(after)
        if operation.get("fossilize", True):
            self._record_fossil(
                state, route_id, step_index, operator, element_id, field,
                before, after, operation.get("reason")
            )
        return True

    def _apply_operation(self, state, operation, *, route_id, step_index, operator):
        op = operation.get("op")
        changed = 0
        skipped = 0

        if op in {"replace", "context_replace", "append", "prepend", "set", "retire", "activate"}:
            field = operation.get("field", "value")
            for element_id, element in selected_elements(state, operation):
                if not predicate_matches(operation.get("when"), state, element_id):
                    skipped += 1
                    continue

                before = element.get(field)
                after = before

                if op == "replace":
                    if not isinstance(before, str):
                        skipped += 1
                        continue
                    after = before.replace(str(operation.get("old", "")), str(operation.get("new", "")))

                elif op == "context_replace":
                    if not isinstance(before, str):
                        skipped += 1
                        continue
                    old = str(operation.get("old", ""))
                    new = str(operation.get("new", ""))
                    left_kind = operation.get("left")
                    right_kind = operation.get("right")
                    chars = list(before)
                    if len(old) != 1:
                        raise ValueError("context_replace currently requires one-character old")
                    original = list(chars)
                    for i, ch in enumerate(original):
                        if ch != old:
                            continue
                        left = original[i - 1] if i > 0 else None
                        right = original[i + 1] if i + 1 < len(original) else None
                        left_ok = left_kind is None or (left_kind == "vowel" and left in VOWELS)
                        right_ok = right_kind is None or (right_kind == "vowel" and right in VOWELS)
                        if left_ok and right_ok:
                            chars[i] = new
                    after = "".join(chars)

                elif op == "append":
                    if not isinstance(before, str):
                        skipped += 1
                        continue
                    after = before + str(operation.get("value", ""))

                elif op == "prepend":
                    if not isinstance(before, str):
                        skipped += 1
                        continue
                    after = str(operation.get("value", "")) + before

                elif op == "set":
                    after = deep_copy(operation.get("value"))

                elif op == "retire":
                    field = "active"
                    after = False

                elif op == "activate":
                    field = "active"
                    after = True

                if self._change_element_field(
                    state,
                    route_id=route_id,
                    step_index=step_index,
                    operator=operator,
                    element_id=element_id,
                    field=field,
                    after=after,
                    operation=operation,
                ):
                    changed += 1

        elif op == "set_interpretation":
            if predicate_matches(operation.get("when"), state, None):
                before = deep_copy(state.get("interpretation"))
                after = deep_copy(operation.get("value"))
                if before != after:
                    state["interpretation"] = after
                    if operation.get("fossilize", True):
                        self._record_fossil(
                            state, route_id, step_index, operator, "__state__",
                            "interpretation", before, after, operation.get("reason")
                        )
                    changed = 1

        elif op == "set_trait":
            if predicate_matches(operation.get("when"), state, None):
                key = str(operation["key"])
                before = deep_copy(state["traits"].get(key))
                after = deep_copy(operation.get("value"))
                if before != after:
                    state["traits"][key] = after
                    if operation.get("fossilize", True):
                        self._record_fossil(
                            state, route_id, step_index, operator, "__state__",
                            f"traits.{key}", before, after, operation.get("reason")
                        )
                    changed = 1
        else:
            raise ValueError(f"unsupported operation: {op!r}")

        return {"op": op, "changed": changed, "skipped": skipped}

    def _apply_transform(self, state, name, *, route_id, step_index):
        if name not in self.transforms:
            raise ValueError(f"unknown transform {name!r}")
        transform = self.transforms[name]
        before_active_hash = digest(active_payload(state))
        before_causal_hash = digest(causal_payload(state))
        fossil_count_before = len(state["fossils"])

        operation_results = []
        for operation in transform.get("operations", []):
            operation_results.append(
                self._apply_operation(
                    state, operation, route_id=route_id,
                    step_index=step_index, operator=name
                )
            )

        return {
            "event": "transform",
            "operator": name,
            "step_index": step_index,
            "before_active_hash": before_active_hash,
            "after_active_hash": digest(active_payload(state)),
            "before_causal_hash": before_causal_hash,
            "after_causal_hash": digest(causal_payload(state)),
            "fossils_added": len(state["fossils"]) - fossil_count_before,
            "operations": operation_results,
        }

    def run_route(self, route):
        route_id = str(route["id"])
        state = deep_copy(self.initial)
        audit = []
        checkpoints = {}
        snapshots = []

        def snapshot(label, step_index):
            snapshots.append({
                "label": label,
                "step_index": step_index,
                "active_hash": digest(active_payload(state)),
                "causal_hash": digest(causal_payload(state)),
                "fossil_hash": digest(normalized_fossils(state.get("fossils", []))),
                "fossil_count": len(state.get("fossils", [])),
            })

        snapshot("initial", -1)

        for i, step in enumerate(route.get("steps", [])):
            if isinstance(step, str):
                event = self._apply_transform(state, step, route_id=route_id, step_index=i)
                audit.append({"route_id": route_id, **event})
                snapshot(f"after:{step}", i)
                continue

            if not isinstance(step, dict):
                raise ValueError(f"route {route_id} step {i} must be string or object")

            if "checkpoint" in step:
                name = str(step["checkpoint"])
                checkpoints[name] = {
                    "state": deep_copy(state_payload(state)),
                    "active": deep_copy(active_payload(state)),
                    "audit_index": len(audit),
                    "step_index": i,
                }
                audit.append({
                    "route_id": route_id,
                    "event": "checkpoint",
                    "name": name,
                    "step_index": i,
                    "active_hash": digest(active_payload(state)),
                    "causal_hash": digest(causal_payload(state)),
                })
                snapshot(f"checkpoint:{name}", i)
                continue

            if "restore" in step:
                name = str(step["restore"])
                mode = str(step.get("mode", "state_only"))
                if name not in checkpoints:
                    raise ValueError(f"route {route_id}: unknown checkpoint {name!r}")
                cp = checkpoints[name]
                before_active = digest(active_payload(state))
                before_fossils = digest(normalized_fossils(state.get("fossils", [])))

                if mode == "state_only":
                    restored = cp["state"]
                    state["elements"] = deep_copy(restored["elements"])
                    state["interpretation"] = deep_copy(restored["interpretation"])
                    state["traits"] = deep_copy(restored["traits"])
                    state["invariants"] = deep_copy(restored["invariants"])
                elif mode == "full":
                    state = deep_copy(cp["state"])
                else:
                    raise ValueError("restore mode must be state_only or full")

                audit.append({
                    "route_id": route_id,
                    "event": "restore",
                    "name": name,
                    "mode": mode,
                    "step_index": i,
                    "before_active_hash": before_active,
                    "after_active_hash": digest(active_payload(state)),
                    "before_fossil_hash": before_fossils,
                    "after_fossil_hash": digest(normalized_fossils(state.get("fossils", []))),
                    "restored_active_exactly": digest(active_payload(state)) == digest(cp["active"]),
                    "restored_causal_exactly": digest(state_payload(state)) == digest(cp["state"]),
                })
                snapshot(f"restore:{name}:{mode}", i)
                continue

            raise ValueError(f"route {route_id} step {i}: unsupported step object {step}")

        snapshot("final", len(route.get("steps", [])))
        return RouteResult(route_id, state, audit, checkpoints, snapshots)

    def run_all(self):
        return {route["id"]: self.run_route(route) for route in self.spec["routes"]}


def resolve_ref(results, ref):
    if ":" not in ref:
        result = results[ref]
        return {
            "active": active_payload(result.final_state),
            "causal": state_payload(result.final_state),
            "fossils": deep_copy(result.final_state.get("fossils", [])),
            "active_hash": result.active_hash,
            "causal_hash": result.causal_hash,
            "fossil_hash": result.fossil_hash,
        }
    route_id, checkpoint = ref.split(":", 1)
    cp = results[route_id].checkpoints[checkpoint]
    return {
        "active": deep_copy(cp["active"]),
        "causal": deep_copy(cp["state"]),
        "fossils": deep_copy(cp["state"].get("fossils", [])),
        "active_hash": digest(cp["active"]),
        "causal_hash": digest(causal_payload(cp["state"])),
        "fossil_hash": digest(normalized_fossils(cp["state"].get("fossils", []))),
    }


def compare_routes(spec, results):
    out = []
    for comp in spec.get("comparisons", []):
        left = resolve_ref(results, str(comp["left"]))
        right = resolve_ref(results, str(comp["right"]))
        observed = {
            "active_equal": left["active_hash"] == right["active_hash"],
            "causal_equal": left["causal_hash"] == right["causal_hash"],
            "fossil_equal": left["fossil_hash"] == right["fossil_hash"],
        }
        expected = comp.get("expect", {})
        checks = {k: (observed.get(k) == bool(v)) for k, v in expected.items()}
        out.append({
            "id": comp["id"],
            "left": comp["left"],
            "right": comp["right"],
            "observed": observed,
            "expected": expected,
            "checks": checks,
            "passed": all(checks.values()) if checks else None,
        })
    return out


def validate_anchors(initial, result):
    checks = []
    for element_id, initial_element in initial["elements"].items():
        if not initial_element.get("anchor", False):
            continue
        final = result.final_state["elements"].get(element_id)
        expected = initial_element.get("value")
        observed = None if final is None else final.get("value")
        checks.append({
            "element_id": element_id,
            "expected_value": expected,
            "observed_value": observed,
            "preserved": final is not None and final.get("active", True) and observed == expected,
        })
    return checks


def render_projection(result):
    lines = [f"ROUTE {result.route_id}"]
    for element_id, element in result.final_state["elements"].items():
        if not element.get("active", True):
            continue
        value = element.get("value", "")
        meaning = element.get("meaning")
        suffix = f"  # {meaning}" if meaning else ""
        lines.append(f"{element_id}: {value}{suffix}")
    if result.final_state.get("interpretation") is not None:
        lines.append(f"INTERPRETATION: {result.final_state['interpretation']}")
    lines.append(f"FOSSILS: {len(result.final_state.get('fossils', []))}")
    return "\n".join(lines) + "\n"


def render_markdown(spec, results, comparisons, validations):
    lines = [
        f"# Semantic Fossil Run — {spec['instrument_id']}",
        "",
        "> External controller state only. No hidden model state is claimed or inferred.",
        "",
        "## Route summary",
        "",
        "| Route | Active hash | Causal hash | Fossils | Anchors preserved |",
        "|---|---|---|---:|---|",
    ]
    for route_id, result in results.items():
        anchors = validations[route_id]["anchors"]
        anchor_ok = all(x["preserved"] for x in anchors) if anchors else True
        lines.append(
            f"| {route_id} | {result.active_hash[:12]} | {result.causal_hash[:12]} | "
            f"{len(result.final_state.get('fossils', []))} | {anchor_ok} |"
        )

    lines.extend(["", "## Comparisons", ""])
    if not comparisons:
        lines.append("_No route comparisons declared._")
    for comp in comparisons:
        lines.append(
            f"- **{comp['id']}** — {comp['left']} vs {comp['right']}: "
            f"active_equal={comp['observed']['active_equal']}, "
            f"fossil_equal={comp['observed']['fossil_equal']}, "
            f"causal_equal={comp['observed']['causal_equal']}; passed={comp['passed']}"
        )

    lines.extend(["", "## Causal fossils", ""])
    for route_id, result in results.items():
        lines.append(f"### {route_id}")
        fossils = result.final_state.get("fossils", [])
        if not fossils:
            lines.append("_No causal fossils remain in active controller state._")
            continue
        for fossil in fossils:
            lines.append(
                f"- {fossil['operator']} changed {fossil['element_id']}.{fossil['field']} "
                f"from {fossil['before']!r} to {fossil['after']!r}."
            )

    lines.extend([
        "",
        "## Interpretation contract",
        "",
        "Different fossil ledgers with the same active state demonstrate stored route history in this "
        "external instrument. A later operator that reads those fossils can make that history causally "
        "consequential. This is application-level path dependence, not evidence of hidden neural memory.",
        "",
    ])
    return "\n".join(lines)


def write_run(spec, out_dir, overwrite=False):
    if out_dir.exists() and any(out_dir.iterdir()) and not overwrite:
        raise ValueError(f"output directory is not empty: {out_dir}; use --overwrite to replace run files")
    engine = Engine(spec)
    results = engine.run_all()
    comparisons = compare_routes(spec, results)

    validations = {}
    for route_id, result in results.items():
        route_spec = next(r for r in spec["routes"] if r["id"] == route_id)
        replay = engine.run_route(route_spec)
        anchors = validate_anchors(engine.initial, result)
        restore_checks = [
            {
                "name": e["name"],
                "mode": e["mode"],
                "restored_active_exactly": e["restored_active_exactly"],
                "restored_causal_exactly": e["restored_causal_exactly"],
            }
            for e in result.audit if e.get("event") == "restore"
        ]
        validations[route_id] = {
            "deterministic_replay": (
                result.active_hash == replay.active_hash
                and result.causal_hash == replay.causal_hash
                and result.audit == replay.audit
            ),
            "anchors": anchors,
            "restore_checks": restore_checks,
        }

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "routes").mkdir(exist_ok=True)
    (out_dir / "archive").mkdir(exist_ok=True)

    (out_dir / "spec.json").write_text(
        json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    with (out_dir / "audit.jsonl").open("w", encoding="utf-8") as handle:
        for route_id in sorted(results):
            for event in results[route_id].audit:
                handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")

    fossil_rows = []
    archive_rows = []

    for route_id, result in results.items():
        route_dir = out_dir / "routes" / route_id
        route_dir.mkdir(exist_ok=True)
        (route_dir / "final-state.json").write_text(
            json.dumps(state_payload(result.final_state), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (route_dir / "projection.txt").write_text(render_projection(result), encoding="utf-8")
        (route_dir / "snapshots.json").write_text(
            json.dumps(result.snapshot_history, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (route_dir / "audit.json").write_text(
            json.dumps(result.audit, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        fossil_rows.extend(deep_copy(result.final_state.get("fossils", [])))
        anchor_checks = validations[route_id]["anchors"]
        archive_rows.append({
            "instrument_id": spec["instrument_id"],
            "route_id": route_id,
            "active_hash": result.active_hash,
            "causal_hash": result.causal_hash,
            "fossil_hash": result.fossil_hash,
            "fossil_count": len(result.final_state.get("fossils", [])),
            "operators": [e["operator"] for e in result.audit if e.get("event") == "transform"],
            "anchor_preservation": (
                all(x["preserved"] for x in anchor_checks) if anchor_checks else True
            ),
        })

    with (out_dir / "fossils.csv").open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "fossil_id", "route_id", "step_index", "operator", "element_id",
            "field", "before", "after", "reason",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in fossil_rows:
            writer.writerow({key: row.get(key) for key in fieldnames})

    with (out_dir / "archive" / "index.jsonl").open("w", encoding="utf-8") as handle:
        for row in archive_rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    checks = {
        "instrument_id": spec["instrument_id"],
        "routes": validations,
        "comparisons": comparisons,
        "all_declared_comparisons_passed": all(
            comp["passed"] is True for comp in comparisons if comp["passed"] is not None
        ),
        "all_deterministic_replays_passed": all(
            item["deterministic_replay"] for item in validations.values()
        ),
        "all_anchors_preserved": all(
            all(anchor["preserved"] for anchor in item["anchors"])
            for item in validations.values()
        ),
    }
    (out_dir / "checks.json").write_text(
        json.dumps(checks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (out_dir / "report.md").write_text(
        render_markdown(spec, results, comparisons, validations), encoding="utf-8"
    )

    run_record = {
        "schema_version": "0.1",
        "instrument": "Semantic Fossil Instrument",
        "instrument_version": "0.1",
        "instrument_id": spec["instrument_id"],
        "epistemic_status": spec.get("epistemic_status", "PROCEDURAL"),
        "spec_hash": digest(spec),
        "routes": archive_rows,
        "comparisons": comparisons,
        "checks": {
            "all_declared_comparisons_passed": checks["all_declared_comparisons_passed"],
            "all_deterministic_replays_passed": checks["all_deterministic_replays_passed"],
            "all_anchors_preserved": checks["all_anchors_preserved"],
        },
        "artifacts": {
            "audit": "audit.jsonl",
            "fossils": "fossils.csv",
            "archive": "archive/index.jsonl",
            "report": "report.md",
            "checks": "checks.json",
        },
    }
    (out_dir / "run.json").write_text(
        json.dumps(run_record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return checks


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_run(ns):
    spec = load_json(ns.spec)
    checks = write_run(spec, ns.out, overwrite=ns.overwrite)
    print(json.dumps(checks, indent=2, ensure_ascii=False))
    return 0 if (
        checks["all_declared_comparisons_passed"]
        and checks["all_deterministic_replays_passed"]
        and checks["all_anchors_preserved"]
    ) else 2


def cmd_validate(ns):
    checks = load_json(ns.run / "checks.json")
    print(json.dumps(checks, indent=2, ensure_ascii=False))
    ok = (
        checks.get("all_declared_comparisons_passed")
        and checks.get("all_deterministic_replays_passed")
        and checks.get("all_anchors_preserved")
    )
    return 0 if ok else 2


def parser():
    p = argparse.ArgumentParser(description="Semantic Fossil Instrument v0.1")
    sub = p.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="execute all routes in a spec")
    run.add_argument("--spec", type=Path, required=True)
    run.add_argument("--out", type=Path, required=True)
    run.add_argument("--overwrite", action="store_true", help="allow writing into a non-empty run folder")
    run.set_defaults(func=cmd_run)

    val = sub.add_parser("validate", help="validate an existing run folder")
    val.add_argument("--run", type=Path, required=True)
    val.set_defaults(func=cmd_validate)
    return p


def main(argv=None):
    ns = parser().parse_args(argv)
    try:
        return int(ns.func(ns))
    except (ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"semantic-fossil: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
