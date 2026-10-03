#!/usr/bin/env python3
import argparse,csv
from pathlib import Path

KEY="record_id"
OVERLAY_FIELDS=["source_status","source_type","source_identifier","source_location","bibliographic_verified","full_text_status","eligibility_decision","exclusion_reason","study_type","reviewer","confidence","adjudication_required","evidence_note"]

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--base",default="artifacts/screening/stage2_execution/B01_source_verification_enriched.csv")
 p.add_argument("--parts",nargs="+",default=["data/screening/stage2_b01_verified_decisions_part01_v1.csv","data/screening/stage2_b01_verified_decisions_part02_v1.csv","data/screening/stage2_b01_verified_decisions_part03_v1.csv"])
 p.add_argument("--output",default="artifacts/screening/stage2_execution/B01_source_verification_final.csv")
 a=p.parse_args()
 with open(a.base,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f)); fields=list(rows[0])
 by={x[KEY]:x for x in rows}
 if len(rows)!=25 or len(by)!=25: raise SystemExit("FAIL base B01 must have 25 unique records")
 seen=set()
 for path in a.parts:
  with open(path,newline="",encoding="utf-8") as f:
   for x in csv.DictReader(f):
    rid=x[KEY]
    if rid in seen: raise SystemExit(f"FAIL duplicate decision across parts: {rid}")
    if rid not in by: raise SystemExit(f"FAIL decision not in B01: {rid}")
    seen.add(rid)
    for k in OVERLAY_FIELDS: by[rid][k]=x.get(k,"")
 if len(seen)!=25: raise SystemExit(f"FAIL expected 25 decisions, found {len(seen)}")
 Path(a.output).parent.mkdir(parents=True,exist_ok=True)
 with open(a.output,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 print("B01 merged: 25/25 source-supported Reviewer-A decisions.")
if __name__=="__main__": main()
