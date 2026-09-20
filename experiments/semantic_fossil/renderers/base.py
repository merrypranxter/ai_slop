"""Renderer plugin contract for turning fossil state into medium-facing instructions."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, Mapping


@dataclass
class RenderedPrompt:
    renderer_id: str
    medium: str
    route_id: str
    prompt: str
    payload: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self):
        return asdict(self)


class RendererPlugin(ABC):
    renderer_id = "abstract"
    medium = "mixed"

    @abstractmethod
    def compile(self, state: Mapping[str, Any], *, route_id: str, config: Mapping[str, Any] | None = None) -> RenderedPrompt:
        raise NotImplementedError

    @abstractmethod
    def write(self, rendered: RenderedPrompt, out_dir: Path) -> Path:
        raise NotImplementedError


def renderer_registry():
    from .suno import SunoRenderer
    from .visual import VisualRenderer
    return {
        "suno": SunoRenderer(),
        "visual": VisualRenderer(),
    }
