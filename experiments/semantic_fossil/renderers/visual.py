from __future__ import annotations

import json
from pathlib import Path

from .base import RenderedPrompt, RendererPlugin
from ..compilers.visual import compile_visual


class VisualRenderer(RendererPlugin):
    renderer_id = "visual"
    medium = "image"

    def compile(self, state, *, route_id, config=None):
        payload = compile_visual(state, route_id=route_id, config=config)
        return RenderedPrompt(self.renderer_id, self.medium, route_id, payload["prompt"], payload)

    def write(self, rendered, out_dir: Path):
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        txt = out_dir / f"{rendered.route_id}.visual.txt"
        txt.write_text(rendered.prompt + "\n", encoding="utf-8")
        meta = out_dir / f"{rendered.route_id}.visual.json"
        meta.write_text(json.dumps(rendered.payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return txt
