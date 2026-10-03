#!/usr/bin/env python3
import argparse,csv
from pathlib import Path

FIELDS=["source_status","source_type","source_identifier","source_location","bibliographic_verified","full_text_status","eligibility_decision","exclusion_reason","study_type","reviewer","confidence","adjudication_required","evidence_note"]

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--base",required=True)
 p.add_argument("--decisions",required=True)
 p.add_argument("--output",required=True)
 a=p.parse_args()
 with open(a.base,newline="",encoding="utf-8") as f:
  rows=list(csv.DictReader(f)); names=list(rows[0])
 by={r["record_id"]:r for r in rows}
 with open(a.decisions,newline="",encoding="utf-8") as f:
  decisions=list(csv.DictReader(f))
 if len(decisions)!=len(rows): raise SystemExit("FAIL incomplete decision ledger")
 if len({r["record_id"] for r in decisions})!=len(decisions): raise SystemExit("FAIL duplicate decision ID")
 for d in decisions:
  rid=d["record_id"]
  if rid not in by: raise SystemExit("FAIL foreign decision ID")
  for k in FIELDS: by[rid][k]=d.get(k,"")
 Path(a.output).parent.mkdir(parents=True,exist_ok=True)
 with open(a.output,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=names);w.writeheader();w.writerows(rows)
 print("Finalized source-supported Stage-2 batch.")
if __name__=="__main__": main()
