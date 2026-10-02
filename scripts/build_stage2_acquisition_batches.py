#!/usr/bin/env python3
import argparse,csv,hashlib
from pathlib import Path

FIELDS=["record_id","batch_id","full_text_status","source_type","source_location","source_identifier","access_checked","verification_status","notes"]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("ledger",nargs="?",default="artifacts/screening/stage2_screening_ledger.csv")
    p.add_argument("--batch-size",type=int,default=25)
    p.add_argument("--outdir",default="artifacts/screening/stage2_acquisition_batches")
    a=p.parse_args()
    with open(a.ledger,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    if len(rows)!=659 or len({r["record_id"] for r in rows})!=659:
        raise SystemExit("FAIL expected 659 unique Stage-2 records")
    rows=sorted(rows,key=lambda r: hashlib.sha256(r["record_id"].encode()).hexdigest())
    out=Path(a.outdir);out.mkdir(parents=True,exist_ok=True)
    for start in range(0,len(rows),a.batch_size):
        chunk=rows[start:start+a.batch_size]; bid=f"B{start//a.batch_size+1:02d}"
        with open(out/f"{bid}.csv","w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
            for r in chunk:w.writerow({"record_id":r["record_id"],"batch_id":bid,"full_text_status":"pending","source_type":"","source_location":"","source_identifier":"","access_checked":"no","verification_status":"pending","notes":""})
    print(f"Created {(len(rows)+a.batch_size-1)//a.batch_size} deterministic acquisition batches for {len(rows)} records.")

if __name__=="__main__": main()
