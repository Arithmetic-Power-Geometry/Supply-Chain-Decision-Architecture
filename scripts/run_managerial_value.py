"""Generate managerial decision-usefulness artifact."""
import argparse,csv,json
from pathlib import Path
from scda.managerial_value import evaluate
ap=argparse.ArgumentParser();ap.add_argument("claims");ap.add_argument("--out",default="artifacts/managerial/decision_usefulness_v1.json");a=ap.parse_args()
with open(a.claims,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
res=evaluate(rows);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(res,indent=2)+"\n")
summary={k:{"claims":v["claims"],"ambiguous_claims":v["ambiguous_claims"],"ambiguity_rate":v["ambiguity_rate"]} for k,v in res.items() if isinstance(v,dict) and "ambiguity_rate" in v}
print(json.dumps(summary,indent=2))
