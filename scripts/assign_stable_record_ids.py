"""Assign deterministic stable record IDs to a candidate corpus."""
import argparse,csv,hashlib,sys
from pathlib import Path
def normdoi(x):
 x=(x or "").strip().lower()
 for p in ("https://doi.org/","http://doi.org/","doi:"):
  if x.startswith(p):x=x[len(p):]
 return x.rstrip(".,;")
def rid(row):
 doi=normdoi(row.get("doi"))
 oa=(row.get("openalex_id") or "").strip().lower()
 title=" ".join((row.get("title") or "").lower().split())
 key=("doi:"+doi) if doi else (("openalex:"+oa) if oa else "title:"+title)
 return "SCDA-"+hashlib.sha256(key.encode()).hexdigest()[:16].upper()
def run(inp,out):
 with open(inp,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
 ids=[rid(x) for x in rows]
 if len(ids)!=len(set(ids)):
  print("stable ID collision detected",file=sys.stderr);return 1
 fields=["record_id"]+list(rows[0].keys())
 Path(out).parent.mkdir(parents=True,exist_ok=True)
 with open(out,"w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for i,row in zip(ids,rows):w.writerow({"record_id":i,**row})
 print(f"wrote {len(rows)} stable candidate records")
 return 0
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("input");ap.add_argument("--out",default="artifacts/corpus/openalex_candidate_corpus_stable.csv");a=ap.parse_args();raise SystemExit(run(a.input,a.out))
