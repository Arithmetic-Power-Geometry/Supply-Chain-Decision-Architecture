from dataclasses import dataclass, asdict
from typing import Iterable


ALLOWED = {
    "level": {"strategic", "tactical", "operational", "real-time/autonomous"},
    "process": {"plan", "source", "make", "store", "move", "deliver", "return", "recover", "enable"},
    "flow": {"material", "information", "financial", "knowledge", "risk", "carbon"},
    "objective": {"cost", "service", "quality", "speed", "flexibility", "resilience", "sustainability", "trust"},
    "method": {"conceptual", "empirical", "optimization", "simulation", "statistics", "machine learning", "artificial intelligence", "multi-agent/autonomous"},
    "evidence": {"conceptual", "synthetic", "simulation", "benchmark", "case study", "observational", "pilot", "deployed", "longitudinal"},
}


@dataclass(frozen=True)
class DecisionRecord:
    identifier: str
    level: str
    process: str
    flow: str
    objective: str
    theory: str
    method: str
    technology: str
    evidence: str
    industry: str

    def validate(self) -> None:
        values = asdict(self)
        for field, domain in ALLOWED.items():
            if values[field] not in domain:
                raise ValueError(f"Invalid {field}: {values[field]}")


class DecisionArchitecture:
    dimensions = (
        "level",
        "process",
        "flow",
        "objective",
        "theory",
        "method",
        "technology",
        "evidence",
        "industry",
    )

    def __init__(self, records: Iterable[DecisionRecord]):
        self.records = tuple(records)
        for record in self.records:
            record.validate()

    def signature(self, record: DecisionRecord, dimensions=None):
        dims = tuple(dimensions or self.dimensions)
        return tuple(getattr(record, dim) for dim in dims)

    def group(self, dimensions=None):
        groups = {}
        for record in self.records:
            key = self.signature(record, dimensions)
            groups.setdefault(key, []).append(record.identifier)
        return groups
