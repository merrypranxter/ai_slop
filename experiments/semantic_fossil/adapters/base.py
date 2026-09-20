"""Provider-neutral transform adapter contract.

Adapters are intentionally outside the core controller. They may call a local model,
remote service, command-line tool, or human-mediated workflow, but they must return an
explicit artifact record. Controller state stays software-owned and inspectable.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, Mapping, Optional


@dataclass
class TransformRequest:
    request_id: str
    route_id: str
    medium: str
    prompt: str
    active_hash: Optional[str] = None
    causal_hash: Optional[str] = None
    fossil_hash: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TransformResult:
    request_id: str
    adapter_id: str
    status: str
    artifact_path: Optional[str] = None
    artifact_kind: Optional[str] = None
    mime_type: Optional[str] = None
    provider_record: Dict[str, Any] = field(default_factory=dict)
    descriptors: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class TransformAdapter(ABC):
    """Minimal contract for plugging a generator into the fossil controller."""

    adapter_id = "abstract"
    medium = "mixed"

    @abstractmethod
    def execute(self, request: TransformRequest) -> TransformResult:
        """Execute or externalize one transform request."""
        raise NotImplementedError

    def parse_result(self, result: TransformResult) -> Mapping[str, Any]:
        """Hook for provider-specific result normalization."""
        return result.to_dict()
