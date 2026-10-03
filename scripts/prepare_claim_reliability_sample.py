#!/usr/bin/env python3
import argparse,csv,hashlib,math
from collections import defaultdict,Counter
from pathlib import Path
DIMS=["decision_level","process","flow","objective","theory","method","technology","evidence_maturity","context"]
OUT=["claim_id","study_id","record_id","claim_text","claim_location","source_support","source_identifier","coder","decision_level","process","flow","objective","theory","method","technology","evidence_maturity","context","confidence","notes"]
def main():
 p=argparse.ArgumentParser();p.add_argument("claims");p.add_argument("--fraction",type=float,default=.20);p.add_argument("--out",default="data/frozen/coder_b_blinded_sample_v1.csv");a=p.parse_args()
 with open(a.claims,encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
 by=defaultdict(list)
 for r in rows: by[r["study_id"]].append(r)
 target=math.ceil(len(rows)*a.fraction)
 def key(s): return hashlib.sha256(("SCDA-CLAIM-REL-v1|"+s).encode()).hexdigest()
 chosen=[];n=0
 for sid in sorted(by,key=key):
  chosen.append(sid);n+=len(by[sid])
  if n>=target: break
 Path(a.out).parent.mkdir(parents=True,exist_ok=True)
 with open(a.out,"w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=OUT);w.writeheader()
  for sid in chosen:
   for r in by[sid]:
    o={k:r.get(k,"") for k in OUT}
    o["coder"]="Coder B";o["confidence"]="";o["notes"]=""
    for d in DIMS:o[d]=""
    w.writerow(o)
 print(f"Prepared blinded clustered Coder-B shell: {n}/{len(rows)} claims ({n/len(rows):.1%}), {len(chosen)} studies; Reviewer-A labels removed.")
if __name__=="__main__":main()
