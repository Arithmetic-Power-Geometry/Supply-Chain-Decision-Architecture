"""Generate preregistered candidate-corpus quality diagnostics."""
import csv,json,collections
from pathlib import Path
p=Path("artifacts/corpus/openalex_candidate_corpus.csv")
if not p.exists(): raise SystemExit("candidate corpus missing")
with p.open(encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
def era(y):
    try:y=int(y)
    except:return "unknown"
    if y<2005:return "pre-2005"
    if y<=2014:return "2005-2014"
    if y<=2019:return "2015-2019"
    if y<=2023:return "2020-2023"
    if y<=2026:return "2024-2026"
    return "post-boundary"
def nonempty(k):return sum(bool((r.get(k) or "").strip()) for r in rows)
eras=collections.Counter(era(r.get("year")) for r in rows)
families=collections.Counter()
for r in rows:
    for q in (r.get("search_family") or "").split(";"):
        if q:families[q]+=1
n=len(rows)
out={"candidate_records":n,"doi_n":nonempty("doi"),"doi_rate":nonempty("doi")/n if n else 0,
"abstract_n":nonempty("abstract"),"abstract_rate":nonempty("abstract")/n if n else 0,
"venue_n":nonempty("venue"),"venue_rate":nonempty("venue")/n if n else 0,
"era_counts":dict(sorted(eras.items())),"query_family_membership":dict(sorted(families.items())),
"interpretation":"retrieval diagnostics only; not an included-study or SCDA-coded corpus"}
Path("artifacts/corpus/candidate_quality_v1.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
