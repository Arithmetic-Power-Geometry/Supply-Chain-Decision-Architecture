#!/usr/bin/env python3
import csv,glob
from pathlib import Path
files=sorted(glob.glob("data/screening/stage2_b??_verified_decisions_v1.csv"))
files+=sorted(glob.glob("data/screening/stage2_b01_verified_decisions_part*_v1.csv"))
rows=[]
for f in files:
 with open(f,encoding="utf-8-sig",newline="") as h: rows.extend(csv.DictReader(h))
by={}
for r in rows:
 rid=r["record_id"].strip()
 if rid in by and by[rid].get("eligibility_decision")!=r.get("eligibility_decision"): raise SystemExit("conflicting "+rid)
 by[rid]=r
rows=list(by.values())
inc=sum(r.get("eligibility_decision")=="include" for r in rows);exc=sum(r.get("eligibility_decision")=="exclude" for r in rows)
if (len(rows),inc,exc)!=(659,518,141): raise SystemExit(f"FAIL reconciliation rows={len(rows)} include={inc} exclude={exc}")
fields=sorted(k for k in set().union(*(r.keys() for r in rows)) if k is not None)\nfor r in rows: r.pop(None,None)
Path("data/frozen").mkdir(parents=True,exist_ok=True)
with open("data/frozen/stage2_final_manifest_v1.csv","w",encoding="utf-8",newline="") as h:
 w=csv.DictWriter(h,fieldnames=fields);w.writeheader();w.writerows(sorted(rows,key=lambda x:x["record_id"]))
print("PASS Stage-2 659 = 518 include + 141 exclude")
