#!/usr/bin/env python3
import argparse,csv
from pathlib import Path

FIELDS=["record_id","batch_id","source_status","source_type","source_identifier","source_location","bibliographic_verified","full_text_status","eligibility_decision","exclusion_reason","study_type","reviewer","confidence","adjudication_required","evidence_note"]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--batch",default="artifacts/screening/stage2_acquisition_batches/B01.csv")
    p.add_argument("--output",default="artifacts/screening/stage2_execution/B01_source_verification.csv")
    a=p.parse_args()
    with open(a.batch,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    if len(rows)!=25 or len({r["record_id"] for r in rows})!=25:
        raise SystemExit("FAIL Batch 01 must contain 25 unique records")
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
        for r in rows:
            w.writerow({"record_id":r["record_id"],"batch_id":"B01","source_status":"pending","source_type":"","source_identifier":"","source_location":"","bibliographic_verified":"no","full_text_status":"pending","eligibility_decision":"","exclusion_reason":"","study_type":"","reviewer":"Reviewer A (AI-assisted)","confidence":"","adjudication_required":"yes","evidence_note":""})
    print("Initialized Stage-2 Batch 01 source-verification package: 25 unique records; no eligibility decisions generated.")

if __name__=="__main__": main()
