"""Verify DOI metadata against the public Crossref REST API."""

from __future__ import annotations
import argparse,csv,json,time,urllib.parse,urllib.request
from pathlib import Path
from scda.corpus import normalize_doi

BASE="https://api.crossref.org/works/"

def fetch(doi,email=""):
    url=BASE+urllib.parse.quote(doi,safe="")
    if email: url+="?"+urllib.parse.urlencode({"mailto":email})
    req=urllib.request.Request(url,headers={"User-Agent":"SCDA-research/0.1"})
    with urllib.request.urlopen(req,timeout=30) as r:
        return json.load(r)["message"]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input_csv")
    ap.add_argument("--doi-column",default="doi")
    ap.add_argument("--out",default="artifacts/corpus/crossref_verification.jsonl")
    ap.add_argument("--email",default="")
    a=ap.parse_args()
    with open(a.input_csv,encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("w",encoding="utf-8") as g:
        for r in rows:
            doi=normalize_doi(r.get(a.doi_column,""))
            if not doi: continue
            try:
                m=fetch(doi,a.email)
                rec={"record_id":r.get("record_id",""),"doi":doi,"status":"verified",
                     "crossref_title":(m.get("title") or [""])[0],
                     "crossref_type":m.get("type",""),
                     "crossref_container":(m.get("container-title") or [""])[0]}
            except Exception as e:
                rec={"record_id":r.get("record_id",""),"doi":doi,"status":"error","error":type(e).__name__}
            g.write(json.dumps(rec,ensure_ascii=False)+"\n"); time.sleep(0.1)

if __name__=="__main__": main()
