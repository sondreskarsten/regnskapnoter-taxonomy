"""Validate mappings/to-build-tables.csv coverage and concept_id references.

Checks:
1. Every (build_table, build_table_column) row has a non-empty regnskap_no_concept_id
   (or an explicit "explicitly unmapped" / "UNMAPPED" note).
2. Every regnskap_no_concept_id referenced exists in the taxonomy concepts/axes.
3. Coverage rate >= 95% non-empty mappings (criterion §10.1 #3).

Exits non-zero on any violation.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pyarrow.parquet as pq

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ARTIFACTS = REPO_ROOT / "artifacts"
MAPPING_CSV = REPO_ROOT / "mappings" / "to-build-tables.csv"


def main() -> int:
    if not MAPPING_CSV.exists():
        print(f"MISSING: {MAPPING_CSV}", file=sys.stderr)
        return 1

    if not (ARTIFACTS / "concepts.parquet").exists():
        print(f"MISSING: {ARTIFACTS / 'concepts.parquet'}", file=sys.stderr)
        return 1

    concepts = {x["concept_id"] for x in pq.read_table(ARTIFACTS / "concepts.parquet").to_pylist()}
    axes = {x["axis_id"] for x in pq.read_table(ARTIFACTS / "axes.parquet").to_pylist()}
    valid_ids = concepts | axes

    violations: list[str] = []
    total = 0
    mapped = 0

    with MAPPING_CSV.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            cid = row["regnskap_no_concept_id"].strip()
            note = row.get("note", "").strip()
            table = row["build_table"]
            col = row["build_table_column"]

            if cid:
                mapped += 1
                if cid not in valid_ids:
                    violations.append(f"REF: {table}.{col} -> '{cid}' is not a valid concept_id or axis_id")
            elif note != "explicitly unmapped (metadata/EAV detail/no semantic concept)":
                violations.append(f"UNMAPPED: {table}.{col} (note='{note}')")

    if total == 0:
        violations.append("MAPPING CSV is empty")

    coverage = mapped / total if total else 0
    print(f"  build_tables mapping: {mapped}/{total} = {coverage:.0%}")
    if coverage < 0.95:
        violations.append(f"COVERAGE: {coverage:.0%} < 95% threshold")

    if violations:
        for v in violations:
            print(f"VIOLATION: {v}", file=sys.stderr)
        print(f"{len(violations)} build_tables mapping violation(s)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
