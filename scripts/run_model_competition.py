"""Run frozen nested-model competition on a claim CSV."""
import argparse,csv,json
from pathlib import Path
from scda.model_competition import compete,leave_one_out,study_cluster_summary
ap=argparse.ArgumentParser();ap.add_argument("claims");ap.add_argument("--out",default="artifacts/model_competition")
a=ap.parse_args()
with open(a.claims,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
grid=[]
for tol in (0,.01,.02,.05):
 for lam in (0,.01,.02,.03,.05):
  x=compete(rows,lam,tol);grid.append({"collision_tolerance":tol,"lambda":lam,
   "selected":x["selection"]["smallest_adequate_model"],"models":x["models"]})
(out/"nested_primary_v1.json").write_text(json.dumps(compete(rows,.02,.02),indent=2)+"\n")
(out/"nested_sensitivity_v1.json").write_text(json.dumps(grid,indent=2)+"\n")
(out/"scda9_ablation_v1.json").write_text(json.dumps(leave_one_out(rows),indent=2)+"\n")
(out/"study_cluster_v1.json").write_text(json.dumps(study_cluster_summary(rows),indent=2)+"\n")
print(json.dumps(compete(rows,.02,.02),indent=2))
