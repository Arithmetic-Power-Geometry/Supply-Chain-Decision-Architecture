"""Prepare a staged corpus from normalized CSV exports.

Input is never modified. Output records retain source database and search_id.
"""

from __future__ import annotations
import argparse, csv, json
from pathlib import Path
from scda.corpus import CorpusRecord, exact_duplicates, normalize_doi, normalize_title

REQUIRED = {"record_id", "title", "database", "search_id"}

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("input_csv")
    p.add_argument("--out-dir", default="artifacts/corpus")
    a = p.parse_args()
    inp, out = Path(a.input_csv), Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    with inp.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    missing = REQUIRED - set(rows[0].keys() if rows else [])
    if missing:
        raise SystemExit(f"Missing required columns: {sorted(missing)}")

    records = [CorpusRecord(
        record_id=r["record_id"], title=r["title"], year=r.get("year",""),
        doi=r.get("doi",""), database=r["database"], search_id=r["search_id"]
    ) for r in rows]
    dups = exact_duplicates(records)
    dup_ids = {d.duplicate_id for d in dups}

    staged = []
    for r in rows:
        x = dict(r)
        x["normalized_doi"] = normalize_doi(r.get("doi"))
        x["normalized_title"] = normalize_title(r.get("title"))
        x["dedup_status"] = "duplicate" if r["record_id"] in dup_ids else "canonical"
        staged.append(x)

    fields = list(staged[0].keys()) if staged else []
    with (out/"staged_records.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(staged)
    with (out/"duplicates.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["canonical_id","duplicate_id","rule"]); w.writeheader()
        w.writerows([d.__dict__ for d in dups])
    summary={"input_records":len(records),"duplicates":len(dups),"canonical_records":len(records)-len(dups)}
    (out/"dedup_summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")

if __name__ == "__main__":
    main()
