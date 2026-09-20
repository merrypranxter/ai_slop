#!/usr/bin/env python3
"""Perceptual Wound v0.1: four-condition Lenia sensory-occlusion assay.

Thin harness around a local checkout of jessescool/lenia-umwelt.
The source project is not vendored or modified here.

Conditions:
  no_mask
  state_erasure
  unnormalized_occlusion
  normalized_occlusion

The point is to separate physical damage from information-only damage and to
record behavior plus morphology instead of judging a single pretty frame.

Epistemic status: PROCEDURAL / HYPOTHESIS until matched runs are completed.
"""
from __future__ import annotations

import argparse
import csv
import importlib
import json
import math
import sys
from pathlib import Path


def args():
    p = argparse.ArgumentParser()
    p.add_argument("--umwelt", type=Path, required=True)
    p.add_argument("--animal", default="O2u")
    p.add_argument("--grid", type=int, default=128)
    p.add_argument("--burn-in", type=int, default=120)
    p.add_argument("--heading-probe", type=int, default=40)
    p.add_argument("--neighborhood-steps", type=int, default=120)
    p.add_argument("--steps", type=int, default=360)
    p.add_argument("--sample-every", type=int, default=2)
    p.add_argument("--mask-radius", type=float, default=10.0)
    p.add_argument("--mask-ahead", type=float, default=22.0)
    p.add_argument("--active-threshold", type=float, default=0.05)
    p.add_argument("--recovery-window", type=int, default=5)
    p.add_argument("--out", type=Path, default=Path("results/perceptual-wound"))
    return p.parse_args()


def load_source(repo: Path):
    repo = repo.expanduser().resolve()
    if not (repo / "substrate").exists() or not (repo / "animals.json").exists():
        raise SystemExit(f"{repo} is not a lenia-umwelt checkout")
    sys.path.insert(0, str(repo))
    return repo, importlib.import_module("substrate")


def centroid(state):
    import torch
    mass = float(state.sum().item())
    if mass <= 1e-12:
        return float("nan"), float("nan")
    h, w = state.shape
    yy = torch.arange(h, device=state.device, dtype=state.dtype)[:, None]
    xx = torch.arange(w, device=state.device, dtype=state.dtype)[None, :]
    return (
        float((state * yy).sum().item() / mass),
        float((state * xx).sum().item() / mass),
    )


def torus_delta(a, b, size):
    d = b - a
    if d > size / 2:
        d -= size
    elif d < -size / 2:
        d += size
    return d


def heading(sim, n):
    start = centroid(sim.board.tensor)
    probe = sim.clone()
    probe.run(n)
    end = centroid(probe.board.tensor)
    h, w = sim.board.shape
    dy = torus_delta(start[0], end[0], h)
    dx = torus_delta(start[1], end[1], w)
    norm = math.hypot(dy, dx)
    return (0.0, 1.0) if norm < 1e-8 else (dy / norm, dx / norm)


def circle_mask(shape, center, radius, device, dtype):
    import torch
    h, w = shape
    cy, cx = center
    yy = torch.arange(h, device=device, dtype=dtype)[:, None]
    xx = torch.arange(w, device=device, dtype=dtype)[None, :]
    dy = torch.minimum((yy - cy).abs(), h - (yy - cy).abs())
    dx = torch.minimum((xx - cx).abs(), w - (xx - cx).abs())
    return ((dx * dx + dy * dy) <= radius * radius).to(dtype)


def profile(state, m):
    import torch
    flat = state.flatten()
    return torch.topk(flat, k=min(m, flat.numel()), largest=True, sorted=True).values


def neighborhood(seed, steps, every, threshold):
    import torch
    sim = seed.clone()
    m = max(64, int((sim.board.tensor > threshold).sum().item()))
    ps = []
    for t in range(steps):
        sim.lenia.step()
        if t % every == 0:
            ps.append(profile(sim.board.tensor, m))
    stack = torch.stack(ps)
    bary = stack.median(dim=0).values
    d = (stack - bary).abs().sum(dim=1)
    return bary, m, float(d.max().item())


def components(state, threshold):
    from scipy import ndimage
    active = (state.detach().cpu().numpy() > threshold)
    return int(ndimage.label(active)[1])


def step_no_mask(sim, mask):
    sim.lenia.step()


def step_state_erasure(sim, mask):
    sim.board.tensor.mul_(1 - mask)
    sim.lenia.step()


def step_unnormalized(sim, mask):
    current = sim.board.tensor
    physical = current.clone()
    current.mul_(1 - mask)
    _, _, update = sim.automaton.decompose(sim.board)
    current.copy_(physical)
    current.copy_((current + update).clamp(0.0, 1.0))
    sim.lenia.tick += 1


def step_normalized(sim, mask):
    sim.lenia.step(blind_mask=mask)


def run_condition(name, seed, mask, step_fn, cfg, bary, m, dmax):
    sim = seed.clone()
    rows = []
    recent = []
    for t in range(cfg.steps + 1):
        if t % cfg.sample_every == 0:
            s = sim.board.tensor
            y, x = centroid(s)
            recent.append((y, x))
            recent = recent[-6:]
            hrad = None
            if len(recent) >= 2:
                dy = torus_delta(recent[0][0], recent[-1][0], sim.board.shape[0])
                dx = torus_delta(recent[0][1], recent[-1][1], sim.board.shape[1])
                if abs(dx) + abs(dy) > 1e-9:
                    hrad = math.atan2(dy, dx)
            mass = float(s.sum().item())
            pdist = float((profile(s, m) - bary).abs().sum().item())
            active = s > cfg.active_threshold
            active_n = max(int(active.sum().item()), 1)
            rows.append({
                "condition": name,
                "step": t,
                "centroid_y": y,
                "centroid_x": x,
                "mass": mass,
                "heading_rad": hrad,
                "connected_components": components(s, cfg.active_threshold),
                "weighted_mask_overlap": float((s * mask).sum().item() / max(mass, 1e-12)),
                "active_mask_overlap": float((active.to(s.dtype) * mask).sum().item() / active_n),
                "profile_distance": pdist,
                "in_natural_neighborhood": pdist <= dmax,
            })
        if t < cfg.steps:
            step_fn(sim, mask)
    return rows, sim


def recovery_step(rows, window):
    exited = False
    trail = []
    for r in rows:
        ok = bool(r["in_natural_neighborhood"])
        exited = exited or not ok
        trail.append(ok)
        if exited and len(trail) >= window and all(trail[-window:]):
            return r["step"]
    return None


def main():
    cfg = args()
    repo, substrate = load_source(cfg.umwelt)
    creatures = substrate.load_animals(repo / "animals.json", codes=[cfg.animal])
    if not creatures:
        raise SystemExit(f"Unknown animal code: {cfg.animal}")
    creature = creatures[0]
    sim_cfg = substrate.Config.from_animal(creature, base_grid=cfg.grid, scale=1)
    sim = substrate.Simulation(sim_cfg)
    sim.place_animal(creature, center=True)
    sim.run(cfg.burn_in)
    seed = sim.clone()

    hy, hx = heading(seed, cfg.heading_probe)
    cy, cx = centroid(seed.board.tensor)
    h, w = seed.board.shape
    mask_center = ((cy + hy * cfg.mask_ahead) % h, (cx + hx * cfg.mask_ahead) % w)
    mask = circle_mask(seed.board.shape, mask_center, cfg.mask_radius,
                       seed.board.tensor.device, seed.board.tensor.dtype)

    bary, m, dmax = neighborhood(
        seed, cfg.neighborhood_steps, cfg.sample_every, cfg.active_threshold
    )

    modes = {
        "no_mask": step_no_mask,
        "state_erasure": step_state_erasure,
        "unnormalized_occlusion": step_unnormalized,
        "normalized_occlusion": step_normalized,
    }
    all_rows = []
    finals = {}
    by_condition = {}
    for name, fn in modes.items():
        print(f"running {name}")
        rows, final_sim = run_condition(name, seed, mask, fn, cfg, bary, m, dmax)
        all_rows.extend(rows)
        by_condition[name] = rows
        finals[name] = final_sim

    cfg.out.mkdir(parents=True, exist_ok=True)
    with (cfg.out / "timeseries.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        writer.writeheader()
        writer.writerows(all_rows)

    import numpy as np
    np.save(cfg.out / "blind_mask.npy", mask.detach().cpu().numpy())
    for name, final_sim in finals.items():
        np.save(cfg.out / f"final_{name}.npy", final_sim.board.tensor.detach().cpu().numpy())

    baseline_heading = by_condition["no_mask"][-1]["heading_rad"]
    summary = {
        "experiment": "perceptual_wound_lenia_occlusion_v0.1",
        "epistemic_status": "PROCEDURAL",
        "substrate": "jessescool/lenia-umwelt",
        "animal": cfg.animal,
        "mask_center_yx": mask_center,
        "mask_radius": cfg.mask_radius,
        "estimated_heading_yx": [hy, hx],
        "natural_neighborhood_dmax": dmax,
        "conditions": {},
    }
    for name, rows in by_condition.items():
        last = rows[-1]
        hd = None
        if last["heading_rad"] is not None and baseline_heading is not None:
            hd = (last["heading_rad"] - baseline_heading + math.pi) % (2 * math.pi) - math.pi
        summary["conditions"][name] = {
            "final_mass": last["mass"],
            "max_profile_distance": max(r["profile_distance"] for r in rows),
            "final_profile_distance": last["profile_distance"],
            "first_recovery_step_after_excursion": recovery_step(rows, cfg.recovery_window),
            "max_weighted_mask_overlap": max(r["weighted_mask_overlap"] for r in rows),
            "max_connected_components": max(r["connected_components"] for r in rows),
            "final_heading_rad": last["heading_rad"],
            "final_heading_delta_vs_no_mask_rad": hd,
            "final_centroid_yx": [last["centroid_y"], last["centroid_x"]],
        }

    (cfg.out / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"wrote {cfg.out / 'summary.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
