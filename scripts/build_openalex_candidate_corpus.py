"""Build a deduplicated, auditable candidate corpus from OpenAlex raw pages."""
import csv,json,re
from pathlib import Path

RAW=Path("data/raw/openalex"); OUT=Path("artifacts/corpus"); OUT.mkdir(parents=True,exist_ok=True)
def doi(x):
    x=(x or "").lower().strip()
    return re.sub(r"^https?://(dx\.)?doi\.org/","",x)
def abstract(inv):
    if not inv:return ""
    pairs=[]
    for w,poses in inv.items():
        for p in poses:pairs.append((p,w))
    return " ".join(w for _,w in sorted(pairs))
rows=[]
for mf in sorted(RAW.glob("O*/retrieval_manifest.json")):
    fam=mf.parent.name
    meta=json.loads(mf.read_text())
    for pf in sorted(mf.parent.glob("page_*.json")):
        obj=json.loads(pf.read_text())
        for x in obj.get("results",[]):
            rows.append({"search_family":fam,"openalex_id":x.get("id",""),"doi":doi(x.get("doi")),
             "year":x.get("publication_year",""),"title":x.get("title",""),
             "venue":((x.get("primary_location") or {}).get("source") or {}).get("display_name",""),
             "cited_by_count":x.get("cited_by_count",0),"abstract":abstract(x.get("abstract_inverted_index"))})
# DOI first; otherwise normalized title.
def key(r):
    if r["doi"]: return "d:"+r["doi"]
    return "t:"+re.sub(r"[^a-z0-9]+"," ",r["title"].lower()).strip()
merged={}
for r in rows:
    k=key(r)
    if k in merged:
        fams=set(merged[k]["search_family"].split(";"));fams.add(r["search_family"])
        merged[k]["search_family"]=";".join(sorted(fams))
    else: merged[k]=r
out=list(merged.values());out.sort(key=lambda z:(int(z["year"] or 0),z["title"]))
fields=list(out[0]) if out else ["search_family","openalex_id","doi","year","title","venue","cited_by_count","abstract"]
with (OUT/"openalex_candidate_corpus.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(out)
summary={"raw_records":len(rows),"deduplicated_records":len(out),
 "with_doi":sum(bool(r["doi"]) for r in out),"with_abstract":sum(bool(r["abstract"]) for r in out),
 "status":"candidate_corpus_not_yet_scda_coded"}
(OUT/"openalex_candidate_summary.json").write_text(json.dumps(summary,indent=2)+"\n")
print(json.dumps(summary,indent=2))
