import unittest
from scda.evidence_layer import evaluate
class TestEvidenceLayer(unittest.TestCase):
 def test_matched_variation(self):
  base={"decision_level":"tactical","process":"plan","flow":"information","objective":"cost","theory":"","method":"simulation","technology":"digital twin"}
  rows=[dict(base,study_id="S1",evidence_maturity="simulation"),dict(base,study_id="S2",evidence_maturity="deployed")]
  x=evaluate(rows);self.assertEqual(x["matched_groups"],1);self.assertEqual(x["groups_with_evidence_variation"],1)
 def test_unmatched_not_counted(self):
  rows=[{"study_id":"S1","decision_level":"strategic","evidence_maturity":"conceptual"}]
  self.assertEqual(evaluate(rows)["matched_groups"],0)
if __name__=="__main__":unittest.main()
