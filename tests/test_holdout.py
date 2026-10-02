import unittest
from scda.holdout import publication_split,leakage,temporal_holdout
class TestHoldout(unittest.TestCase):
 def test_no_claim_leakage(self):
  rows=[{"study_id":"S1"},{"study_id":"S1"},{"study_id":"S2"}]
  x=publication_split(rows);self.assertEqual(leakage(x),[])
  self.assertEqual(x[0]["partition"],x[1]["partition"])
 def test_deterministic(self):
  r=[{"study_id":"S1"},{"study_id":"S2"}]
  self.assertEqual([x["partition"] for x in publication_split(r)],[x["partition"] for x in publication_split(r)])
 def test_temporal(self):
  x=temporal_holdout([{"study_id":"A","year":"2023"},{"study_id":"B","year":"2024"}])
  self.assertEqual([z["temporal_partition"] for z in x],["development","holdout"])
if __name__=="__main__":unittest.main()
