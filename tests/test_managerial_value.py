import unittest
from scda.managerial_value import evaluate
class TestManagerialValue(unittest.TestCase):
 def test_same_tech_different_decision(self):
  rows=[{"study_id":"A","technology":"ai","decision_level":"strategic","process":"source","flow":"material","objective":"resilience"},
        {"study_id":"B","technology":"ai","decision_level":"operational","process":"deliver","flow":"material","objective":"cost"}]
  self.assertEqual(evaluate(rows)["technology_hides_decision"]["ambiguity_rate"],1.0)
if __name__=="__main__":unittest.main()
