"""Run nested SCDA pilot stress test on provisional primary studies."""
from __future__ import annotations
import csv,json
from pathlib import Path
from scda.evaluation import signatures,collision_rate_from_signatures,coverage,entropy,ablation

IN=Path("data/primary_pilot_v1.csv")
OUT=Path("artifacts/pilot"); OUT.mkdir(parents=True,exist_ok=True)
with IN.open(encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))

models={
"K4":["level","process","flow","objective"],
"KS7":["level","process","flow","objective","theory","method","technology"],
"KSV8":["level","process","flow","objective","theory","method","technology","evidence"],
"SCDA9":["level","process","flow","objective","theory","method","technology","evidence","industry"],
}
results=[]
for name,dims in models.items():
    sig=signatures(rows,dims)
    results.append({
      "model":name,"dimensions":len(dims),"records":len(rows),
      "coverage":coverage(rows,dims),
      "collision_rate":collision_rate_from_signatures(sig),
      "distinct_signatures":len(set(sig)),
      "signature_entropy":entropy(["|".join(x) for x in sig]),
    })
with (OUT/"nested_results.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=results[0]);w.writeheader();w.writerows(results)

abl=ablation(rows,models["SCDA9"])
with (OUT/"scda9_ablation.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=abl[0]);w.writeheader();w.writerows(abl)

summary={"status":"pilot_only_not_publication_evidence","models":results,
         "interpretation_rule":"Do not use pilot metrics as headline manuscript results."}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
