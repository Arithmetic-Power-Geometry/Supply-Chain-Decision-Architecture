"""Matched-case falsification for incremental value of SCDA context I."""
from collections import defaultdict
MATCH_DIMS=["decision_level","process","flow","objective","theory","method","technology","evidence_maturity"]
def norm(x): return (x or "").strip().lower()
def key(r): return tuple(norm(r.get(d)) for d in MATCH_DIMS)
def matched_groups(rows,min_size=2):
    g=defaultdict(list)
    for r in rows:g[key(r)].append(r)
    return {k:v for k,v in g.items() if len(v)>=min_size}
def evaluate(rows):
    groups=matched_groups(rows); variable=[]; invariant=[]
    for k,rs in groups.items():
        ctx=sorted(set(norm(r.get("context")) for r in rs if norm(r.get("context"))))
        studies=set(norm(r.get("study_id")) for r in rs if norm(r.get("study_id")))
        rec={"match_key":k,"claims":len(rs),"studies":len(studies),
             "contexts":ctx,"context_count":len(ctx),
             "cross_study":len(studies)>=2}
        (variable if len(ctx)>1 else invariant).append(rec)
    cross=[g for g in variable if g["cross_study"]]
    return {"matched_groups":len(groups),"groups_with_context_variation":len(variable),
            "cross_study_groups_with_context_variation":len(cross),
            "groups_without_context_variation":len(invariant),
            "variation_rate":len(variable)/len(groups) if groups else 0,
            "cross_study_variation_rate":len(cross)/len(groups) if groups else 0,
            "variable_groups":variable,"invariant_groups":invariant,
            "interpretation":"Context variation is descriptive evidence of boundary information only; it does not by itself establish context as a core identity dimension."}
