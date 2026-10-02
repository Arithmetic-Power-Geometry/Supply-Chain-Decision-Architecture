#!/usr/bin/env python3
import argparse,csv,hashlib
from pathlib import Path

FIELDS=["record_id","sample_rank","stratum","coder_b_status","coder_b_decision","notes"]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("stage2",nargs="?",default="artifacts/screening/stage2_screening_ledger.csv")
    p.add_argument("--fraction",type=float,default=.20)
    p.add_argument("--output",default="artifacts/reliability/stage2_coder_b_sample.csv")
    a=p.parse_args()
    with open(a.stage2,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    if len(rows)!=659 or len({r["record_id"] for r in rows})!=659: raise SystemExit("FAIL expected 659 unique Stage-2 records")
    # Sampling membership is deterministic and blinded to Reviewer-A decisions.
    ranked=sorted(rows,key=lambda r:hashlib.sha256(("SCDA-G4|"+r["record_id"]).encode()).hexdigest())
    n=max(1,int(len(rows)*a.fraction+0.999999))
    chosen=ranked[:n]
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
        for i,r in enumerate(chosen,1):w.writerow({"record_id":r["record_id"],"sample_rank":i,"stratum":"stage2_entry","coder_b_status":"pending","coder_b_decision":"","notes":""})
    print(f"Prepared independent-coder sample shell: {len(chosen)}/{len(rows)} records. No coder-B decisions generated.")

if __name__=="__main__": main()
