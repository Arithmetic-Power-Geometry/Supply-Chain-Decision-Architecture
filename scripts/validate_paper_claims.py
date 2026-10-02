"""Validate manuscript claim-to-artifact alignment."""
import csv,json,sys
from pathlib import Path
CLASSES={"descriptive","comparative","reliability","generalization","managerial_descriptive","methodological"}
STRENGTH={"descriptive","association","comparative","generalization_limited","methodological"}
STATUS={"planned","supported","narrow","remove","pending"}
def nested(obj,path):
 cur=obj
 for p in path.split("."):
  if isinstance(cur,dict) and p in cur:cur=cur[p]
  else:return False,None
 return True,cur
def validate(ledger):
 with open(ledger,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
 errors=[];warnings=[];checked=[]
 for i,r in enumerate(rows,2):
  cid=(r.get("claim_id") or "").strip()
  if not cid:errors.append(f"row {i}: missing claim_id")
  if r.get("claim_class") not in CLASSES:errors.append(f"{cid}: invalid claim_class")
  if r.get("allowed_strength") not in STRENGTH:errors.append(f"{cid}: invalid allowed_strength")
  if r.get("status") not in STATUS:errors.append(f"{cid}: invalid status")
  art=(r.get("artifact_path") or "").strip();field=(r.get("artifact_field") or "").strip()
  exists=Path(art).exists() if art else False;field_ok=None;value=None
  if r.get("status")=="supported":
   if not art:errors.append(f"{cid}: supported claim lacks artifact")
   elif not exists:errors.append(f"{cid}: artifact missing: {art}")
   elif field:
    try:o=json.loads(Path(art).read_text(encoding="utf-8"));field_ok,value=nested(o,field)
    except Exception as e:errors.append(f"{cid}: artifact JSON unreadable: {e}")
    if field_ok is False:errors.append(f"{cid}: artifact field missing: {field}")
  if r.get("claim_class")=="managerial_descriptive" and r.get("allowed_strength") not in {"descriptive","comparative"}:
   errors.append(f"{cid}: managerial descriptive claim exceeds permitted strength")
  checked.append({"claim_id":cid,"artifact_exists":exists,"field_ok":field_ok,"value":value})
 return {"claims":len(rows),"checked":checked,"errors":errors,"warnings":warnings,
 "status":"pass" if not errors else "fail",
 "note":"Alignment verifies declared evidence linkage; semantic prose still requires final human/source audit."}
if __name__=="__main__":
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument("ledger");ap.add_argument("--out",default="artifacts/paper/claim_alignment_v1.json");a=ap.parse_args()
 x=validate(a.ledger);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+"\n");print(json.dumps(x,indent=2));sys.exit(1 if x["errors"] else 0)
