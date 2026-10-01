"""Ingest one or more raw CSV exports using a manifest.

Manifest columns: file,database,search_id,expected_rows
"""

from __future__ import annotations
import argparse,csv,json
from pathlib import Path
from scda.ingest import ingest_csv
from scda.corpus import CorpusRecord, exact_duplicates, normalize_doi, normalize_title

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("manifest_csv")
    ap.add_argument("--raw-dir",default="data/raw")
    ap.add_argument("--out-dir",default="artifacts/corpus")
    a=ap.parse_args()
    raw,out=Path(a.raw_dir),Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    with open(a.manifest_csv,encoding="utf-8-sig",newline="") as f:
        specs=list(csv.DictReader(f))
    allrows=[]; metas=[]
    for s in specs:
        rows,meta=ingest_csv(raw/s["file"],s["database"],s["search_id"])
        expected=s.get("expected_rows","").strip()
        if expected and len(rows)!=int(expected):
            raise SystemExit(f'Row-count mismatch for {s["file"]}: expected {expected}, got {len(rows)}')
        allrows.extend(rows); metas.append(meta)
    recs=[CorpusRecord(r["record_id"],r["title"],r["year"],r["doi"],r["database"],r["search_id"]) for r in allrows]
    dups=exact_duplicates(recs); dupmap={d.duplicate_id:d for d in dups}
    for r in allrows:
        r["normalized_doi"]=normalize_doi(r["doi"]); r["normalized_title"]=normalize_title(r["title"])
        d=dupmap.get(r["record_id"])
        r["dedup_status"]="duplicate" if d else "canonical"
        r["duplicate_of"]=d.canonical_id if d else ""
        r["duplicate_rule"]=d.rule if d else ""
    fields=list(allrows[0]) if allrows else []
    with (out/"canonical_ingest.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(allrows)
    (out/"raw_manifest.json").write_text(json.dumps(metas,indent=2)+"\n",encoding="utf-8")
    summary={"raw_records":len(allrows),"exact_duplicates":len(dups),"canonical_records":len(allrows)-len(dups)}
    (out/"ingest_summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__": main()
