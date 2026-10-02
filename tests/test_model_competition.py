import unittest
from scda.model_competition import compete,leave_one_out,study_cluster_summary
class TestCompetition(unittest.TestCase):
 def setUp(self):
  self.rows=[
   {"study_id":"S1","decision_level":"tactical","process":"plan","flow":"information","objective":"cost","theory":"","method":"analytical","technology":"","evidence_maturity":"synthetic","context":"general"},
   {"study_id":"S1","decision_level":"tactical","process":"plan","flow":"information","objective":"cost","theory":"","method":"simulation","technology":"","evidence_maturity":"simulation","context":"general"},
   {"study_id":"S2","decision_level":"strategic","process":"recover","flow":"risk","objective":"resilience","theory":"","method":"case","technology":"","evidence_maturity":"case study","context":"automotive"}]
 def test_smallest_adequate(self):
  x=compete(self.rows);self.assertIn(x["selection"]["smallest_adequate_model"],{"K4","KS7","KSV8","SCDA9"})
 def test_ablation(self): self.assertEqual(len(leave_one_out(self.rows)),9)
 def test_cluster(self): self.assertEqual(study_cluster_summary(self.rows)["multi_claim_studies"],1)
if __name__=="__main__":unittest.main()
