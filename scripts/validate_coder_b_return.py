#!/usr/bin/env python3
"""Validate a returned independent Coder-B file against its blinded frozen template."""
import argparse,csv,hashlib,json,sys
from pathlib import Path
IMM=["claim_id","study_id","record_id","claim_text","claim_location","source_support","source_identifier"]
REQ=["decision_level","process","flow","objective","method","evidence_maturity","context","confidence"]
ALLOWED={
"decision_level":{"Strategic","Tactical","Operational","Real-time/autonomous"},
"process":{"Plan","Source","Make","Store","Move","Deliver","Return","Recover","Enable"},
"flow":{"Material","Information","Financial","Knowledge","Risk","Carbon"},
"objective":{"Cost","Service","Quality","Speed","Flexibility","Resilience","Sustainability","Trust"},
"method":{"Conceptual","Empirical","Optimization","Simulation","Statistics","Machine Learning","Artificial Intelligence","Multi-agent/Autonomous"},
"evidence_maturity":{"Conceptual","Synthetic","Simulation","Benchmark","Case study","Observational","Pilot","Deployed","Longitudinal"},
"confidence":{"certain","probable","ambiguous"}}
def load(p):
 with open(p,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
ap=argparse.ArgumentParser();ap.add_argument("template");ap.add_argument("returned");ap.add_argument("--out",default="artifacts/reliability/coder_b_return_validation_v1.json");a=ap.parse_args()
T=load(a.template);R=load(a.returned);err=[]
if len(T)!=len(R):err.append(f"row count changed: template={len(T)} returned={len(R)}")
tm={r["claim_id"]:r for r in T};rm={r["claim_id"]:r for r in R}
if set(tm)!=set(rm):err.append("claim-id membership changed")
for cid in sorted(set(tm)&set(rm)):
 for k in IMM:
  if (tm[cid].get(k) or "")!=(rm[cid].get(k) or ""):err.append(f"{cid}: immutable field changed: {k}")
 for k in REQ:
  v=(rm[cid].get(k) or "").strip()
  if not v:err.append(f"{cid}: missing {k}")
  if k in ALLOWED and v and v not in ALLOWED[k]:err.append(f"{cid}: invalid {k}={v}")
res={"status":"PASS" if not err else "FAIL","template_claims":len(T),"returned_claims":len(R),"errors":err,
"returned_sha256":hashlib.sha256(Path(a.returned).read_bytes()).hexdigest()}
p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(res,indent=2)+"\n");print(json.dumps(res,indent=2))
if err:sys.exit(1)
