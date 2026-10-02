"""Build auditable PRISMA-compatible flow counts from the frozen screening ledger."""
import csv,json,collections,sys
from pathlib import Path
C=Path("artifacts/corpus/openalex_candidate_corpus.csv")
S=Path("data/screening_log_v3.csv")
OUT=Path("artifacts/corpus"); OUT.mkdir(parents=True,exist_ok=True)
if not C.exists(): raise SystemExit("candidate corpus missing")
if not S.exists():
    print("screening log absent: flow generation deferred"); sys.exit(0)
with C.open(encoding="utf-8-sig",newline="") as f:cand=list(csv.DictReader(f))
with S.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
allowed_stage={"title_abstract","full_text"}
allowed_decision={"include","exclude","uncertain"}
reasons={"E01","E02","E03","E04","E05","E06","E07","E08","E09","E10"}
errors=[]
for i,r in enumerate(rows,2):
    if r.get("stage") not in allowed_stage: errors.append(f"row {i}: invalid stage")
    if r.get("decision") not in allowed_decision: errors.append(f"row {i}: invalid decision")
    if r.get("decision")=="exclude" and r.get("exclusion_reason") not in reasons:
        errors.append(f"row {i}: exclusion requires E01-E10")
    if r.get("decision")!="exclude" and r.get("exclusion_reason"):
        errors.append(f"row {i}: exclusion reason on non-excluded record")
key=lambda r:(r.get("record_id") or r.get("openalex_id") or r.get("doi") or "").strip()
by=collections.defaultdict(dict)
for r in rows:
    k=key(r)
    if not k: errors.append("screening row without stable identifier"); continue
    if r["stage"] in by[k]: errors.append(f"{k}: duplicate stage {r['stage']}")
    by[k][r["stage"]]=r
for k,st in by.items():
    ta=st.get("title_abstract"); ft=st.get("full_text")
    if ft and (not ta or ta.get("decision")!="include"):
        errors.append(f"{k}: full-text record lacks title/abstract inclusion")
counts=collections.Counter()
counts["identified_deduplicated"]=len(cand)
for r in rows:
    counts[f"{r['stage']}_{r['decision']}"]+=1
    if r["decision"]=="exclude": counts[f"{r['stage']}_{r['exclusion_reason']}"]+=1
included_primary=sum(1 for st in by.values() if st.get("full_text",{}).get("decision")=="include" and st["full_text"].get("study_type")=="primary")
included_review=sum(1 for st in by.values() if st.get("full_text",{}).get("decision")=="include" and st["full_text"].get("study_type")=="review")
out={"counts":dict(sorted(counts.items())),"included_primary":included_primary,
"included_review":included_review,"unresolved_uncertain":sum(1 for r in rows if r["decision"]=="uncertain"),
"errors":errors,"status":"pass" if not errors else "fail",
"note":"PRISMA-compatible accounting artifact; terminology in the paper must reflect the databases and processes actually executed."}
(OUT/"screening_flow_v1.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
if errors: sys.exit(1)
