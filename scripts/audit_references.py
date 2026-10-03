"""Audit BibTeX keys, DOI duplication, and manuscript citation coverage."""
import argparse,re,json
from pathlib import Path
def audit(tex,bib):
 t=Path(tex).read_text(encoding="utf-8");b=Path(bib).read_text(encoding="utf-8")
 entries=re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)",b,re.S)
 keys=[k.strip() for k,_ in entries]
 dois={}
 for k,body in entries:
  m=re.search(r"\bdoi\s*=\s*[\{\"]([^\}\"]+)",body,re.I)
  if m:dois.setdefault(m.group(1).strip().lower(),[]).append(k.strip())
 cites=[]
 for m in re.finditer(r"\\cite\w*\s*\{([^}]+)\}",t):
  cites.extend(x.strip() for x in m.group(1).split(",") if x.strip())
 ks=set(keys);cs=set(cites)
 return {"bib_entries":len(keys),"cited_keys":len(cs),"duplicate_bib_keys":sorted(k for k in set(keys) if keys.count(k)>1),
 "duplicate_dois":{d:k for d,k in dois.items() if len(k)>1},
 "cited_missing_from_bib":sorted(cs-ks),"bib_uncited_in_manuscript":sorted(ks-cs),
 "status":"pass" if not (cs-ks or any(keys.count(k)>1 for k in set(keys)) or any(len(v)>1 for v in dois.values())) else "fail",
 "note":"Uncited bibliography entries are reported for review but do not alone fail this audit."}
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("tex");ap.add_argument("bib");ap.add_argument("--out",default="artifacts/integrity/reference_audit_v1.json");a=ap.parse_args()
 x=audit(a.tex,a.bib);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+"\n");print(json.dumps(x,indent=2));raise SystemExit(1 if x["status"]=="fail" else 0)
