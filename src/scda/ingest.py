"""Normalize bibliographic exports into the canonical SCDA corpus schema."""

from __future__ import annotations
import csv, hashlib
from pathlib import Path
from .corpus import normalize_doi, normalize_title

ALIASES = {
    "title": ["Title", "Article Title", "Document Title", "title"],
    "year": ["Year", "Publication Year", "Publication Date", "year"],
    "doi": ["DOI", "Doi", "doi"],
    "authors": ["Authors", "Author Full Names", "authors"],
    "abstract": ["Abstract", "abstract"],
    "author_keywords": ["Author Keywords", "Keywords", "author_keywords"],
    "source_title": ["Source title", "Source Title", "Publication Name", "source_title"],
    "document_type": ["Document Type", "Document type", "document_type"],
    "cited_by": ["Cited by", "Times Cited, All Databases", "Times Cited", "cited_by"],
    "source_record_url": ["Link", "URL", "source_record_url"],
}

def _pick(row: dict[str,str], names: list[str]) -> str:
    for n in names:
        if n in row and row[n] is not None:
            return str(row[n]).strip()
    return ""

def file_sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()

def stable_record_id(database: str, search_id: str, doi: str, title: str, ordinal: int) -> str:
    key=normalize_doi(doi) or normalize_title(title) or f"row-{ordinal}"
    digest=hashlib.sha1(f"{database}|{search_id}|{key}".encode()).hexdigest()[:12]
    return f"{database.lower()}-{search_id.lower()}-{digest}"

def ingest_csv(path: str|Path, database: str, search_id: str) -> tuple[list[dict],dict]:
    p=Path(path)
    with p.open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    out=[]
    for i,row in enumerate(rows,1):
        x={k:_pick(row,v) for k,v in ALIASES.items()}
        x["record_id"]=stable_record_id(database,search_id,x["doi"],x["title"],i)
        x["database"]=database
        x["search_id"]=search_id
        x["raw_file"]=p.name
        x["raw_row"]=str(i)
        out.append(x)
    meta={"file":p.name,"sha256":file_sha256(p),"database":database,
          "search_id":search_id,"rows":len(rows)}
    return out,meta
