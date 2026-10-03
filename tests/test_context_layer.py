import unittest
from scda.context_layer import evaluate
class TestContextLayer(unittest.TestCase):
 def test_context_variation(self):
  base={"decision_level":"strategic","process":"source","flow":"material","objective":"resilience","theory":"","method":"case","technology":"","evidence_maturity":"case study"}
  rows=[dict(base,study_id="S1",context="automotive"),dict(base,study_id="S2",context="healthcare")]
  x=evaluate(rows);self.assertEqual(x["groups_with_context_variation"],1);self.assertEqual(x["cross_study_groups_with_context_variation"],1)
 def test_single_claim_not_matched(self):
  self.assertEqual(evaluate([{"study_id":"S1","context":"retail"}])["matched_groups"],0)
if __name__=="__main__":unittest.main()
