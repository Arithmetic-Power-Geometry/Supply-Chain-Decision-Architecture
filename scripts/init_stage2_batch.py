#!/usr/bin/env python3
import argparse,csv,re
from pathlib import Path

FIELDS=["record_id","batch_id","openalex_id","doi","title","year","search_family","abstract","source_status","source_type","source_identifier","source_location","bibliographic_verified","full_text_status","eligibility_decision","exclusion_reason","study_type","reviewer","confidence","adjudication_required","evidence_note"]

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--batch-id",required=True,help="B01..B27")
 p.add_argument("--batch-dir",default="artifacts/screening/stage2_acquisition_batches")
 p.add_argument("--corpus",default="artifacts/corpus/openalex_candidate_corpus_stable.csv")
 p.add_argument("--output-dir",default="artifacts/screening/stage2_execution")
 a=p.parse_args()
 bid=a.batch_id.upper()
 if not re.fullmatch(r"B(?:0[1-9]|1[0-9]|2[0-7])",bid): raise SystemExit("FAIL batch-id must be B01..B27")
 batch_path=Path(a.batch_dir)/f"{bid}.csv"\n if not batch_path.exists(): raise SystemExit(f"FAIL acquisition batch missing: {batch_path.resolve()}")
 with open(batch_path,newline="",encoding="utf-8") as f: batch=list(csv.DictReader(f))
 expected=9 if bid=="B27" else 25
 if len(batch)!=expected or len({x["record_id"] for x in batch})!=expected: raise SystemExit(f"FAIL {bid} expected {expected} unique records")
 corpus_path=Path(a.corpus)\n if not corpus_path.exists(): raise SystemExit(f"FAIL stable corpus missing: {corpus_path.resolve()}")\n with open(corpus_path,newline="",encoding="utf-8") as f: corpus={x["record_id"]:x for x in csv.DictReader(f)}
 missing=[x["record_id"] for x in batch if x["record_id"] not in corpus]
 if missing: raise SystemExit(f"FAIL metadata missing for {missing}")
 out=Path(a.output_dir)/f"{bid}_source_verification_enriched.csv";out.parent.mkdir(parents=True,exist_ok=True)
 with open(out,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
  for x in batch:
   m=corpus[x["record_id"]]
   w.writerow({"record_id":x["record_id"],"batch_id":bid,"openalex_id":m.get("openalex_id",""),"doi":m.get("doi",""),"title":m.get("title",""),"year":m.get("year",""),"search_family":m.get("search_family",""),"abstract":m.get("abstract",""),"source_status":"pending","source_type":"","source_identifier":"","source_location":"","bibliographic_verified":"no","full_text_status":"pending","eligibility_decision":"","exclusion_reason":"","study_type":"","reviewer":"Reviewer A (AI-assisted)","confidence":"","adjudication_required":"yes","evidence_note":""})
 print(f"{bid}: initialized and enriched {expected} records; no eligibility decisions generated.")
if __name__=="__main__": main()
