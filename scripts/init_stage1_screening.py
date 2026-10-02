"""Initialize Stage-1 title/abstract screening ledger without making review decisions."""
import argparse,csv,sys
from pathlib import Path
FIELDS=["record_id","openalex_id","doi","title","year","search_family","stage","decision","exclusion_reason","study_type","fulltext_status","reviewer","confidence","adjudication_required","notes"]
def run(inp,out):
 with open(inp,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
 if "record_id" not in (rows[0].keys() if rows else []):
  print("stable record_id required",file=sys.stderr);return 1
 ids=[r["record_id"] for r in rows]
 if len(ids)!=len(set(ids)) or any(not x for x in ids):
  print("record_id missing or duplicated",file=sys.stderr);return 1
 Path(out).parent.mkdir(parents=True,exist_ok=True)
 with open(out,"w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
  for r in rows:
   w.writerow({"record_id":r["record_id"],"openalex_id":r.get("openalex_id",""),"doi":r.get("doi",""),
    "title":r.get("title",""),"year":r.get("year",""),"search_family":r.get("query_families",""),
    "stage":"title_abstract","decision":"","exclusion_reason":"","study_type":"","fulltext_status":"",
    "reviewer":"","confidence":"","adjudication_required":"","notes":""})
 print(f"initialized {len(rows)} undecided Stage-1 records")
 return 0
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("candidate");ap.add_argument("--out",default="artifacts/screening/screening_stage1_blank_v1.csv");a=ap.parse_args();raise SystemExit(run(a.candidate,a.out))
