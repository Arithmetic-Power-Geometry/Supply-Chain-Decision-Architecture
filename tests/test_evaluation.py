from scda.evaluation import entropy, normalized_entropy, collision_rate_from_signatures, coverage, ablation

def test_entropy_constant_zero():
    assert entropy(["a","a","a"]) == 0.0

def test_normalized_entropy_balanced_binary():
    assert normalized_entropy(["a","a","b","b"]) == 1.0

def test_collision_counts_records_in_shared_signatures():
    assert collision_rate_from_signatures([("a",),("a",),("b",)]) == 2/3

def test_coverage():
    rows=[{"a":"x","b":"y"},{"a":"z","b":""}]
    assert coverage(rows,["a","b"]) == 0.75

def test_ablation_exposes_useful_dimension():
    rows=[{"a":"x","b":"1"},{"a":"x","b":"2"}]
    result={x["removed"]:x for x in ablation(rows,["a","b"])}
    assert result["b"]["collision_increase"] == 1.0
    assert result["a"]["collision_increase"] == 0.0
