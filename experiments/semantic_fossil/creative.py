#!/usr/bin/env python3
"""Creative bridge for Semantic Fossil runs.

Compile fossil-aware Suno/visual instructions, make provider-neutral request packets,
and ingest generated artifacts back into explicit route history.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .adapters.base import TransformRequest
    from .adapters.packet import PacketAdapter
    from .artifacts import ingest_artifact, load_route_state
    from .instrument import digest, active_payload, causal_payload, normalized_fossils
    from .renderers import renderer_registry
except ImportError:  # direct script execution from the repository checkout
    import sys
    ROOT = Path(__file__).resolve().parents[2]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from experiments.semantic_fossil.adapters.base import TransformRequest
    from experiments.semantic_fossil.adapters.packet import PacketAdapter
    from experiments.semantic_fossil.artifacts import ingest_artifact, load_route_state
    from experiments.semantic_fossil.instrument import digest, active_payload, causal_payload, normalized_fossils
    from experiments.semantic_fossil.renderers import renderer_registry


def route_ids(run_dir: Path):
    root = Path(run_dir) / "routes"
    if not root.is_dir():
        raise ValueError(f"not a Semantic Fossil run folder: {run_dir}")
    return sorted(p.name for p in root.iterdir() if p.is_dir() and (p / "final-state.json").is_file())


def parse_descriptors(items):
    out = {}
    for item in items or []:
        if "=" not in item:
            raise ValueError(f"descriptor must be key=value: {item}")
        key, value = item.split("=", 1)
        value = value.strip()
        lowered = value.lower()
        if lowered in {"true", "false"}:
            parsed = lowered == "true"
        else:
            try:
                parsed = int(value)
            except ValueError:
                try:
                    parsed = float(value)
                except ValueError:
                    parsed = value
        out[key.strip()] = parsed
    return out


def cmd_compile(ns):
    registry = renderer_registry()
    names = list(registry) if ns.renderer == "all" else [ns.renderer]
    out = ns.out or (ns.run / "compiled")
    out.mkdir(parents=True, exist_ok=True)
    routes = [ns.route] if ns.route else route_ids(ns.run)
    written = []

    for route_id in routes:
        state = load_route_state(ns.run, route_id, include_artifacts=not ns.ignore_artifacts)
        for name in names:
            renderer = registry[name]
            rendered = renderer.compile(state, route_id=route_id, config={})
            target = renderer.write(rendered, out / name)
            written.append({"route": route_id, "renderer": name, "path": str(target)})

    print(json.dumps({"written": written}, indent=2))
    return 0


def cmd_packet(ns):
    registry = renderer_registry()
    renderer = registry[ns.renderer]
    state = load_route_state(ns.run, ns.route, include_artifacts=not ns.ignore_artifacts)
    rendered = renderer.compile(state, route_id=ns.route, config={})
    request = TransformRequest(
        request_id=ns.request_id or f"{ns.route}-{ns.renderer}",
        route_id=ns.route,
        medium=renderer.medium,
        prompt=rendered.prompt,
        active_hash=digest(active_payload(state)),
        causal_hash=digest(causal_payload(state)),
        fossil_hash=digest(normalized_fossils(state.get("fossils", []))),
        metadata={"renderer": renderer.renderer_id, "payload": rendered.payload},
    )
    adapter = PacketAdapter(ns.out)
    result = adapter.execute(request)
    print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
    return 0


def cmd_ingest(ns):
    result = ingest_artifact(
        ns.run,
        ns.route,
        ns.file,
        medium=ns.medium,
        artifact_kind=ns.kind,
        descriptors=parse_descriptors(ns.descriptor),
        source_operator=ns.operator,
        reason=ns.reason,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


def parser():
    p = argparse.ArgumentParser(description="Semantic Fossil creative bridge v0.2")
    sub = p.add_subparsers(dest="command", required=True)

    compile_p = sub.add_parser("compile", help="compile route state to medium-facing instructions")
    compile_p.add_argument("--run", type=Path, required=True)
    compile_p.add_argument("--route")
    compile_p.add_argument("--renderer", choices=["suno", "visual", "all"], default="all")
    compile_p.add_argument("--out", type=Path)
    compile_p.add_argument("--ignore-artifacts", action="store_true")
    compile_p.set_defaults(func=cmd_compile)

    packet = sub.add_parser("packet", help="write a provider-neutral transform request packet")
    packet.add_argument("--run", type=Path, required=True)
    packet.add_argument("--route", required=True)
    packet.add_argument("--renderer", choices=["suno", "visual"], required=True)
    packet.add_argument("--request-id")
    packet.add_argument("--out", type=Path, required=True)
    packet.add_argument("--ignore-artifacts", action="store_true")
    packet.set_defaults(func=cmd_packet)

    ingest = sub.add_parser("ingest", help="ingest a rendered artifact as explicit route history")
    ingest.add_argument("--run", type=Path, required=True)
    ingest.add_argument("--route", required=True)
    ingest.add_argument("--medium", required=True)
    ingest.add_argument("--kind")
    ingest.add_argument("--file", type=Path, required=True)
    ingest.add_argument("--descriptor", action="append", default=[])
    ingest.add_argument("--operator", default="external_render")
    ingest.add_argument("--reason")
    ingest.set_defaults(func=cmd_ingest)
    return p


def main(argv=None):
    ns = parser().parse_args(argv)
    try:
        return int(ns.func(ns))
    except (ValueError, KeyError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"semantic-fossil-creative: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
