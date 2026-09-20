#!/usr/bin/env python3
"""Silent Scar v0.1: matched second-injury assay for Lenia.

A scar claim is about history changing what happens next.

Route A (control):    seed -> ordinary evolution -> standardized second injury -> response
Route B (wounded):    seed -> transient sensory wound -> visible recovery -> same class of
                      standardized second injury -> response

If B matters, the two post-injury response families may diverge even after both routes have
returned to the same ordinary morphology neighborhood. This script records that divergence;
it does not declare "memory" from one run.

Thin harness around a local checkout of jessescool/lenia-umwelt.
Epistemic status: PROCEDURAL / HYPOTHESIS.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

from run_lenia_occlusion import (
    centroid,
    circle_mask,
    components,
    heading,
    load_source,
    profile,
    torus_delta,
)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--umwelt", type=Path, required=True)
    p.add_argument("--animal", default="O2u")
    p.add_argument("--grid", type=int, default=128)
    p.add_argument("--burn-in", type=int, default=120)
    p.add_argument("--heading-probe", type=int, default=40)
    p.add_argument("--neighborhood-steps", type=int, default=160)
    p.add_argument("--neighborhood-sample-every", type=int, default=2)
    p.add_argument("--active-threshold", type=float, default=0.05)

    p.add_argument("--first-wound-steps", type=int, default=80)
    p.add_argument("--first-mask-radius", type=float, default=10.0)
    p.add_argument("--first-mask-ahead", type=float, default=22.0)
    p.add_argument("--max-recovery-steps", type=int, default=500)
    p.add_argument("--recovery-window", type=int, default=8)

    p.add_argument("--second-mask-radius", type=float, default=8.0)
    p.add_argument("--second-mask-ahead", type=float, default=10.0)
    p.add_argument("--second-response-steps", type=int, default=260)
    p.add_argument("--sample-every", type=int, default=2)

    p.add_argument("--out", type=Path, default=Path("results/silent-scar"))
    return p.parse_args()


def natural_neighborhood(seed, steps, every, threshold):
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
    distances = (stack - bary).abs().sum(dim=1)
    return bary, m, float(distances.max().item())


def profile_distance(state, bary, m):
    return float((profile(state, m) - bary).abs().sum().item())


def relative_mask(sim, radius, ahead, heading_probe):
    hy, hx = heading(sim, heading_probe)
    cy, cx = centroid(sim.board.tensor)
    h, w = sim.board.shape
    center = ((cy + hy * ahead) % h, (cx + hx * ahead) % w)
    mask = circle_mask(
        sim.board.shape,
        center,
        radius,
        sim.board.tensor.device,
        sim.board.tensor.dtype,
    )
    return mask, center, (hy, hx)


def run_first_wound(seed, mask, cfg, bary, m, dmax):
    """Transient normalized sensory wound followed by ordinary recovery."""
    sim = seed.clone()
    max_distance = profile_distance(sim.board.tensor, bary, m)
    wound_distances = []

    for _ in range(cfg.first_wound_steps):
        sim.lenia.step(blind_mask=mask)
        d = profile_distance(sim.board.tensor, bary, m)
        wound_distances.append(d)
        max_distance = max(max_distance, d)

    consecutive = 0
    recovery_wait = None
    recovery_trace = []

    for t in range(1, cfg.max_recovery_steps + 1):
        sim.lenia.step()
        d = profile_distance(sim.board.tensor, bary, m)
        recovery_trace.append(d)
        max_distance = max(max_distance, d)
        if d <= dmax:
            consecutive += 1
            if consecutive >= cfg.recovery_window:
                recovery_wait = t
                break
        else:
            consecutive = 0

    elapsed = cfg.first_wound_steps + (recovery_wait or cfg.max_recovery_steps)
    return {
        "sim": sim,
        "elapsed": elapsed,
        "recovery_wait": recovery_wait,
        "max_profile_distance": max_distance,
        "wound_max_profile_distance": max(wound_distances) if wound_distances else None,
        "final_profile_distance": profile_distance(sim.board.tensor, bary, m),
        "returned_to_neighborhood": recovery_wait is not None,
        "recovery_trace": recovery_trace,
    }


def advance_control(seed, steps):
    sim = seed.clone()
    sim.run(steps)
    return sim


def snapshot_metrics(sim, mask, bary, m, threshold):
    s = sim.board.tensor
    mass = float(s.sum().item())
    active = s > threshold
    active_n = max(int(active.sum().item()), 1)
    return {
        "profile_distance": profile_distance(s, bary, m),
        "mass": mass,
        "connected_components": components(s, threshold),
        "weighted_mask_overlap": float((s * mask).sum().item() / max(mass, 1e-12)),
        "active_mask_overlap": float((active.to(s.dtype) * mask).sum().item() / active_n),
        "centroid_yx": list(centroid(s)),
    }


def inflict_second_injury(sim, mask):
    """One-shot physical erasure. No persistent mask remains afterward."""
    sim.board.tensor.mul_(1 - mask)


def record_second_response(label, sim, mask, cfg, bary, m, dmax):
    rows = []
    start_y, start_x = centroid(sim.board.tensor)
    recent = []

    for t in range(cfg.second_response_steps + 1):
        if t % cfg.sample_every == 0:
            s = sim.board.tensor
            cy, cx = centroid(s)
            recent.append((cy, cx))
            recent = recent[-6:]
            local_heading = None
            if len(recent) >= 2:
                dy = torus_delta(recent[0][0], recent[-1][0], sim.board.shape[0])
                dx = torus_delta(recent[0][1], recent[-1][1], sim.board.shape[1])
                if abs(dx) + abs(dy) > 1e-9:
                    local_heading = math.atan2(dy, dx)

            dy0 = torus_delta(start_y, cy, sim.board.shape[0])
            dx0 = torus_delta(start_x, cx, sim.board.shape[1])
            mass = float(s.sum().item())
            active = s > cfg.active_threshold
            active_n = max(int(active.sum().item()), 1)
            d = profile_distance(s, bary, m)

            rows.append({
                "route": label,
                "step_after_second_injury": t,
                "profile_distance": d,
                "in_natural_neighborhood": d <= dmax,
                "mass": mass,
                "connected_components": components(s, cfg.active_threshold),
                "centroid_y": cy,
                "centroid_x": cx,
                "centroid_displacement": math.hypot(dy0, dx0),
                "local_heading_rad": local_heading,
                "weighted_second_mask_overlap": float(
                    (s * mask).sum().item() / max(mass, 1e-12)
                ),
                "active_second_mask_overlap": float(
                    (active.to(s.dtype) * mask).sum().item() / active_n
                ),
            })

        if t < cfg.second_response_steps:
            sim.lenia.step()

    return rows


def recovery_step(rows, window):
    consecutive = 0
    for row in rows:
        if row["in_natural_neighborhood"]:
            consecutive += 1
            if consecutive >= window:
                return row["step_after_second_injury"]
        else:
            consecutive = 0
    return None


def route_summary(rows, window):
    return {
        "second_recovery_step": recovery_step(rows, window),
        "max_profile_distance": max(r["profile_distance"] for r in rows),
        "final_profile_distance": rows[-1]["profile_distance"],
        "minimum_mass": min(r["mass"] for r in rows),
        "final_mass": rows[-1]["mass"],
        "max_connected_components": max(r["connected_components"] for r in rows),
        "max_centroid_displacement": max(r["centroid_displacement"] for r in rows),
        "final_centroid_displacement": rows[-1]["centroid_displacement"],
    }


def num_delta(a, b):
    if a is None or b is None:
        return None
    return a - b


def main():
    cfg = parse_args()
    repo, substrate = load_source(cfg.umwelt)
    animals = substrate.load_animals(repo / "animals.json", codes=[cfg.animal])
    if not animals:
        raise SystemExit(f"Unknown animal code: {cfg.animal}")

    creature = animals[0]
    sim_cfg = substrate.Config.from_animal(creature, base_grid=cfg.grid, scale=1)
    seed_sim = substrate.Simulation(sim_cfg)
    seed_sim.place_animal(creature, center=True)
    seed_sim.run(cfg.burn_in)
    seed = seed_sim.clone()

    bary, m, dmax = natural_neighborhood(
        seed,
        cfg.neighborhood_steps,
        cfg.neighborhood_sample_every,
        cfg.active_threshold,
    )

    first_mask, first_center, first_heading = relative_mask(
        seed,
        cfg.first_mask_radius,
        cfg.first_mask_ahead,
        cfg.heading_probe,
    )

    first = run_first_wound(seed, first_mask, cfg, bary, m, dmax)
    scarred = first["sim"]
    control = advance_control(seed, first["elapsed"])

    # Both routes receive the same *class* and dose of injury in their own body-relative
    # coordinates. This avoids pretending their absolute world coordinates stayed aligned.
    scar_mask, scar_center, scar_heading = relative_mask(
        scarred,
        cfg.second_mask_radius,
        cfg.second_mask_ahead,
        cfg.heading_probe,
    )
    control_mask, control_center, control_heading = relative_mask(
        control,
        cfg.second_mask_radius,
        cfg.second_mask_ahead,
        cfg.heading_probe,
    )

    pre_scar = snapshot_metrics(
        scarred, scar_mask, bary, m, cfg.active_threshold
    )
    pre_control = snapshot_metrics(
        control, control_mask, bary, m, cfg.active_threshold
    )

    cfg.out.mkdir(parents=True, exist_ok=True)

    import numpy as np
    np.save(cfg.out / "first_wound_mask.npy", first_mask.detach().cpu().numpy())
    np.save(cfg.out / "pre_second_scarred.npy", scarred.board.tensor.detach().cpu().numpy())
    np.save(cfg.out / "pre_second_control.npy", control.board.tensor.detach().cpu().numpy())
    np.save(cfg.out / "second_mask_scarred.npy", scar_mask.detach().cpu().numpy())
    np.save(cfg.out / "second_mask_control.npy", control_mask.detach().cpu().numpy())

    inflict_second_injury(scarred, scar_mask)
    inflict_second_injury(control, control_mask)

    scar_rows = record_second_response(
        "first_wound_then_second_injury",
        scarred,
        scar_mask,
        cfg,
        bary,
        m,
        dmax,
    )
    control_rows = record_second_response(
        "no_first_wound_then_second_injury",
        control,
        control_mask,
        cfg,
        bary,
        m,
        dmax,
    )

    rows = scar_rows + control_rows
    with (cfg.out / "second_response_timeseries.csv").open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    np.save(cfg.out / "final_scarred.npy", scarred.board.tensor.detach().cpu().numpy())
    np.save(cfg.out / "final_control.npy", control.board.tensor.detach().cpu().numpy())

    scar_summary = route_summary(scar_rows, cfg.recovery_window)
    control_summary = route_summary(control_rows, cfg.recovery_window)
    deltas = {
        key: num_delta(scar_summary[key], control_summary[key])
        for key in scar_summary
        if isinstance(scar_summary[key], (int, float)) or scar_summary[key] is None
    }

    valid_visible_match = (
        first["returned_to_neighborhood"]
        and pre_scar["profile_distance"] <= dmax
        and pre_control["profile_distance"] <= dmax
    )

    summary = {
        "experiment": "silent_scar_second_injury_v0.1",
        "epistemic_status": "PROCEDURAL",
        "substrate": "jessescool/lenia-umwelt",
        "animal": cfg.animal,
        "scar_law": "A->C may differ from A->B->C when B leaves a causal scar.",
        "natural_neighborhood_dmax": dmax,
        "first_wound": {
            "type": "transient normalized sensory occlusion",
            "steps": cfg.first_wound_steps,
            "mask_radius": cfg.first_mask_radius,
            "mask_center_yx": first_center,
            "heading_yx": first_heading,
            "recovery_wait_steps": first["recovery_wait"],
            "returned_to_neighborhood": first["returned_to_neighborhood"],
            "max_profile_distance": first["max_profile_distance"],
            "final_profile_distance": first["final_profile_distance"],
            "total_elapsed_before_second_injury": first["elapsed"],
        },
        "pre_second_injury": {
            "scarred_route": pre_scar,
            "matched_control_route": pre_control,
            "both_visibly_in_natural_neighborhood": valid_visible_match,
        },
        "second_injury": {
            "type": "one-shot body-relative physical state erasure",
            "mask_radius": cfg.second_mask_radius,
            "scarred_center_yx": scar_center,
            "control_center_yx": control_center,
            "scarred_heading_yx": scar_heading,
            "control_heading_yx": control_heading,
        },
        "second_response": {
            "scarred_route": scar_summary,
            "matched_control_route": control_summary,
            "scarred_minus_control": deltas,
        },
        "interpretation_contract": (
            "A single divergent run is not a memory claim. Candidate scar evidence requires "
            "matched visible recovery, repeated runs/doses, and a reproducible difference in "
            "response to the standardized second perturbation."
        ),
    }

    (cfg.out / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(json.dumps({
        "valid_visible_match": valid_visible_match,
        "first_wound_recovery_wait": first["recovery_wait"],
        "scarred_second_recovery": scar_summary["second_recovery_step"],
        "control_second_recovery": control_summary["second_recovery_step"],
        "output": str(cfg.out / "summary.json"),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
