#!/usr/bin/env python3
import argparse,csv
from pathlib import Path

def main():
 p=argparse.ArgumentParser()
 p.add_argument("batch_ids",nargs="+")
 p.add_argument("--execution-dir",default="artifacts/screening/stage2_execution")
 a=p.parse_args()
 total=0; all_ids=[]
 for bid in a.batch_ids:
  path=Path(a.execution_dir)/f"{bid}_source_verification_enriched.csv"
  if not path.exists(): raise SystemExit(f"FAIL missing initialized batch: {path}")
  with path.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
  expected=9 if bid=="B27" else 25
  if len(rows)!=expected: raise SystemExit(f"FAIL {bid} rows={len(rows)} expected={expected}")
  ids=[r["record_id"] for r in rows]
  if len(set(ids))!=expected: raise SystemExit(f"FAIL {bid} duplicate record_id")
  if any(r["batch_id"]!=bid for r in rows): raise SystemExit(f"FAIL {bid} batch_id mismatch")
  if any(r["eligibility_decision"] for r in rows): raise SystemExit(f"FAIL {bid} contains generated eligibility decision")
  if any(r["source_status"]!="pending" for r in rows): raise SystemExit(f"FAIL {bid} source status not pending")
  if any(r["adjudication_required"]!="yes" for r in rows): raise SystemExit(f"FAIL {bid} adjudication flag not yes")
  if any(not r["title"] for r in rows): raise SystemExit(f"FAIL {bid} missing title")
  total+=len(rows); all_ids.extend(ids)
 if len(set(all_ids))!=len(all_ids): raise SystemExit("FAIL record overlap across requested batches")
 print(f"PASS initialized evidence wave: {','.join(a.batch_ids)}; {total} unique records; no synthetic decisions.")

if __name__=="__main__": main()
