"""Matched-case tests for incremental value of SCDA evidence maturity V."""
from collections import defaultdict,Counter
LEVELS=["conceptual","synthetic","simulation","benchmark","case study","observational","pilot","deployed","longitudinal"]
RANK={v:i for i,v in enumerate(LEVELS)}
MATCH_DIMS=["decision_level","process","flow","objective","theory","method","technology"]
def key(r): return tuple((r.get(d) or "").strip().lower() for d in MATCH_DIMS)
def matched_groups(rows,min_size=2):
    g=defaultdict(list)
    for r in rows:g[key(r)].append(r)
    return {k:v for k,v in g.items() if len(v)>=min_size}
def evaluate(rows):
    groups=matched_groups(rows); informative=[]; invariant=[]
    for k,rs in groups.items():
        ev=[(r.get("evidence_maturity") or "").strip().lower() for r in rs]
        valid=[e for e in ev if e in RANK]
        uniq=sorted(set(valid),key=lambda x:RANK[x])
        rec={"match_key":k,"claims":len(rs),"studies":len(set((r.get("study_id") or "").strip() for r in rs)),
             "evidence_levels":uniq,"level_count":len(uniq),
             "rank_span":(max(RANK[e] for e in valid)-min(RANK[e] for e in valid)) if valid else None}
        (informative if len(uniq)>1 else invariant).append(rec)
    return {"matched_groups":len(groups),"groups_with_evidence_variation":len(informative),
            "groups_without_evidence_variation":len(invariant),
            "variation_rate":len(informative)/len(groups) if groups else 0,
            "informative_groups":informative,"invariant_groups":invariant,
            "interpretation":"Diagnostic of incremental descriptive information in V; not causal evidence and not proof of managerial effectiveness."}
