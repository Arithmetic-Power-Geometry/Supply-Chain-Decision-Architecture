"""Retrieve OpenAlex works for a frozen search family and preserve raw JSON.

Usage:
 python scripts/retrieve_openalex.py --search-id O001 --query "supply chain management"

Network access is required. Raw pages are evidence and must not be edited.
"""

from __future__ import annotations
import argparse, datetime as dt, hashlib, json, time, urllib.parse, urllib.request
from pathlib import Path

BASE="https://api.openalex.org/works"

def fetch(url: str) -> dict:
    req=urllib.request.Request(url,headers={"User-Agent":"SCDA-research/0.1"})
    with urllib.request.urlopen(req,timeout=60) as r:
        return json.load(r)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--search-id",required=True)
    ap.add_argument("--query",required=True)
    ap.add_argument("--out-dir",default="data/raw/openalex")
    ap.add_argument("--per-page",type=int,default=100)
    ap.add_argument("--max-pages",type=int,default=0,help="0 retrieves until cursor exhaustion")
    a=ap.parse_args()

    out=Path(a.out_dir)/a.search_id
    out.mkdir(parents=True,exist_ok=True)
    cursor="*"; page=0; total=None; manifest=[]
    while cursor:
        params={"search":a.query,"filter":"from_publication_date:1900-01-01,to_publication_date:2026-10-01",
                "per-page":str(a.per_page),"cursor":cursor}
        url=BASE+"?"+urllib.parse.urlencode(params)
        obj=fetch(url); page+=1
        if total is None: total=obj.get("meta",{}).get("count")
        p=out/f"page_{page:05d}.json"
        raw=(json.dumps(obj,ensure_ascii=False,sort_keys=True)+"\n").encode()
        p.write_bytes(raw)
        manifest.append({"page":page,"file":p.name,"sha256":hashlib.sha256(raw).hexdigest(),
                         "records":len(obj.get("results",[]))})
        cursor=obj.get("meta",{}).get("next_cursor")
        if not obj.get("results") or (a.max_pages and page>=a.max_pages): break
        time.sleep(0.12)
    meta={"search_id":a.search_id,"query":a.query,
          "executed_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
          "reported_count":total,"pages_retrieved":page,"manifest":manifest}
    (out/"retrieval_manifest.json").write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__": main()
