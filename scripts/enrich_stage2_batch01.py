#!/usr/bin/env python3
import argparse,csv
from pathlib import Path

FIELDS=["record_id","batch_id","openalex_id","doi","title","year","search_family","abstract","source_status","source_type","source_identifier","source_location","bibliographic_verified","full_text_status","eligibility_decision","exclusion_reason","study_type","reviewer","confidence","adjudication_required","evidence_note"]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--batch",default="artifacts/screening/stage2_acquisition_batches/B01.csv")
    p.add_argument("--corpus",default="artifacts/corpus/openalex_candidate_corpus_stable.csv")
    p.add_argument("--output",default="artifacts/screening/stage2_execution/B01_source_verification_enriched.csv")
    a=p.parse_args()
    with open(a.batch,newline="",encoding="utf-8") as f: batch=list(csv.DictReader(f))
    with open(a.corpus,newline="",encoding="utf-8") as f: corpus={x["record_id"]:x for x in csv.DictReader(f)}
    if len(batch)!=25 or len({x["record_id"] for x in batch})!=25: raise SystemExit("FAIL expected 25 unique B01 records")
    missing=[x["record_id"] for x in batch if x["record_id"] not in corpus]
    if missing: raise SystemExit(f"FAIL metadata missing for {missing}")
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
        for x in batch:
            m=corpus[x["record_id"]]
            w.writerow({"record_id":x["record_id"],"batch_id":"B01","openalex_id":m.get("openalex_id",""),"doi":m.get("doi",""),"title":m.get("title",""),"year":m.get("year",""),"search_family":m.get("search_family",""),"abstract":m.get("abstract",""),"source_status":"pending","source_type":"","source_identifier":"","source_location":"","bibliographic_verified":"no","full_text_status":"pending","eligibility_decision":"","exclusion_reason":"","study_type":"","reviewer":"Reviewer A (AI-assisted)","confidence":"","adjudication_required":"yes","evidence_note":""})
    print("Enriched B01 with corpus metadata for 25 records; screening fields remain empty.")

if __name__=="__main__": main()
