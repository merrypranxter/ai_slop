"""Compile Semantic Fossil state into a visual-generation instruction package."""
from __future__ import annotations

from typing import Any, Mapping

from .common import active_elements, anchor_lines, clamp, fossil_lines, fossil_pressure


def compile_visual(state: Mapping[str, Any], *, route_id: str = "route", config: Mapping[str, Any] | None = None):
    config = dict(config or {})
    prompt_max = int(config.get("prompt_max", 6000))
    anchors = anchor_lines(state)
    pressure = fossil_pressure(state)
    elements = active_elements(state)

    lines = [
        "Generate a visual artifact from explicit external route state.",
        "The current frame is not a clean restart: route history may constrain material, geometry, continuity, damage, and interpretation.",
        "Do not merely decorate the image with labels for prior events; make their consequences govern visible structure.",
    ]
    if anchors:
        lines.append("PRESERVE AS RECOGNIZABLE INVARIANTS: " + "; ".join(anchors) + ".")
    if state.get("interpretation"):
        lines.append("CURRENT INTERPRETATION: " + str(state.get("interpretation")) + ".")
    if elements:
        lines.append("ACTIVE STATE:")
        for e in elements:
            lines.append(f"- {e['id']}: value={e['value']!r}; meaning={e['meaning']!r}; anchor={e['anchor']}")
    if state.get("traits"):
        lines.append("STRUCTURAL TRAITS: " + repr(state.get("traits")))
    if state.get("fossils"):
        lines.append("ROUTE FOSSILS — THESE ARE CAUSAL CONSTRAINTS ON THE NEXT IMAGE:")
        for fossil in fossil_lines(state):
            lines.append("- " + fossil)
        lines.append(
            "Translate each relevant fossil into a physical or compositional consequence: deformation, repair tissue, topology, material memory, asymmetry, repeated artifact, capture damage, or changed ownership of structure."
        )
    if pressure["artifact_media_seen"]:
        lines.append(
            "Some fossils point to prior rendered artifacts. Reuse their recorded descriptors as inherited structure; do not claim access to anything beyond those stored descriptors."
        )
    lines.append("Keep the explicit anchor stable while route-sensitive dimensions are allowed to mutate.")
    prompt = clamp("\n".join(lines), prompt_max)
    return {
        "renderer": "visual",
        "route_id": route_id,
        "prompt": prompt,
        "limits": {"prompt_max": prompt_max},
        "history_summary": pressure,
    }
