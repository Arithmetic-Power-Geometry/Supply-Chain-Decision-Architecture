#!/usr/bin/env python3
import argparse,csv,json
from pathlib import Path

TERMINAL={"include","exclude","uncertain"}
EXCLUSIONS={f"E{i:02d}" for i in range(1,11)}
SOURCE_STATUS={"pending","located","verified","unavailable"}
FULLTEXT={"pending","abstract_only","metadata_only","full_text","unavailable"}

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--input",default="artifacts/screening/stage2_execution/B01_source_verification_enriched.csv")
 p.add_argument("--audit",default="artifacts/screening/stage2_execution/B01_evidence_audit.json")
 a=p.parse_args()
 with open(a.input,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
 errors=[]
 if len(rows)!=25 or len({r["record_id"] for r in rows})!=25: errors.append("B01 must contain 25 unique records")
 for i,r in enumerate(rows,1):
  rid=r["record_id"]
  if r["source_status"] not in SOURCE_STATUS: errors.append(f"{rid}: invalid source_status")
  if r["full_text_status"] not in FULLTEXT: errors.append(f"{rid}: invalid full_text_status")
  d=r["eligibility_decision"].strip()
  if d and d not in TERMINAL: errors.append(f"{rid}: invalid eligibility_decision")
  if r["bibliographic_verified"] not in {"yes","no"}: errors.append(f"{rid}: bibliographic_verified must be yes/no")
  if d:
   if r["source_status"] not in {"verified","unavailable"}: errors.append(f"{rid}: decision without verified/unavailable source state")
   if not r["evidence_note"].strip(): errors.append(f"{rid}: terminal decision requires evidence_note")
   if d=="exclude" and r["exclusion_reason"] not in EXCLUSIONS: errors.append(f"{rid}: exclusion requires E01-E10")
   if d=="include" and r["study_type"] not in {"primary","review"}: errors.append(f"{rid}: include requires primary/review routing")
  if not d and r["exclusion_reason"].strip(): errors.append(f"{rid}: exclusion code without decision")
 summary={"records":len(rows),"unique_record_ids":len({r["record_id"] for r in rows}),"source_verified":sum(r["source_status"]=="verified" for r in rows),"bibliographic_verified":sum(r["bibliographic_verified"]=="yes" for r in rows),"terminal_decisions":sum(bool(r["eligibility_decision"].strip()) for r in rows),"errors":errors}
 Path(a.audit).parent.mkdir(parents=True,exist_ok=True)
 Path(a.audit).write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2))
 if errors: raise SystemExit("FAIL Batch-01 evidence audit")
if __name__=="__main__": main()
