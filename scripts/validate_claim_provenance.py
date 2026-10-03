"""Validate claim-to-source provenance without inferring semantic support."""
import csv,json,re,sys
from pathlib import Path
VALID={"verified_support","partial_support","not_supported","pending_review"}
DOI=re.compile(r"^10\.\d{4,9}/\S+$",re.I)
def normdoi(x):
 x=(x or "").strip().lower()
 for p in ("https://doi.org/","http://doi.org/","doi:"): 
  if x.startswith(p): x=x[len(p):]
 return x.rstrip(".,;")
def validate(path):
 with open(path,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
 errors=[];warnings=[];seen=set();stats={k:0 for k in VALID}
 for i,r in enumerate(rows,2):
  cid=(r.get("claim_id") or "").strip();sid=(r.get("study_id") or "").strip()
  if not cid:errors.append(f"row {i}: missing claim_id")
  if not sid:errors.append(f"row {i}: missing study_id")
  if cid in seen:errors.append(f"row {i}: duplicate claim_id {cid}")
  seen.add(cid)
  doi=normdoi(r.get("source_doi"))
  if doi and not DOI.match(doi):warnings.append(f"row {i}: DOI format requires review: {doi}")
  st=(r.get("support_status") or "").strip()
  if st not in VALID:errors.append(f"row {i}: invalid support_status {st}")
  else:stats[st]+=1
  if st!="pending_review" and not (r.get("reviewer") or "").strip():
   errors.append(f"row {i}: reviewed support judgment lacks reviewer")
  if st in {"verified_support","partial_support","not_supported"} and not (r.get("source_locator") or "").strip():
   errors.append(f"row {i}: support judgment lacks source locator")
 return {"records":len(rows),"support_status_counts":stats,"errors":errors,"warnings":warnings,
 "status":"pass" if not errors else "fail",
 "note":"Pass verifies ledger integrity only; it does not independently establish semantic claim support."}
if __name__=="__main__":
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument("ledger");ap.add_argument("--out",default="artifacts/integrity/claim_provenance_validation_v1.json");a=ap.parse_args()
 res=validate(a.ledger);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(res,indent=2)+"\n");print(json.dumps(res,indent=2))
 if res["errors"]:sys.exit(1)
