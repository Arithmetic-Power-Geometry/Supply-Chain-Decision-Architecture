"""Generate frozen holdout assignments and generalization diagnostics."""
import argparse,csv,json
from pathlib import Path
from collections import Counter
from scda.holdout import publication_split,leakage,temporal_holdout
from scda.model_competition import compete
ap=argparse.ArgumentParser();ap.add_argument("claims");ap.add_argument("--out",default="artifacts/generalization");a=ap.parse_args()
with open(a.claims,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
x=publication_split(rows);bad=leakage(x)
if bad:raise SystemExit("study leakage: "+",".join(bad))
x=temporal_holdout(x,2024)
out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
fields=list(x[0].keys()) if x else []
with (out/"holdout_assignments_v1.csv").open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(x)
report={"claims":len(x),"studies":len(set(r["study_id"] for r in x)),
"publication_partition":dict(Counter(r["partition"] for r in x)),
"temporal_partition":dict(Counter(r["temporal_partition"] for r in x)),"leakage":[],"evaluations":{}}
for field in ("partition","temporal_partition"):
 report["evaluations"][field]={}
 for part in ("development","holdout"):
  sub=[r for r in x if r[field]==part]
  report["evaluations"][field][part]={"claims":len(sub),"studies":len(set(r["study_id"] for r in sub)),
   "competition":compete(sub) if sub else None}
disc=sorted(set((r.get("discipline") or "").strip() for r in x if (r.get("discipline") or "").strip()))
report["leave_one_discipline_out"]={}
for d in disc:
 h=[r for r in x if (r.get("discipline") or "").strip()==d];dev=[r for r in x if (r.get("discipline") or "").strip()!=d]
 report["leave_one_discipline_out"][d]={"holdout_studies":len(set(r["study_id"] for r in h)),
 "holdout_claims":len(h),"holdout_competition":compete(h) if h else None,
 "development_competition":compete(dev) if dev else None}
(out/"generalization_report_v1.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
