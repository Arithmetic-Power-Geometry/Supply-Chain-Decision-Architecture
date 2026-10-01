"""Corpus normalization and deterministic deduplication utilities."""

from __future__ import annotations
import re
from dataclasses import dataclass
from typing import Iterable

_DOI_PREFIX = re.compile(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", re.I)
_NON_ALNUM = re.compile(r"[^a-z0-9]+")

def normalize_doi(value: str | None) -> str:
    if not value:
        return ""
    v = value.strip().lower()
    v = _DOI_PREFIX.sub("", v)
    return v.rstrip(" .;,") if v.startswith("10.") else ""

def normalize_title(value: str | None) -> str:
    if not value:
        return ""
    return " ".join(_NON_ALNUM.sub(" ", value.lower()).split())

@dataclass(frozen=True)
class CorpusRecord:
    record_id: str
    title: str
    year: str = ""
    doi: str = ""
    database: str = ""
    search_id: str = ""

@dataclass(frozen=True)
class DedupResult:
    canonical_id: str
    duplicate_id: str
    rule: str

def exact_duplicates(records: Iterable[CorpusRecord]) -> list[DedupResult]:
    seen_doi: dict[str, str] = {}
    seen_title: dict[str, str] = {}
    out: list[DedupResult] = []
    for r in records:
        doi = normalize_doi(r.doi)
        title = normalize_title(r.title)
        if doi and doi in seen_doi:
            out.append(DedupResult(seen_doi[doi], r.record_id, "exact_doi"))
            continue
        if title and title in seen_title:
            out.append(DedupResult(seen_title[title], r.record_id, "exact_title"))
            continue
        if doi:
            seen_doi[doi] = r.record_id
        if title:
            seen_title[title] = r.record_id
    return out
