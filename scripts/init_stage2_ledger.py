#!/usr/bin/env python3
import argparse,csv
from pathlib import Path

FIELDS=["record_id","stage2_decision","exclusion_reason","full_text_status","full_text_source","full_text_identifier","study_type","reviewer","confidence","adjudication_required","notes"]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--stage1",default="artifacts/screening/stage2_queue.csv")
    p.add_argument("--output",default="artifacts/screening/stage2_screening_ledger.csv")
    a=p.parse_args()
    with open(a.stage1,newline="",encoding="utf-8") as f: src=list(csv.DictReader(f))
    if len(src)!=659: raise SystemExit(f"FAIL Stage-2 entry rows={len(src)} expected=659")
    ids=[r["record_id"] for r in src]
    if len(set(ids))!=659: raise SystemExit("FAIL duplicate Stage-2 entry record_id")
    out=[]
    for r in src:
        out.append({"record_id":r["record_id"],"stage2_decision":"","exclusion_reason":"","full_text_status":"pending","full_text_source":"","full_text_identifier":"","study_type":r.get("study_type",""),"reviewer":"Reviewer A (AI-assisted)","confidence":"","adjudication_required":"yes","notes":""})
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(out)
    print(f"Stage-2 ledger initialized: {len(out)} records; all pending full-text eligibility.")

if __name__=="__main__": main()
