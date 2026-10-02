"""Compute pre-adjudication dimension-level inter-coder reliability."""
import argparse,csv,json,math,collections,sys
from pathlib import Path
DIMS=["decision_level","process","flow","objective","theory","method","technology","evidence_maturity","context"]
def load(p):
    with open(p,encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
    out={}
    for r in rows:
        k=(r.get("claim_id") or "").strip()
        if not k: raise ValueError(f"{p}: missing claim_id")
        if k in out: raise ValueError(f"{p}: duplicate claim_id {k}")
        out[k]=r
    return out
def kappa(pairs):
    n=len(pairs)
    if not n:return None
    po=sum(a==b for a,b in pairs)/n
    ca=collections.Counter(a for a,b in pairs); cb=collections.Counter(b for a,b in pairs)
    pe=sum((ca[k]/n)*(cb[k]/n) for k in set(ca)|set(cb))
    if math.isclose(1-pe,0): return 1.0 if math.isclose(po,1) else None
    return (po-pe)/(1-pe)
ap=argparse.ArgumentParser();ap.add_argument("coder_a");ap.add_argument("coder_b")
ap.add_argument("--out",default="artifacts/reliability/intercoder_v1.json");a=ap.parse_args()
A=load(a.coder_a);B=load(a.coder_b); common=sorted(set(A)&set(B))
if not common: raise SystemExit("no matched claim_ids")
res={}
for d in DIMS:
    complete=[]; missing=0
    for k in common:
        x=(A[k].get(d) or "").strip();y=(B[k].get(d) or "").strip()
        if not x or not y: missing+=1;continue
        complete.append((x,y))
    agree=sum(x==y for x,y in complete)
    res[d]={"matched_nonmissing":len(complete),"missing_pairs":missing,
            "raw_agreement":round(agree/len(complete),6) if complete else None,
            "cohen_kappa":round(kappa(complete),6) if kappa(complete) is not None else None}
out={"matched_claims":len(common),"coder_a_only":len(set(A)-set(B)),"coder_b_only":len(set(B)-set(A)),
"dimensions":res,"status":"pre_adjudication","warning":"Reliability must be computed before adjudication; this artifact does not infer or fabricate a second coder."}
p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
