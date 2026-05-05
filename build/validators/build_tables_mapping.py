"""Validate build_tables column mapping CSV.

Checks:
- Every concept_id referenced exists in concepts.parquet.
- Every axis_id (when non-empty) exists in axes.parquet.
- Every axis_member (when non-empty) exists in axis_members.parquet.
- 100% of non-metadata columns are mapped.
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
        print(f"Mapping CSV not found at {MAPPING_CSV}", file=sys.stderr)
        return 1

    concepts = {x["concept_id"] for x in pq.read_table(ARTIFACTS / "concepts.parquet").to_pylist()}
    axes = {x["axis_id"] for x in pq.read_table(ARTIFACTS / "axes.parquet").to_pylist()}
    members = {x["member_id"] for x in pq.read_table(ARTIFACTS / "axis_members.parquet").to_pylist()}

    errors: list[str] = []
    rows = list(csv.DictReader(MAPPING_CSV.open(encoding="utf-8")))
    unmapped = sum(1 for r in rows if not r.get("concept_id"))
    if unmapped:
        errors.append(f"BUILD_TABLES: {unmapped} unmapped column(s)")
    for r in rows:
        cid = r.get("concept_id", "")
        if cid and cid not in concepts:
            errors.append(f"BUILD_TABLES: {r['table']}.{r['column']} references unknown concept_id '{cid}'")
        axis = r.get("axis_id", "")
        if axis and axis not in axes:
            errors.append(f"BUILD_TABLES: {r['table']}.{r['column']} references unknown axis_id '{axis}'")
        member = r.get("axis_member", "")
        if member and member not in members:
            errors.append(
                f"BUILD_TABLES: {r['table']}.{r['column']} references unknown axis_member '{member}'"
            )

    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"{len(errors)} build_tables mapping violation(s)", file=sys.stderr)
        return 1
    total = len(rows)
    mapped = sum(1 for r in rows if r.get("concept_id"))
    print(f"  build_tables mapping: {mapped}/{total} = {mapped / total:.0%}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
