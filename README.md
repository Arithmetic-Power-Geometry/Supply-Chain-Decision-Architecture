# Supply Chain Decision Architecture

A research software and evidence repository for a cross-disciplinary decision architecture for supply chain management.

The project develops a formal representation of supply-chain decisions across management, operations research, analytics, and artificial intelligence. The repository operationalizes the concept as software, evaluates it through reproducible benchmarks, and preserves workflow-generated evidence.

## Research sequence

1. **Concept** — define the supply-chain decision architecture and its dimensions.
2. **Software** — implement a transparent classification and comparison engine.
3. **Evaluation** — test deterministic behavior, coverage, consistency, and baseline comparisons.
4. **Workflow evidence** — generate auditable artifacts through GitHub Actions.
5. **Research reporting** — use the resulting evidence in scholarly analysis.

## Core architecture

A supply-chain study or decision instance is represented across nine dimensions:

- decision level
- supply-chain process
- flow
- managerial objective
- theoretical lens
- analytical/modeling method
- enabling technology
- evidence maturity
- industry context

The architecture separates the **decision problem** from the **method used to solve it** and the **technology used to enable it**.

## Repository structure

```
concept/                 Conceptual specification and research propositions
src/scda/                Reference implementation
tests/                   Unit and reproducibility tests
benchmarks/              Benchmark cases and comparison runner
artifacts/               Workflow-generated evidence outputs
.github/workflows/        Continuous integration and evidence workflow
```

## Reproducibility

The GitHub Actions workflow installs the package, runs the test suite, executes benchmark comparisons, and publishes generated evidence as workflow artifacts.

Local execution:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python benchmarks/run_benchmark.py
```

## License

Code in this repository is released under the Apache License 2.0.

Copyright © 2026 Mohammad Amir Khusru Akhtar.
