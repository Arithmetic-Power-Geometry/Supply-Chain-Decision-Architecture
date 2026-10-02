"""Detect common author-identifying strings in a blinded LaTeX manuscript."""
import argparse,re,json
from pathlib import Path
PATTERNS={"author_name":[r"mohammad\s+amir\s+khusru\s+akhtar",r"md\.?\s+saifullah\s+khalid"],
"institution":[r"usha\s+martin\s+university"],"personal_email":[r"[\w.+-]+@[\w.-]+\.[a-z]{2,}"],
"repository_identity":[r"github\.com/Arithmetic-Power-Geometry",r"zenodo\.\d+",r"orcid\.org/"]}
def audit(path):
 t=Path(path).read_text(encoding="utf-8",errors="ignore");hits={}
 for k,ps in PATTERNS.items():
  vals=[]
  for p in ps: vals += [m.group(0) for m in re.finditer(p,t,re.I)]
  if vals:hits[k]=sorted(set(vals))
 return {"hits":hits,"status":"pass" if not hits else "fail",
 "note":"Static identity screen; manual double-blind review remains required."}
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("tex");ap.add_argument("--out",default="artifacts/paper/blind_audit_v1.json");a=ap.parse_args()
 x=audit(a.tex);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+"\n");print(json.dumps(x,indent=2));raise SystemExit(1 if x["hits"] else 0)
