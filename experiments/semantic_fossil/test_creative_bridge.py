import json
import tempfile
import unittest
from pathlib import Path

from experiments.semantic_fossil.adapters.base import TransformRequest, TransformResult
from experiments.semantic_fossil.adapters.callback import CallbackAdapter
from experiments.semantic_fossil.adapters.packet import PacketAdapter
from experiments.semantic_fossil.artifacts import ingest_artifact, load_route_state
from experiments.semantic_fossil.compilers.suno import compile_suno
from experiments.semantic_fossil.compilers.visual import compile_visual
from experiments.semantic_fossil.instrument import Engine, write_run
from experiments.semantic_fossil.renderers import renderer_registry


HERE = Path(__file__).resolve().parent


class CreativeBridgeTests(unittest.TestCase):
    def load_spec(self):
        return json.loads((HERE / "examples" / "causal-scar.json").read_text(encoding="utf-8"))

    def test_fossil_history_changes_compiled_prompts_and_full_reset_ablates(self):
        results = Engine(self.load_spec()).run_all()
        direct = results["DIRECT"].final_state
        scarred = results["VIA_B_STATE_RESTORE"].final_state
        reset = results["VIA_B_FULL_RESET"].final_state

        direct_suno = compile_suno(direct, route_id="same")["lyrics_control"]
        scarred_suno = compile_suno(scarred, route_id="same")["lyrics_control"]
        reset_suno = compile_suno(reset, route_id="same")["lyrics_control"]
        self.assertNotEqual(direct_suno, scarred_suno)
        self.assertEqual(direct_suno, reset_suno)

        direct_visual = compile_visual(direct, route_id="same")["prompt"]
        scarred_visual = compile_visual(scarred, route_id="same")["prompt"]
        reset_visual = compile_visual(reset, route_id="same")["prompt"]
        self.assertNotEqual(direct_visual, scarred_visual)
        self.assertEqual(direct_visual, reset_visual)

    def test_prompt_limits_are_hard(self):
        state = Engine(self.load_spec()).run_all()["VIA_B_STATE_RESTORE"].final_state
        suno = compile_suno(state, route_id="x", config={"style_max": 220, "lyrics_max": 420})
        visual = compile_visual(state, route_id="x", config={"prompt_max": 500})
        self.assertLessEqual(len(suno["style"]), 220)
        self.assertLessEqual(len(suno["lyrics_control"]), 420)
        self.assertLessEqual(len(visual["prompt"]), 500)

    def test_artifact_ingestion_becomes_compiler_visible_fossil(self):
        spec = self.load_spec()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "run"
            write_run(spec, out)

            artifact = Path(td) / "render.png"
            artifact.write_bytes(b"fake-png-payload-for-test")
            result = ingest_artifact(
                out,
                "DIRECT",
                artifact,
                medium="image",
                artifact_kind="image",
                descriptors={
                    "identity_anchor_preserved": True,
                    "topological_damage": 0.72,
                    "glitch_density": 0.88,
                },
                source_operator="visual_renderer",
                reason="first rendered artifact became inherited material",
            )
            self.assertTrue(result["artifact"]["stored_path"].startswith("routes/DIRECT/artifacts/files/"))

            state = load_route_state(out, "DIRECT")
            artifact_fossils = [f for f in state["fossils"] if f.get("artifact_ref")]
            self.assertEqual(len(artifact_fossils), 1)
            self.assertEqual(
                artifact_fossils[0]["artifact_summary"]["descriptors"]["topological_damage"],
                0.72,
            )

            visual = compile_visual(state, route_id="DIRECT")["prompt"]
            suno = compile_suno(state, route_id="DIRECT")["lyrics_control"]
            self.assertIn("topological_damage", visual)
            self.assertIn("glitch_density", suno)

    def test_renderers_write_medium_packages(self):
        state = Engine(self.load_spec()).run_all()["VIA_B_STATE_RESTORE"].final_state
        registry = renderer_registry()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)
            suno = registry["suno"].compile(state, route_id="scar")
            visual = registry["visual"].compile(state, route_id="scar")
            suno_path = registry["suno"].write(suno, out / "suno")
            visual_path = registry["visual"].write(visual, out / "visual")
            self.assertTrue(suno_path.is_file())
            self.assertTrue(visual_path.is_file())
            self.assertTrue((out / "visual" / "scar.visual.json").is_file())

    def test_packet_and_callback_adapters_preserve_request_identity(self):
        request = TransformRequest(
            request_id="r1",
            route_id="route-a",
            medium="image",
            prompt="make the stored scar causally visible",
        )
        with tempfile.TemporaryDirectory() as td:
            result = PacketAdapter(Path(td)).execute(request)
            self.assertEqual(result.status, "prepared")
            self.assertTrue(Path(result.artifact_path).is_file())

        def callback(req):
            return TransformResult(
                request_id=req.request_id,
                adapter_id="fake-local-model",
                status="completed",
                artifact_path="artifact.png",
                artifact_kind="image",
            )

        result = CallbackAdapter(callback, adapter_id="fake-local-model", medium="image").execute(request)
        self.assertEqual(result.request_id, "r1")
        self.assertEqual(result.adapter_id, "fake-local-model")


if __name__ == "__main__":
    unittest.main()
