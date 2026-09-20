"""Adapter that writes a provider-neutral request packet for external execution."""
from __future__ import annotations

import json
from pathlib import Path

from .base import TransformAdapter, TransformRequest, TransformResult


class PacketAdapter(TransformAdapter):
    adapter_id = "packet"
    medium = "mixed"

    def __init__(self, out_dir: Path):
        self.out_dir = Path(out_dir)

    def execute(self, request: TransformRequest) -> TransformResult:
        self.out_dir.mkdir(parents=True, exist_ok=True)
        path = self.out_dir / f"{request.request_id}.request.json"
        path.write_text(json.dumps(request.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return TransformResult(
            request_id=request.request_id,
            adapter_id=self.adapter_id,
            status="prepared",
            artifact_path=str(path),
            artifact_kind="request_packet",
            mime_type="application/json",
            provider_record={"execution": "external", "packet": str(path)},
        )
