import importlib.util
import json
import tempfile
import unittest
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "instrument.py"
SPEC = importlib.util.spec_from_file_location("semantic_fossil_instrument", MODULE_PATH)
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)


class SemanticFossilTests(unittest.TestCase):
    def load(self, name):
        return json.loads((HERE / "examples" / name).read_text(encoding="utf-8"))

    def test_choir_reproduces_expected_forms_and_reset(self):
        spec = self.load("choir.json")
        engine = mod.Engine(spec)
        results = engine.run_all()

        expected_ab = {
            "pressure": "fava",
            "knot": "favi",
            "breath": "ava",
            "turn": "fota",
            "echo": "tava",
            "return": "mora",
            "scar": "kavi",
            "thread": "sava",
        }
        expected_ba = {
            "pressure": "fafa",
            "knot": "fafi",
            "breath": "afa",
            "turn": "fota",
            "echo": "tava",
            "return": "mora",
            "scar": "kafi",
            "thread": "safa",
        }
        got_ab = {k: v["value"] for k, v in results["AB"].final_state["elements"].items()}
        got_ba = {k: v["value"] for k, v in results["BA"].final_state["elements"].items()}
        self.assertEqual(got_ab, expected_ab)
        self.assertEqual(got_ba, expected_ba)
        self.assertNotEqual(results["AB"].active_hash, results["BA"].active_hash)
        self.assertEqual(results["A_RESET_B"].active_hash, results["B_ONLY"].active_hash)
        self.assertEqual(results["A_RESET_B"].causal_hash, results["B_ONLY"].causal_hash)

    def test_state_restore_preserves_fossil_and_full_reset_ablates_it(self):
        spec = self.load("causal-scar.json")
        engine = mod.Engine(spec)
        results = engine.run_all()
        comparisons = {x["id"]: x for x in mod.compare_routes(spec, results)}

        self.assertTrue(comparisons["same-visible-state-before-C"]["passed"])
        self.assertTrue(comparisons["history-changes-C"]["passed"])
        self.assertTrue(comparisons["full-reset-ablates-scar-before-C"]["passed"])
        self.assertTrue(comparisons["full-reset-ablates-downstream-effect"]["passed"])

        direct = results["DIRECT"]
        via = results["VIA_B_STATE_RESTORE"]
        full = results["VIA_B_FULL_RESET"]
        self.assertNotEqual(direct.active_hash, via.active_hash)
        self.assertEqual(direct.active_hash, full.active_hash)

        restore_event = next(e for e in via.audit if e.get("event") == "restore")
        self.assertTrue(restore_event["restored_active_exactly"])
        self.assertFalse(restore_event["restored_causal_exactly"])

        full_restore = next(e for e in full.audit if e.get("event") == "restore")
        self.assertTrue(full_restore["restored_active_exactly"])
        self.assertTrue(full_restore["restored_causal_exactly"])

    def test_run_writes_minimum_record_and_archive(self):
        spec = self.load("causal-scar.json")
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "run"
            checks = mod.write_run(spec, out)
            self.assertTrue(checks["all_declared_comparisons_passed"])
            self.assertTrue(checks["all_deterministic_replays_passed"])
            self.assertTrue(checks["all_anchors_preserved"])
            for rel in [
                "run.json",
                "checks.json",
                "report.md",
                "audit.jsonl",
                "fossils.csv",
                "archive/index.jsonl",
                "routes/DIRECT/final-state.json",
                "routes/VIA_B_STATE_RESTORE/projection.txt",
            ]:
                self.assertTrue((out / rel).is_file(), rel)

            run_record = json.loads((out / "run.json").read_text(encoding="utf-8"))
            self.assertEqual(run_record["instrument_version"], "0.1")
            self.assertEqual(run_record["instrument_id"], "semantic-scar-causal-demo-v0.1")


if __name__ == "__main__":
    unittest.main()
