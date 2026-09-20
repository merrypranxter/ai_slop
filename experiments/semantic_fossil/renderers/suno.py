from __future__ import annotations

import json
from pathlib import Path

from .base import RenderedPrompt, RendererPlugin
from ..compilers.suno import compile_suno


class SunoRenderer(RendererPlugin):
    renderer_id = "suno"
    medium = "audio"

    def compile(self, state, *, route_id, config=None):
        payload = compile_suno(state, route_id=route_id, config=config)
        prompt = payload["style"] + "\n\n" + payload["lyrics_control"]
        return RenderedPrompt(self.renderer_id, self.medium, route_id, prompt, payload)

    def write(self, rendered, out_dir: Path):
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"{rendered.route_id}.suno.json"
        path.write_text(json.dumps(rendered.payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return path
