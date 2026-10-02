"""Managerial decision-usefulness diagnostics for SCDA-coded claims."""
from collections import defaultdict,Counter
VIEWS={
"technology_only":["technology"],
"method_only":["method"],
"solution_only":["theory","method","technology"],
"decision_kernel":["decision_level","process","flow","objective"],
"KS7":["decision_level","process","flow","objective","theory","method","technology"],
"KSV8":["decision_level","process","flow","objective","theory","method","technology","evidence_maturity"],
"SCDA9":["decision_level","process","flow","objective","theory","method","technology","evidence_maturity","context"]}
def norm(x):return (x or "").strip().lower()
def sig(r,dims):return tuple(norm(r.get(d)) for d in dims)
def ambiguity(rows,view_dims,target_dims):
    groups=defaultdict(list)
    for r in rows:groups[sig(r,view_dims)].append(r)
    ambiguous=0;examples=[]
    for k,rs in groups.items():
        targets=set(sig(r,target_dims) for r in rs)
        if len(targets)>1:
            ambiguous+=len(rs)
            examples.append({"view_signature":k,"claims":len(rs),"distinct_target_signatures":len(targets),
                             "study_count":len(set(norm(r.get("study_id")) for r in rs if norm(r.get("study_id"))))})
    return {"claims":len(rows),"ambiguous_claims":ambiguous,
            "ambiguity_rate":ambiguous/len(rows) if rows else 0,"ambiguous_groups":examples}
def evaluate(rows):
    # Does a shallow description hide differences in the managerial decision kernel?
    tech=ambiguity(rows,VIEWS["technology_only"],VIEWS["decision_kernel"])
    method=ambiguity(rows,VIEWS["method_only"],VIEWS["decision_kernel"])
    solution=ambiguity(rows,VIEWS["solution_only"],VIEWS["decision_kernel"])
    # Among same K+S, do readiness/context annotations alter interpretation?
    readiness=ambiguity(rows,VIEWS["KS7"],["evidence_maturity"])
    context=ambiguity(rows,VIEWS["KSV8"],["context"])
    return {"technology_hides_decision":tech,"method_hides_decision":method,
            "solution_hides_decision":solution,"same_KS_different_evidence":readiness,
            "same_KSV_different_context":context,
            "interpretation":"Descriptive decision-usefulness diagnostic only. It does not estimate managerial performance, ROI, adoption success, or causal benefit."}
