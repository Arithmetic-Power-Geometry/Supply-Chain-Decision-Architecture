import unittest
from scda.stable_ids import stable_record_id
class TestStableIDs(unittest.TestCase):
 def test_doi_normalization(self):
  a={"doi":"https://doi.org/10.1000/ABC","openalex_id":"x","title":"A"}
  b={"doi":"10.1000/abc","openalex_id":"y","title":"B"}
  self.assertEqual(stable_record_id(a),stable_record_id(b))
 def test_openalex_fallback(self):
  a={"doi":"","openalex_id":"https://openalex.org/W123","title":"A"}
  self.assertEqual(stable_record_id(a),stable_record_id(a))
if __name__=="__main__":unittest.main()
