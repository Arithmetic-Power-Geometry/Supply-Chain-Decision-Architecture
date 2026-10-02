#!/usr/bin/env python3
import argparse, csv, glob
from pathlib import Path

def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--batches", default="data/screening/adjudication_source_batch*_v1.csv")
    ap.add_argument("--out", required=True)
    args=ap.parse_args()

    base=read_rows(args.base)
    if len(base)!=705:
        raise SystemExit(f"Expected 705 base rows, found {len(base)}")
    ids=[r["record_id"] for r in base]
    if len(set(ids))!=705:
        raise SystemExit("Base ledger record_id values are not unique")

    updates={}
    for path in sorted(glob.glob(args.batches)):
        for r in read_rows(path):
            rid=r["record_id"]
            if rid in updates:
                raise SystemExit(f"Duplicate adjudication record_id: {rid}")
            updates[rid]=r
    if len(updates)!=147:
        raise SystemExit(f"Expected 147 adjudications, found {len(updates)}")
    missing=set(updates)-set(ids)
    if missing:
        raise SystemExit(f"Adjudication IDs absent from base: {sorted(missing)}")

    for r in base:
        u=updates.get(r["record_id"])
        if not u: continue
        r["decision"]=u["decision"]
        r["exclusion_reason"]=u.get("exclusion_reason","")
        r["study_type"]=u.get("study_type","")
        if "adjudication_required" in r: r["adjudication_required"]="no"
        if "notes" in r:
            r["notes"]=(r.get("notes","")+" | Source-adjudicated; "+u.get("source","")).strip(" |")

    fields=list(base[0])
    Path(args.out).parent.mkdir(parents=True,exist_ok=True)
    with open(args.out,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(base)

    counts={}
    for r in base: counts[r["decision"]]=counts.get(r["decision"],0)+1
    print({"rows":len(base),"unique_ids":len(set(ids)),"adjudications":len(updates),"decisions":counts})

if __name__=="__main__":
    main()
