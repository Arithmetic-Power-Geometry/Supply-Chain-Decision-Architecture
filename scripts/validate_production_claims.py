#!/usr/bin/env python3
import argparse,csv
ALLOWED={
"decision_level":{"strategic","tactical","operational","real-time/autonomous"},
"process":{"plan","source","make","store","move","deliver","return","recover","enable"},
"flow":{"material","information","financial","knowledge","risk","carbon"},
"objective":{"cost","service","quality","speed","flexibility","resilience","sustainability","trust"},
"method":{"conceptual","empirical","optimization","simulation","statistics","machine learning","artificial intelligence","multi-agent/autonomous"},
"evidence_maturity":{"conceptual","synthetic","simulation","benchmark","case study","observational","pilot","deployed","longitudinal"}
}
REQ=["claim_id","study_id","record_id","claim_text","claim_location","source_support","source_identifier","coder","confidence"]
p=argparse.ArgumentParser();p.add_argument("claims");a=p.parse_args()
with open(a.claims,encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
seen=set();errors=[]
for n,r in enumerate(rows,2):
 for k in REQ:
  if not (r.get(k) or "").strip(): errors.append(f"row {n}: missing {k}")
 cid=(r.get("claim_id") or "").strip()
 if cid in seen: errors.append(f"row {n}: duplicate claim_id {cid}")
 seen.add(cid)
 for k,vals in ALLOWED.items():
  v=(r.get(k) or "").strip().lower()
  if v and v not in vals and v!="ambiguous": errors.append(f"row {n}: invalid {k}={r.get(k)}")
 if not (r.get("context") or "").strip(): errors.append(f"row {n}: missing context")
if errors:
 print("\n".join(errors));raise SystemExit(f"FAIL {len(errors)} production claim-coding errors")
print(f"PASS {len(rows)} production claims satisfy frozen-category/provenance gate")
