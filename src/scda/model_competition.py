"""Nested SCDA competition with parsimony and study-cluster diagnostics."""
from collections import Counter,defaultdict
from math import log2
MODELS={"K4":["decision_level","process","flow","objective"],
"KS7":["decision_level","process","flow","objective","theory","method","technology"],
"KSV8":["decision_level","process","flow","objective","theory","method","technology","evidence_maturity"],
"SCDA9":["decision_level","process","flow","objective","theory","method","technology","evidence_maturity","context"]}
def _sig(r,dims): return tuple((r.get(d) or "").strip() for d in dims)
def entropy(vals):
    if not vals:return 0.
    c=Counter(vals);n=len(vals)
    return -sum((v/n)*log2(v/n) for v in c.values())
def metrics(rows,dims):
    sig=[_sig(r,dims) for r in rows]; c=Counter(sig); n=len(rows)
    collision=sum(v for v in c.values() if v>1)/n if n else 0
    cov=sum(bool(x) for s in sig for x in s)/(n*len(dims)) if n and dims else 0
    return {"dimensions":len(dims),"coverage":cov,"collision_rate":collision,
            "distinct_signatures":len(c),"signature_entropy":entropy(sig)}
def compete(rows,lambda_complexity=.02,collision_tolerance=.02):
    out={}
    for name,dims in MODELS.items():
        m=metrics(rows,dims)
        m["parsimony_score"]=(1-m["collision_rate"])*m["coverage"]-lambda_complexity*len(dims)
        out[name]=m
    best_collision=min(v["collision_rate"] for v in out.values())
    adequate=[k for k,v in out.items() if v["collision_rate"]<=best_collision+collision_tolerance]
    selected=min(adequate,key=lambda k:(len(MODELS[k]),-out[k]["coverage"])) if adequate else None
    return {"models":out,"selection":{"collision_tolerance":collision_tolerance,
        "complexity_penalty_per_dimension":lambda_complexity,
        "smallest_adequate_model":selected,
        "rule":"smallest model within collision tolerance of best observed collision; report coverage and sensitivity to penalty/tolerance"}}
def leave_one_out(rows,model="SCDA9"):
    dims=MODELS[model]; base=metrics(rows,dims); ans=[]
    for d in dims:
        m=metrics(rows,[x for x in dims if x!=d]);m["removed"]=d
        m["collision_increase"]=m["collision_rate"]-base["collision_rate"];ans.append(m)
    return ans
def study_cluster_summary(rows,model="SCDA9"):
    groups=defaultdict(list)
    for r in rows: groups[(r.get("study_id") or "").strip()].append(r)
    dims=MODELS[model]
    return {"studies":len([k for k in groups if k]),"claims":len(rows),
        "multi_claim_studies":sum(len(v)>1 for k,v in groups.items() if k),
        "study_signature_sets":{k:len(set(_sig(r,dims) for r in v)) for k,v in groups.items() if k}}
