import unittest

from scda import DecisionRecord, DecisionArchitecture, collision_rate, distinguishability


class TestSCDA(unittest.TestCase):
    def setUp(self):
        self.records = [
            DecisionRecord("A", "strategic", "plan", "material", "cost", "systems", "optimization", "none", "benchmark", "manufacturing"),
            DecisionRecord("B", "strategic", "plan", "risk", "resilience", "systems", "simulation", "digital twin", "simulation", "manufacturing"),
            DecisionRecord("C", "operational", "deliver", "material", "speed", "operations", "optimization", "IoT", "case study", "retail"),
        ]
        self.arch = DecisionArchitecture(self.records)

    def test_validation_accepts_valid_records(self):
        self.assertEqual(len(self.arch.records), 3)

    def test_full_architecture_separates_records(self):
        self.assertEqual(distinguishability(self.arch, self.arch.dimensions), 1.0)

    def test_function_only_has_collision(self):
        self.assertGreater(collision_rate(self.arch, ["process"]), 0.0)

    def test_signature_is_deterministic(self):
        first = self.arch.signature(self.records[0])
        second = self.arch.signature(self.records[0])
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
