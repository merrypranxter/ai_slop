"""Artifact-aware fossil helpers.

Generated media stays external. The controller records only explicit files, hashes,
descriptors, and provenance. That record can then become causal input to later compilers.
"""
from __future__ import annotations

import hashlib
import json
import mimetypes
import shutil
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, Mapping, Optional


@dataclass
class ArtifactRef:
    artifact_id: str
    route_id: str
    medium: str
    artifact_kind: str
    stored_path: str
    sha256: str
    byte_size: int
    mime_type: Optional[str] = None
    descriptors: Dict[str, Any] = field(default_factory=dict)
    source_operator: str = "external_render"
    reason: Optional[str] = None

    def to_dict(self):
        return asdict(self)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def describe_file(path: Path, *, medium: str, descriptors: Mapping[str, Any] | None = None):
    path = Path(path)
    mime, _ = mimetypes.guess_type(path.name)
    return {
        "medium": medium,
        "filename": path.name,
        "suffix": path.suffix.lower(),
        "byte_size": path.stat().st_size,
        "sha256": sha256_file(path),
        "mime_type": mime,
        "descriptors": dict(descriptors or {}),
    }


def store_artifact(
    run_dir: Path,
    route_id: str,
    source_path: Path,
    *,
    medium: str,
    artifact_kind: Optional[str] = None,
    descriptors: Mapping[str, Any] | None = None,
    source_operator: str = "external_render",
    reason: Optional[str] = None,
) -> ArtifactRef:
    run_dir = Path(run_dir)
    source_path = Path(source_path)
    if not source_path.is_file():
        raise FileNotFoundError(source_path)

    route_dir = run_dir / "routes" / route_id
    if not route_dir.is_dir():
        raise ValueError(f"unknown route in run folder: {route_id}")

    description = describe_file(source_path, medium=medium, descriptors=descriptors)
    short = description["sha256"][:12]
    artifact_id = f"{route_id}-{medium}-{short}"
    artifact_dir = route_dir / "artifacts"
    file_dir = artifact_dir / "files"
    file_dir.mkdir(parents=True, exist_ok=True)

    stored_name = f"{artifact_id}{source_path.suffix.lower()}"
    stored = file_dir / stored_name
    if source_path.resolve() != stored.resolve():
        shutil.copy2(source_path, stored)

    ref = ArtifactRef(
        artifact_id=artifact_id,
        route_id=route_id,
        medium=medium,
        artifact_kind=artifact_kind or medium,
        stored_path=str(stored.relative_to(run_dir)),
        sha256=description["sha256"],
        byte_size=description["byte_size"],
        mime_type=description["mime_type"],
        descriptors=dict(descriptors or {}),
        source_operator=source_operator,
        reason=reason,
    )
    record_path = artifact_dir / f"{artifact_id}.json"
    record_path.write_text(json.dumps(ref.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return ref


def artifact_fossil(ref: ArtifactRef):
    return {
        "fossil_id": f"artifact:{ref.artifact_id}",
        "route_id": ref.route_id,
        "step_index": None,
        "operator": ref.source_operator,
        "element_id": "__artifact__",
        "field": "artifact",
        "before": None,
        "after": ref.artifact_id,
        "reason": ref.reason or "rendered artifact entered route history",
        "artifact_ref": ref.stored_path,
        "artifact_kind": ref.artifact_kind,
        "descriptor_ref": f"routes/{ref.route_id}/artifacts/{ref.artifact_id}.json",
        "artifact_summary": {
            "sha256": ref.sha256,
            "byte_size": ref.byte_size,
            "mime_type": ref.mime_type,
            "descriptors": dict(ref.descriptors),
        },
    }


def append_artifact_fossil(run_dir: Path, route_id: str, fossil: Mapping[str, Any]) -> Path:
    path = Path(run_dir) / "routes" / route_id / "artifact-fossils.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(dict(fossil), ensure_ascii=False, sort_keys=True) + "\n")
    return path


def load_artifact_fossils(run_dir: Path, route_id: str):
    path = Path(run_dir) / "routes" / route_id / "artifact-fossils.jsonl"
    if not path.is_file():
        return []
    out = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if raw:
            out.append(json.loads(raw))
    return out


def load_route_state(run_dir: Path, route_id: str, *, include_artifacts: bool = True):
    path = Path(run_dir) / "routes" / route_id / "final-state.json"
    if not path.is_file():
        raise ValueError(f"route final state not found: {route_id}")
    state = json.loads(path.read_text(encoding="utf-8"))
    if include_artifacts:
        state.setdefault("fossils", []).extend(load_artifact_fossils(run_dir, route_id))
    return state


def ingest_artifact(
    run_dir: Path,
    route_id: str,
    source_path: Path,
    *,
    medium: str,
    artifact_kind: Optional[str] = None,
    descriptors: Mapping[str, Any] | None = None,
    source_operator: str = "external_render",
    reason: Optional[str] = None,
):
    ref = store_artifact(
        run_dir,
        route_id,
        source_path,
        medium=medium,
        artifact_kind=artifact_kind,
        descriptors=descriptors,
        source_operator=source_operator,
        reason=reason,
    )
    fossil = artifact_fossil(ref)
    overlay = append_artifact_fossil(run_dir, route_id, fossil)
    return {"artifact": ref.to_dict(), "fossil": fossil, "overlay": str(overlay)}
