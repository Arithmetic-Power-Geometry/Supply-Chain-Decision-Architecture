"""Complexity-aware evaluation metrics for coded SCM frameworks."""

from __future__ import annotations
from collections import Counter
from math import log2
from typing import Iterable, Mapping, Sequence

def entropy(values: Iterable[str]) -> float:
    vals=[v for v in values if v not in ("", None)]
    n=len(vals)
    if n == 0:
        return 0.0
    c=Counter(vals)
    return -sum((k/n)*log2(k/n) for k in c.values())

def normalized_entropy(values: Iterable[str]) -> float:
    vals=[v for v in values if v not in ("", None)]
    if len(vals) <= 1:
        return 0.0
    unique=len(set(vals))
    if unique <= 1:
        return 0.0
    return entropy(vals)/log2(unique)

def signatures(rows: Sequence[Mapping[str,str]], dims: Sequence[str]) -> list[tuple[str,...]]:
    return [tuple(str(r.get(d,"")) for d in dims) for r in rows]

def collision_rate_from_signatures(sigs: Sequence[tuple[str,...]]) -> float:
    if not sigs:
        return 0.0
    counts=Counter(sigs)
    collided=sum(n for n in counts.values() if n > 1)
    return collided/len(sigs)

def coverage(rows: Sequence[Mapping[str,str]], dims: Sequence[str]) -> float:
    if not rows or not dims:
        return 0.0
    total=len(rows)*len(dims)
    present=sum(1 for r in rows for d in dims if str(r.get(d,"")).strip())
    return present/total

def ablation(rows: Sequence[Mapping[str,str]], dims: Sequence[str]) -> list[dict]:
    base=signatures(rows,dims)
    base_collision=collision_rate_from_signatures(base)
    out=[]
    for removed in dims:
        kept=[d for d in dims if d != removed]
        sig=signatures(rows,kept)
        collision=collision_rate_from_signatures(sig)
        out.append({
            "removed":removed,
            "dimensions_remaining":len(kept),
            "collision_rate":collision,
            "collision_increase":collision-base_collision,
            "coverage":coverage(rows,kept),
            "signature_entropy":entropy(["|".join(s) for s in sig]),
        })
    return out
