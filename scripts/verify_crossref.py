"""Verify candidate DOI metadata independently against Crossref without mutating source data."""
from __future__ import annotations
import argparse,csv,json,re,time,urllib.error,urllib.parse,urllib.request
from pathlib import Path
from difflib import SequenceMatcher

BASE="https://api.crossref.org/works/"
def norm_doi(x): return re.sub(r"^https?://(dx\.)?doi\.org/","",(x or "").strip().lower())
def norm_text(x): return re.sub(r"[^a-z0-9]+"," ",(x or "").lower()).strip()
def sim(a,b): return SequenceMatcher(None,norm_text(a),norm_text(b)).ratio() if a and b else 0.0
def year_of(m):
    for k in ("published-print","published-online","published","issued","created"):
        parts=(m.get(k) or {}).get("date-parts") or []
        if parts and parts[0]: return parts[0][0]
    return None
def fetch(doi,email=""):
    url=BASE+urllib.parse.quote(doi,safe="")
    if email:url+="?"+urllib.parse.urlencode({"mailto":email})
    req=urllib.request.Request(url,headers={"User-Agent":"SCDA-research/0.2 (metadata verification)"})
    with urllib.request.urlopen(req,timeout=30) as z:return json.load(z)["message"]

ap=argparse.ArgumentParser();ap.add_argument("input_csv")
ap.add_argument("--out",default="artifacts/corpus/crossref_verification_v2.jsonl")
ap.add_argument("--summary",default="artifacts/corpus/crossref_verification_summary_v2.json")
ap.add_argument("--email",default="");ap.add_argument("--sleep",type=float,default=.12)
a=ap.parse_args()
with open(a.input_csv,encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
Path(a.out).parent.mkdir(parents=True,exist_ok=True)
counts={"records":len(rows),"with_doi":0,"verified":0,"not_found":0,"errors":0,
        "title_match_ge_0_90":0,"title_mismatch_lt_0_80":0,"year_mismatch":0}
with open(a.out,"w",encoding="utf-8") as g:
    for i,r in enumerate(rows,1):
        doi=norm_doi(r.get("doi")); 
        if not doi: continue
        counts["with_doi"]+=1
        base={"row_number":i,"openalex_id":r.get("openalex_id",""),"doi":doi,
              "source_title":r.get("title",""),"source_year":r.get("year",""),"source_venue":r.get("venue","")}
        try:
            m=fetch(doi,a.email); ct=(m.get("title") or [""])[0]; cy=year_of(m); s=sim(base["source_title"],ct)
            ym=bool(base["source_year"] and cy and str(base["source_year"])!=str(cy))
            rec={**base,"status":"verified","crossref_title":ct,"crossref_year":cy,
                 "crossref_container":(m.get("container-title") or [""])[0],
                 "crossref_type":m.get("type",""),"title_similarity":round(s,4),"year_mismatch":ym}
            counts["verified"]+=1
            if s>=.90:counts["title_match_ge_0_90"]+=1
            if s<.80:counts["title_mismatch_lt_0_80"]+=1
            if ym:counts["year_mismatch"]+=1
        except urllib.error.HTTPError as e:
            rec={**base,"status":"not_found" if e.code==404 else "http_error","http_code":e.code}
            counts["not_found" if e.code==404 else "errors"]+=1
        except Exception as e:
            rec={**base,"status":"error","error_type":type(e).__name__};counts["errors"]+=1
        g.write(json.dumps(rec,ensure_ascii=False)+"\n");time.sleep(a.sleep)
counts["doi_rate"]=round(counts["with_doi"]/counts["records"],6) if counts["records"] else 0
counts["verified_rate_among_doi"]=round(counts["verified"]/counts["with_doi"],6) if counts["with_doi"] else 0
counts["interpretation"]="Independent metadata audit only. Source records are never silently overwritten."
Path(a.summary).write_text(json.dumps(counts,indent=2)+"\n",encoding="utf-8")
print(json.dumps(counts,indent=2))
