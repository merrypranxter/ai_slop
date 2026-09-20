"""Shared fossil-to-prompt compilation helpers."""
from __future__ import annotations

import json
from typing import Any, Mapping


def clamp(text: str, limit: int) -> str:
    if limit <= 0:
        return ""
    if len(text) <= limit:
        return text
    if limit <= 3:
        return text[:limit]
    return text[: limit - 3].rstrip() + "..."


def active_elements(state: Mapping[str, Any]):
    out = []
    for element_id, element in state.get("elements", {}).items():
        if not element.get("active", True):
            continue
        out.append({
            "id": element_id,
            "value": element.get("value"),
            "meaning": element.get("meaning"),
            "anchor": bool(element.get("anchor", False)),
        })
    return out


def anchor_lines(state: Mapping[str, Any]):
    return [
        f"{e['id']}={e['value']}"
        for e in active_elements(state)
        if e["anchor"]
    ]


def fossil_lines(state: Mapping[str, Any], limit: int = 16):
    fossils = list(state.get("fossils", []))[-limit:]
    lines = []
    for fossil in fossils:
        base = (
            f"{fossil.get('operator')} changed {fossil.get('element_id')}.{fossil.get('field')} "
            f"from {fossil.get('before')!r} to {fossil.get('after')!r}"
        )
        artifact = fossil.get("artifact_summary")
        if artifact:
            desc = artifact.get("descriptors", artifact)
            base += "; artifact=" + json.dumps(desc, sort_keys=True, ensure_ascii=False)
        lines.append(base)
    return lines


def fossil_pressure(state: Mapping[str, Any]):
    """Summarize history into explicit, non-mystical downstream obligations."""
    fossils = list(state.get("fossils", []))
    operators = []
    artifact_media = []
    for fossil in fossils:
        op = fossil.get("operator")
        if op and op not in operators:
            operators.append(op)
        if fossil.get("artifact_kind") and fossil.get("artifact_kind") not in artifact_media:
            artifact_media.append(fossil.get("artifact_kind"))
    return {
        "fossil_count": len(fossils),
        "operators_seen": operators,
        "artifact_media_seen": artifact_media,
        "history_present": bool(fossils),
    }
