"""Run frozen evidence-layer matched-case analysis."""
import argparse,csv,json
from pathlib import Path
from scda.evidence_layer import evaluate
ap=argparse.ArgumentParser();ap.add_argument("claims");ap.add_argument("--out",default="artifacts/evidence_layer/matched_case_v1.json");a=ap.parse_args()
with open(a.claims,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
res=evaluate(rows);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(res,indent=2)+"\n")
print(json.dumps({k:v for k,v in res.items() if not k.endswith("_groups")},indent=2))
