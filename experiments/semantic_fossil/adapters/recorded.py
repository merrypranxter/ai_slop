"""Adapter for bringing an already-generated artifact back into the instrument."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping, Optional

from .base import TransformAdapter, TransformRequest, TransformResult
from ..artifacts import describe_file


class RecordedResponseAdapter(TransformAdapter):
    adapter_id = "recorded-response"
    medium = "mixed"

    def __init__(self, response_path: Path, *, artifact_kind: Optional[str] = None, descriptors: Optional[Mapping[str, Any]] = None):
        self.response_path = Path(response_path)
        self.artifact_kind = artifact_kind
        self.descriptors = dict(descriptors or {})

    def execute(self, request: TransformRequest) -> TransformResult:
        if not self.response_path.is_file():
            raise FileNotFoundError(self.response_path)
        description = describe_file(self.response_path, medium=request.medium, descriptors=self.descriptors)
        return TransformResult(
            request_id=request.request_id,
            adapter_id=self.adapter_id,
            status="recorded",
            artifact_path=str(self.response_path),
            artifact_kind=self.artifact_kind or request.medium,
            mime_type=description.get("mime_type"),
            provider_record={"source": "recorded_external_response"},
            descriptors=description,
        )
