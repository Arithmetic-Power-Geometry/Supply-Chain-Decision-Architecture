#!/usr/bin/env python3
"""Recompute SCDA study-level 125-pair agreement without editing frozen outputs.

Usage:
  python EMSUB/scripts/recompute_125_coder_agreement.py \
    'EMSUB/evidence/SCDA_Coder_A_Coder_B_Adjudication_Datasets_FINAL(3).xlsx' \
    --expected data/Final_SCM/Cohen_Kappa_125_FINAL.csv

Requires openpyxl. Treats missing/blank theory labels as an explicit category
to reproduce the historical 125-row summary. This is a reconstruction of the
published calculation, NOT a claim that missing-as-category is methodologically
appropriate or that coders' independent identities are authenticated.
"""
import argparse
import collections
import csv
import json
import math
from pathlib import Path
from openpyxl import load_workbook

DIMS = ("decision_level", "process", "flow", "objective", "theory",
        "method", "technology", "evidence_maturity", "context")

def norm(value):
    return "" if value is None else str(value).strip()

def compute(path):
    wb = load_workbook(path, read_only=True, data_only=True)
    sheet = wb["Coder_A_B_Paired_125"]
    rows = sheet.iter_rows(values_only=True)
    headers = next(rows)
    items = [dict(zip(headers, row)) for row in rows
             if any(value is not None for value in row)]
    ids = [norm(r.get("record_id")) for r in items]
    if not ids or any(not x for x in ids) or len(set(ids)) != len(ids):
        raise ValueError("Missing or duplicate record_id")
    results = []
    for dim in DIMS:
        pairs = [(norm(r.get("A_" + dim)), norm(r.get("B_" + dim)))
                 for r in items]
        n = len(pairs)
        observed = sum(a == b for a, b in pairs) / n
        ca = collections.Counter(a for a, _ in pairs)
        cb = collections.Counter(b for _, b in pairs)
        expected = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n**2
        kappa = ((observed - expected) / (1 - expected)
                 if not math.isclose(expected, 1.0) else
                 (1.0 if math.isclose(observed, 1.0) else None))
        results.append({"dimension": dim, "n": n,
                        "raw_agreement": round(observed, 6),
                        "cohen_kappa": round(kappa, 6) if kappa is not None else None,
                        "blank_a": ca[""], "blank_b": cb[""]})
    return results

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workbook", type=Path)
    ap.add_argument("--expected", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    results = compute(args.workbook)
    if args.expected:
        with args.expected.open(newline="", encoding="utf-8-sig") as fh:
            expected = {r["dimension"]: r for r in csv.DictReader(fh)}
        for r in results:
            e = expected[r["dimension"]]
            assert r["n"] == int(e["n"]), r["dimension"]
            assert abs(r["raw_agreement"] - float(e["raw_agreement"])) < 1e-6, r["dimension"]
            assert abs(r["cohen_kappa"] - float(e["cohen_kappa"])) < 1e-6, r["dimension"]
    output = {"status": "MATCH" if args.expected else "CALCULATED",
              "unit": "record_id / study-level pair",
              "missing_value_policy": "blank is explicit category",
              "results": results}
    rendered = json.dumps(output, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
    print(rendered, end="")

if __name__ == "__main__":
    main()
