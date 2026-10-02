import csv
from pathlib import Path
from scda.evaluation import signatures, collision_rate_from_signatures

def test_nested_models_do_not_lose_records():
    p=Path("data/primary_pilot_v1.csv")
    with p.open(encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
    for dims in [["level","process","flow","objective"],
                 ["level","process","flow","objective","theory","method","technology","evidence","industry"]]:
        assert len(signatures(rows,dims))==len(rows)

def test_pilot_has_no_duplicate_ids():
    with Path("data/primary_pilot_v1.csv").open(encoding="utf-8-sig",newline="") as f:
        ids=[r["pilot_id"] for r in csv.DictReader(f)]
    assert len(ids)==len(set(ids))
