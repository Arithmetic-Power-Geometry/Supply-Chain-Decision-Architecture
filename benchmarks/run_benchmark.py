import csv
import json
from pathlib import Path

from scda import DecisionRecord, DecisionArchitecture, coverage, collision_rate, distinguishability


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "benchmarks" / "cases.csv"
ARTIFACT_DIR = ROOT / "artifacts"
ARTIFACT_DIR.mkdir(exist_ok=True)


def load_records():
    with CASES.open(newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        return [DecisionRecord(**row) for row in rows]


def main():
    records = load_records()
    architecture = DecisionArchitecture(records)

    schemes = {
        "SCDA-9D": list(architecture.dimensions),
        "Function-only": ["process"],
        "Technology-only": ["technology"],
        "Method-only": ["method"],
        "Decision-core": ["level", "process", "objective"],
    }

    results = {}
    for name, dims in schemes.items():
        results[name] = {
            "dimensions": dims,
            "coverage": round(coverage(records, dims), 4),
            "collision_rate": round(collision_rate(architecture, dims), 4),
            "distinguishability": round(distinguishability(architecture, dims), 4),
        }

    out_json = ARTIFACT_DIR / "benchmark_results.json"
    out_csv = ARTIFACT_DIR / "benchmark_results.csv"

    out_json.write_text(json.dumps(results, indent=2), encoding="utf-8")

    with out_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["scheme", "coverage", "collision_rate", "distinguishability"])
        for name, result in results.items():
            writer.writerow([
                name,
                result["coverage"],
                result["collision_rate"],
                result["distinguishability"],
            ])

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
