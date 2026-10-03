#!/usr/bin/env python3
"""Block empirical architecture analysis until the production evidence gate is complete."""
import csv,json,hashlib,sys
from pathlib import Path
CLAIMS=Path("data/production_claims_final_v1.csv")
ADJ=Path("data/production_pre_reliability_adjudication_v1.csv")
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
with CLAIMS.open(encoding="utf-8-sig",newline="") as f: claims=list(csv.DictReader(f))
with ADJ.open(encoding="utf-8-sig",newline="") as f: adj=list(csv.DictReader(f))
pending=[r for r in adj if (r.get("status") or "").startswith("pending")]
studies={r["study_id"] for r in claims if r.get("study_id")}
report={"claims":len(claims),"contributing_studies":len(studies),"claims_sha256":sha(CLAIMS),
"pending_pre_reliability_adjudications":len(pending),
"coder_b_completed":False,
"architecture_analysis_unlocked":False,
"status":"BLOCKED",
"reasons":[]}
if pending: report["reasons"].append("Pre-reliability adjudications remain unresolved.")
report["reasons"].append("Independent Coder-B coding and pre-adjudication reliability are not yet available.")
report["reasons"].append("Production source acquisition/extraction is not declared complete.")
p=Path("artifacts/final/empirical_gate_status_v1.json");p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
sys.exit(2)
