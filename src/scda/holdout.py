"""Deterministic publication-level holdouts for SCDA generalization tests."""
from __future__ import annotations
import hashlib
from collections import defaultdict
def bucket(study_id,salt="scda-holdout-v1"):
    h=hashlib.sha256((salt+"|"+study_id).encode()).hexdigest()
    return int(h[:12],16)/float(16**12)
def assign_study(study_id,holdout_fraction=.20,salt="scda-holdout-v1"):
    if not study_id: raise ValueError("study_id required")
    return "holdout" if bucket(study_id,salt)<holdout_fraction else "development"
def publication_split(rows,holdout_fraction=.20,salt="scda-holdout-v1"):
    out=[]
    study_part={}
    for r in rows:
        sid=(r.get("study_id") or "").strip()
        if not sid: raise ValueError("all claims require study_id")
        part=study_part.setdefault(sid,assign_study(sid,holdout_fraction,salt))
        q=dict(r);q["partition"]=part;out.append(q)
    return out
def leakage(rows):
    p=defaultdict(set)
    for r in rows:p[r["study_id"]].add(r["partition"])
    return sorted(k for k,v in p.items() if len(v)>1)
def temporal_holdout(rows,cutoff_year=2024):
    out=[]
    for r in rows:
        y=int(r["year"]) if str(r.get("year","")).strip() else None
        q=dict(r);q["temporal_partition"]="holdout" if y is not None and y>=cutoff_year else "development"
        out.append(q)
    return out
def discipline_holdout(rows,discipline):
    out=[]
    for r in rows:
        q=dict(r);q["discipline_partition"]="holdout" if (r.get("discipline") or "").strip()==discipline else "development"
        out.append(q)
    return out
