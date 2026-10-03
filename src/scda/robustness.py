"""Robustness battery for SCDA architecture selection."""
from __future__ import annotations
import hashlib,random
from collections import defaultdict,Counter
from .model_competition import compete,MODELS
DIMS=MODELS["SCDA9"]
def complete_case(rows,dims=DIMS):
    return [r for r in rows if all((r.get(d) or "").strip() for d in dims)]
def explicit_missing(rows,dims=DIMS):
    out=[]
    for r in rows:
        q=dict(r)
        for d in dims:
            if not (q.get(d) or "").strip():q[d]="__missing__"
        out.append(q)
    return out
def study_bootstrap(rows,n=500,seed="scda-robustness-v1",tol=.02,lam=.02):
    groups=defaultdict(list)
    for r in rows:groups[(r.get("study_id") or "").strip()].append(r)
    ids=sorted(k for k in groups if k)
    if not ids:return {"replicates":0,"selection_counts":{}}
    s=int(hashlib.sha256(seed.encode()).hexdigest()[:16],16);rng=random.Random(s)
    c=Counter()
    for _ in range(n):
        draw=[rng.choice(ids) for __ in ids]
        sample=[]
        for j,sid in enumerate(draw):
            for r in groups[sid]:
                q=dict(r);q["study_id"]=f"{sid}__boot{j}";sample.append(q)
        c[compete(sample,lam,tol)["selection"]["smallest_adequate_model"]]+=1
    return {"replicates":n,"selection_counts":dict(c),
            "selection_rates":{k:v/n for k,v in c.items()}}
def battery(rows,bootstrap_n=500):
    scenarios=[]
    for policy,data in (("available_fields",rows),("complete_case_scda9",complete_case(rows)),("explicit_missing",explicit_missing(rows))):
        for tol in (0,.01,.02,.05):
            for lam in (0,.01,.02,.03,.05):
                x=compete(data,lam,tol)
                scenarios.append({"missing_policy":policy,"collision_tolerance":tol,"lambda":lam,
                                  "claims":len(data),"selected":x["selection"]["smallest_adequate_model"]})
    boot=study_bootstrap(rows,bootstrap_n)
    return {"scenarios":scenarios,"scenario_selection_counts":dict(Counter(x["selected"] for x in scenarios)),
            "study_bootstrap":boot,
            "annotation_views":{"core_KS7":"K+S core; V and I treated as annotations",
                                "core_KSV8":"K+S+V core; I treated as annotation",
                                "core_SCDA9":"K+S+V+I all core"},
            "warning":"Sensitivity analyses diagnose stability; they do not license choosing the scenario that favors a preferred architecture."}
