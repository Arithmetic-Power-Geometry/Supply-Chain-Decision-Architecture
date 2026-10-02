import hashlib
def _doi(x):
 x=(x or "").strip().lower()
 for p in ("https://doi.org/","http://doi.org/","doi:"):
  if x.startswith(p):x=x[len(p):]
 return x.rstrip(".,;")
def stable_record_id(row):
 d=_doi(row.get("doi"));o=(row.get("openalex_id") or "").strip().lower();t=" ".join((row.get("title") or "").lower().split())
 key=("doi:"+d) if d else (("openalex:"+o) if o else "title:"+t)
 return "SCDA-"+hashlib.sha256(key.encode()).hexdigest()[:16].upper()
