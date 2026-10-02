#!/usr/bin/env python3
import argparse,csv,hashlib,re
from pathlib import Path

FIELDS=["record_id","batch_id","openalex_id","doi","title","year","search_family","abstract","source_status","source_type","source_identifier","source_location","bibliographic_verified","full_text_status","eligibility_decision","exclusion_reason","study_type","reviewer","confidence","adjudication_required","evidence_note"]

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--batch-id",required=True,help="B01..B27")
 p.add_argument("--ledger",default="artifacts/screening/stage2_screening_ledger.csv")
 p.add_argument("--corpus",default="artifacts/corpus/openalex_candidate_corpus_stable.csv")
 p.add_argument("--output-dir",default="artifacts/screening/stage2_execution")
 p.add_argument("--batch-dir",default="",help="Deprecated; batch membership is reconstructed from the frozen Stage-2 ledger.")
 a=p.parse_args()
 bid=a.batch_id.upper()
 if not re.fullmatch(r"B(?:0[1-9]|1[0-9]|2[0-7])",bid): raise SystemExit("FAIL batch-id must be B01..B27")
 ledger_path=Path(a.ledger)
 if not ledger_path.exists(): raise SystemExit(f"FAIL Stage-2 ledger missing: {ledger_path.resolve()}")
 with ledger_path.open(newline="",encoding="utf-8") as f: ledger=list(csv.DictReader(f))
 if len(ledger)!=659 or len({x["record_id"] for x in ledger})!=659: raise SystemExit("FAIL expected 659 unique Stage-2 ledger records")
 ordered=sorted(ledger,key=lambda r: hashlib.sha256(r["record_id"].encode()).hexdigest())
 idx=int(bid[1:])-1
 batch=ordered[idx*25:(idx+1)*25]
 expected=9 if bid=="B27" else 25
 if len(batch)!=expected or len({x["record_id"] for x in batch})!=expected: raise SystemExit(f"FAIL {bid} expected {expected} unique records")
 corpus_path=Path(a.corpus)
 if not corpus_path.exists(): raise SystemExit(f"FAIL stable corpus missing: {corpus_path.resolve()}")
 with corpus_path.open(newline="",encoding="utf-8") as f: corpus={x["record_id"]:x for x in csv.DictReader(f)}
 missing=[x["record_id"] for x in batch if x["record_id"] not in corpus]
 if missing: raise SystemExit(f"FAIL metadata missing for {missing}")
 out=Path(a.output_dir)/f"{bid}_source_verification_enriched.csv";out.parent.mkdir(parents=True,exist_ok=True)
 with out.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
  for x in batch:
   m=corpus[x["record_id"]]
   w.writerow({"record_id":x["record_id"],"batch_id":bid,"openalex_id":m.get("openalex_id",""),"doi":m.get("doi",""),"title":m.get("title",""),"year":m.get("year",""),"search_family":m.get("search_family",""),"abstract":m.get("abstract",""),"source_status":"pending","source_type":"","source_identifier":"","source_location":"","bibliographic_verified":"no","full_text_status":"pending","eligibility_decision":"","exclusion_reason":"","study_type":"","reviewer":"Reviewer A (AI-assisted)","confidence":"","adjudication_required":"yes","evidence_note":""})
 print(f"{bid}: reconstructed deterministically from frozen Stage-2 ledger and enriched {expected} records; no eligibility decisions generated.")

if __name__=="__main__": main()
