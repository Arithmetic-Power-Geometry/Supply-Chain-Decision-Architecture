#!/usr/bin/env python3
import argparse,csv,json
from collections import Counter
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("ledger",nargs="?",default="artifacts/screening/stage2_screening_ledger.csv")
    p.add_argument("--output",default="artifacts/screening/stage2_status_audit.json")
    a=p.parse_args()
    with open(a.ledger,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    ids=[r["record_id"] for r in rows]
    if len(rows)!=659 or len(set(ids))!=659:
        raise SystemExit("FAIL Stage-2 ledger must contain 659 unique record IDs")
    status=Counter(r.get("full_text_status","") for r in rows)
    decision=Counter(r.get("stage2_decision","") or "pending" for r in rows)
    missing_reason=[r["record_id"] for r in rows if r.get("stage2_decision")=="exclude" and not r.get("exclusion_reason")]
    report={"records":len(rows),"unique_record_ids":len(set(ids)),"full_text_status":dict(status),"eligibility_decision":dict(decision),"excluded_without_reason":len(missing_reason),"freeze_ready":decision.get("pending",0)==0 and not missing_reason}
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    with open(a.output,"w",encoding="utf-8") as f: json.dump(report,f,indent=2)
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
