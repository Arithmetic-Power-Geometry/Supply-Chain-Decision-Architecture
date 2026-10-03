"""Validate OpenAlex retrieval provenance before corpus construction."""
import json,hashlib,sys
from pathlib import Path
ROOT=Path("data/raw/openalex"); errors=[]; summary={}
for mf in sorted(ROOT.glob("O*/retrieval_manifest.json")):
    m=json.loads(mf.read_text(encoding="utf-8")); sid=m.get("search_id",mf.parent.name)
    seen=set(); recs=0
    if not m.get("query"): errors.append(f"{sid}: missing query")
    if not m.get("executed_utc"): errors.append(f"{sid}: missing execution timestamp")
    for e in m.get("manifest",[]):
        p=mf.parent/e["file"]
        if not p.exists(): errors.append(f"{sid}: missing {p.name}"); continue
        raw=p.read_bytes(); sha=hashlib.sha256(raw).hexdigest()
        if sha!=e.get("sha256"): errors.append(f"{sid}: checksum mismatch {p.name}")
        obj=json.loads(raw); rs=obj.get("results",[])
        if len(rs)!=e.get("records"): errors.append(f"{sid}: record count mismatch {p.name}")
        recs+=len(rs)
        for x in rs:
            oid=x.get("id")
            if oid and oid in seen: errors.append(f"{sid}: duplicate OpenAlex id {oid}")
            if oid: seen.add(oid)
            y=x.get("publication_year")
            if y and not (1900<=int(y)<=2026): errors.append(f"{sid}: year out of bounds {y}")
    summary[sid]={"pages":m.get("pages_retrieved"),"retrieved_records":recs,
                  "reported_count":m.get("reported_count"),"unique_openalex_ids":len(seen)}
if not summary: errors.append("no retrieval manifests found")
out={"searches":summary,"errors":errors,"status":"pass" if not errors else "fail"}
Path("artifacts/corpus").mkdir(parents=True,exist_ok=True)
Path("artifacts/corpus/retrieval_integrity_v1.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
if errors: sys.exit(1)
