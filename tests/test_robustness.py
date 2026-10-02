import unittest
from scda.robustness import battery,study_bootstrap
class TestRobustness(unittest.TestCase):
 def setUp(self):
  self.rows=[{"study_id":"S1","decision_level":"tactical","process":"plan","flow":"information","objective":"cost","theory":"","method":"simulation","technology":"","evidence_maturity":"simulation","context":"general"},
             {"study_id":"S2","decision_level":"strategic","process":"recover","flow":"risk","objective":"resilience","theory":"","method":"case","technology":"","evidence_maturity":"case study","context":"automotive"}]
 def test_grid(self): self.assertEqual(len(battery(self.rows,10)["scenarios"]),60)
 def test_bootstrap(self): self.assertEqual(study_bootstrap(self.rows,10)["replicates"],10)
if __name__=="__main__":unittest.main()
