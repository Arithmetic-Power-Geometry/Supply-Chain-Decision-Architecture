"""Validate one-to-one terminal screening coverage for a candidate corpus."""
import csv,json,sys
from pathlib import Path
C=Path("artifacts/corpus/openalex_candidate_corpus.csv")
S=Path("data/screening_log_v2.csv")
if not C.exists():
    print("candidate corpus absent: retrieval must run first"); sys.exit(0)
if not S.exists():
    raise SystemExit("screening log missing")
with C.open(encoding="utf-8-sig",newline="") as f: cand=list(csv.DictReader(f))
with S.open(encoding="utf-8-sig",newline="") as f: scr=list(csv.DictReader(f))
def key(r): return (r.get("doi") or r.get("openalex_id") or r.get("record_id") or r.get("title","").strip().lower())
ck=[key(r) for r in cand]; sk=[key(r) for r in scr]
dups=len(sk)-len(set(sk)); missing=set(ck)-set(sk); extra=set(sk)-set(ck)
terminal={"include_primary","include_review","exclude"}
bad=[r for r in scr if r.get("decision") not in terminal|{"uncertain"}]
summary={"candidates":len(cand),"screened_rows":len(scr),"duplicate_screen_keys":dups,
"missing_terminal_or_uncertain_records":len(missing),"extra_screen_records":len(extra),
"invalid_decisions":len(bad)}
Path("artifacts/corpus/screening_validation.json").write_text(json.dumps(summary,indent=2)+"\n")
print(json.dumps(summary,indent=2))
if dups or missing or extra or bad: raise SystemExit("screening validation failed")
