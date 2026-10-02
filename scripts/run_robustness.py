"""Run frozen SCDA robustness battery."""
import argparse,csv,json
from pathlib import Path
from scda.robustness import battery
ap=argparse.ArgumentParser();ap.add_argument("claims");ap.add_argument("--bootstrap",type=int,default=500);ap.add_argument("--out",default="artifacts/robustness/robustness_v1.json");a=ap.parse_args()
with open(a.claims,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
res=battery(rows,a.bootstrap);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(res,indent=2)+"\n")
print(json.dumps({"scenario_selection_counts":res["scenario_selection_counts"],"study_bootstrap":res["study_bootstrap"]},indent=2))
