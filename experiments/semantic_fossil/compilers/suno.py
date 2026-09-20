"""Compile Semantic Fossil state into a Suno-facing prompt package."""
from __future__ import annotations

from typing import Any, Mapping

from .common import active_elements, anchor_lines, clamp, fossil_lines, fossil_pressure


def compile_suno(state: Mapping[str, Any], *, route_id: str = "route", config: Mapping[str, Any] | None = None):
    config = dict(config or {})
    style_max = int(config.get("style_max", 1000))
    lyrics_max = int(config.get("lyrics_max", 5000))

    anchors = anchor_lines(state)
    pressure = fossil_pressure(state)
    elements = active_elements(state)
    interpretation = state.get("interpretation")

    style_parts = [
        "Compose from explicit controller state, not from generic weirdness.",
        "Keep musical jurisdictions distinct: rhythm, harmony, melody, timbre, performance, and anchor may carry different obligations.",
    ]
    if anchors:
        style_parts.append("Preserve route anchors as recognizable musical invariants: " + "; ".join(anchors) + ".")
    if interpretation:
        style_parts.append(f"Current interpretation: {interpretation}.")
    if pressure["history_present"]:
        style_parts.append(
            "Route history is material. Let earlier transformations leave audible consequences instead of resetting to a pristine endpoint."
        )
        style_parts.append("Operators already in ancestry: " + ", ".join(pressure["operators_seen"]) + ".")
    if pressure["artifact_media_seen"]:
        style_parts.append("Prior artifact media in the fossil record: " + ", ".join(pressure["artifact_media_seen"]) + ".")
    style = clamp(" ".join(style_parts), style_max)

    controls = [
        "[SEMANTIC FOSSIL CONTROLLER]",
        f"[ROUTE {route_id}]",
        "[Treat the following as explicit external route state. Do not claim hidden model memory.]",
    ]
    if anchors:
        controls.append("[ANCHORS: " + "; ".join(anchors) + "]")
    if interpretation:
        controls.append(f"[CURRENT INTERPRETATION: {interpretation}]")
    controls.append("[ACTIVE ELEMENTS]")
    for e in elements:
        controls.append(f"[{e['id']}: value={e['value']!r}; meaning={e['meaning']!r}; anchor={e['anchor']}]")
    if state.get("traits"):
        controls.append("[TRAITS: " + repr(state.get("traits")) + "]")
    if state.get("fossils"):
        controls.append("[FOSSIL CONSEQUENCES: later structure should respond to these route events when musically relevant]")
        for line in fossil_lines(state):
            controls.append("[" + line + "]")
    controls.extend([
        "[Do not flatten all route effects into one style adjective. Assign consequences to concrete musical layers.]",
        "[Preserve anchors while allowing scarred dimensions to carry forward their history.]",
        "[If a fossil contains an artifact descriptor, translate the descriptor into arrangement, phonetics, timing, texture, or form rather than merely naming it.]",
    ])
    lyrics_control = clamp("\n".join(controls), lyrics_max)

    return {
        "renderer": "suno",
        "route_id": route_id,
        "style": style,
        "lyrics_control": lyrics_control,
        "limits": {"style_max": style_max, "lyrics_max": lyrics_max},
        "history_summary": pressure,
    }
