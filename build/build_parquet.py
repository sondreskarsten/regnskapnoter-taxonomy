"""Emit nine Parquet artifacts from concept and axis Markdown sources.

Output schema (Apache Arrow):

* ``concepts.parquet`` — one row per concept.
* ``labels.parquet`` — one row per (concept, lang, role).
* ``definitions.parquet`` — one row per (concept, lang, role, source).
* ``references.parquet`` — one row per (concept, source citation).
* ``mappings.parquet`` — one row per (concept, target_concept).
* ``calc_arcs.parquet`` — one row per (role, parent, child).
* ``axes.parquet`` — one row per axis.
* ``axis_members.parquet`` — one row per (axis, member).
* ``concept_hypercube.parquet`` — one row per (concept, axis).

Snappy compression, schema validated against pyarrow Schemas declared inline.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any

import pyarrow as pa
import pyarrow.parquet as pq

from build.parse_concepts import REPO_ROOT, load_axes, load_concepts


def _str(value: Any) -> str | None:
    if value is None:
        return None
    return str(value)


def _build_concepts(concepts: list[Any]) -> pa.Table:
    rows: list[dict[str, Any]] = []
    for c in concepts:
        fm = c.front_matter
        rows.append(
            {
                "concept_id": fm["concept_id"],
                "namespace": fm["namespace"],
                "period_type": fm["period_type"],
                "balance": fm.get("balance"),
                "data_type": fm["data_type"],
                "substitution_group": fm["substitution_group"],
                "abstract": bool(fm["abstract"]),
                "status": fm["status"],
                "introduced_version": fm["introduced_version"],
                "deprecated_date": _str(fm.get("deprecated_date")),
                "deprecated_replacement": fm.get("deprecated_replacement"),
                "source_path": str(c.path.relative_to(REPO_ROOT)),
            }
        )
    schema = pa.schema(
        [
            pa.field("concept_id", pa.string(), nullable=False),
            pa.field("namespace", pa.string(), nullable=False),
            pa.field("period_type", pa.string(), nullable=False),
            pa.field("balance", pa.string(), nullable=True),
            pa.field("data_type", pa.string(), nullable=False),
            pa.field("substitution_group", pa.string(), nullable=False),
            pa.field("abstract", pa.bool_(), nullable=False),
            pa.field("status", pa.string(), nullable=False),
            pa.field("introduced_version", pa.string(), nullable=False),
            pa.field("deprecated_date", pa.string(), nullable=True),
            pa.field("deprecated_replacement", pa.string(), nullable=True),
            pa.field("source_path", pa.string(), nullable=False),
        ]
    )
    return pa.Table.from_pylist(rows, schema=schema)


def _build_labels(concepts: list[Any], axes: list[Any]) -> pa.Table:
    rows: list[dict[str, Any]] = []
    for c in concepts:
        cid = c.front_matter["concept_id"]
        for lab in c.front_matter.get("labels") or []:
            rows.append(
                {
                    "subject_id": cid,
                    "subject_kind": "concept",
                    "lang": lab["lang"],
                    "role": lab["role"],
                    "text": lab["text"],
                }
            )
    for a in axes:
        aid = a.front_matter["axis_id"]
        for lab in a.front_matter.get("labels") or []:
            rows.append(
                {
                    "subject_id": aid,
                    "subject_kind": "axis",
                    "lang": lab["lang"],
                    "role": lab["role"],
                    "text": lab["text"],
                }
            )
        for member in a.front_matter.get("members") or []:
            mid = member["id"]
            for lab in member.get("labels") or []:
                rows.append(
                    {
                        "subject_id": mid,
                        "subject_kind": "member",
                        "lang": lab["lang"],
                        "role": lab["role"],
                        "text": lab["text"],
                    }
                )
    schema = pa.schema(
        [
            pa.field("subject_id", pa.string(), nullable=False),
            pa.field("subject_kind", pa.string(), nullable=False),
            pa.field("lang", pa.string(), nullable=False),
            pa.field("role", pa.string(), nullable=False),
            pa.field("text", pa.string(), nullable=False),
        ]
    )
    return pa.Table.from_pylist(rows, schema=schema)


def _build_definitions(concepts: list[Any]) -> pa.Table:
    rows: list[dict[str, Any]] = []
    for c in concepts:
        cid = c.front_matter["concept_id"]
        for d in c.front_matter.get("definitions") or []:
            rows.append(
                {
                    "concept_id": cid,
                    "lang": d["lang"],
                    "role": d["role"],
                    "text": d["text"],
                    "source_publisher": d["source_publisher"],
                    "source_document": d["source_document"],
                    "source_paragraph": d["source_paragraph"],
                    "source_version": d.get("source_version"),
                    "applicable_from_fiscal_year": d["applicable_from_fiscal_year"],
                    "applicable_to_fiscal_year": d.get("applicable_to_fiscal_year"),
                    "authoritative": bool(d["authoritative"]),
                }
            )
    schema = pa.schema(
        [
            pa.field("concept_id", pa.string(), nullable=False),
            pa.field("lang", pa.string(), nullable=False),
            pa.field("role", pa.string(), nullable=False),
            pa.field("text", pa.string(), nullable=False),
            pa.field("source_publisher", pa.string(), nullable=False),
            pa.field("source_document", pa.string(), nullable=False),
            pa.field("source_paragraph", pa.string(), nullable=False),
            pa.field("source_version", pa.string(), nullable=True),
            pa.field("applicable_from_fiscal_year", pa.int32(), nullable=False),
            pa.field("applicable_to_fiscal_year", pa.int32(), nullable=True),
            pa.field("authoritative", pa.bool_(), nullable=False),
        ]
    )
    return pa.Table.from_pylist(rows, schema=schema)


def _build_references(concepts: list[Any], axes: list[Any]) -> pa.Table:
    rows: list[dict[str, Any]] = []
    for c in concepts:
        cid = c.front_matter["concept_id"]
        for ref in c.front_matter.get("references") or []:
            rows.append(
                {
                    "subject_id": cid,
                    "subject_kind": "concept",
                    "publisher": ref["publisher"],
                    "document": ref["document"],
                    "paragraph": ref["paragraph"],
                    "version": ref.get("version"),
                    "applicable_from_fiscal_year": ref["applicable_from_fiscal_year"],
                    "applicable_to_fiscal_year": ref.get("applicable_to_fiscal_year"),
                    "note": ref.get("note"),
                }
            )
    for a in axes:
        for member in a.front_matter.get("members") or []:
            mid = member["id"]
            for ref in member.get("references") or []:
                rows.append(
                    {
                        "subject_id": mid,
                        "subject_kind": "member",
                        "publisher": ref["publisher"],
                        "document": ref["document"],
                        "paragraph": ref["paragraph"],
                        "version": ref.get("version"),
                        "applicable_from_fiscal_year": ref.get("applicable_from_fiscal_year") or 1900,
                        "applicable_to_fiscal_year": ref.get("applicable_to_fiscal_year"),
                        "note": ref.get("note"),
                    }
                )
    schema = pa.schema(
        [
            pa.field("subject_id", pa.string(), nullable=False),
            pa.field("subject_kind", pa.string(), nullable=False),
            pa.field("publisher", pa.string(), nullable=False),
            pa.field("document", pa.string(), nullable=False),
            pa.field("paragraph", pa.string(), nullable=False),
            pa.field("version", pa.string(), nullable=True),
            pa.field("applicable_from_fiscal_year", pa.int32(), nullable=False),
            pa.field("applicable_to_fiscal_year", pa.int32(), nullable=True),
            pa.field("note", pa.string(), nullable=True),
        ]
    )
    return pa.Table.from_pylist(rows, schema=schema)


def _build_mappings(concepts: list[Any], axes: list[Any]) -> pa.Table:
    rows: list[dict[str, Any]] = []
    for c in concepts:
        cid = c.front_matter["concept_id"]
        for m in c.front_matter.get("mappings") or []:
            rows.append(
                {
                    "subject_id": cid,
                    "subject_kind": "concept",
                    "target": m.get("to"),
                    "relation": m.get("relation"),
                    "quality": m.get("quality"),
                    "note": m.get("note"),
                }
            )
    for a in axes:
        aid = a.front_matter["axis_id"]
        for m in a.front_matter.get("mappings") or []:
            rows.append(
                {
                    "subject_id": aid,
                    "subject_kind": "axis",
                    "target": m.get("to"),
                    "relation": m.get("relation"),
                    "quality": m.get("quality"),
                    "note": m.get("note"),
                }
            )
        for member in a.front_matter.get("members") or []:
            mid = member["id"]
            mapping = member.get("mapping")
            if mapping:
                rows.append(
                    {
                        "subject_id": mid,
                        "subject_kind": "member",
                        "target": mapping.get("to"),
                        "relation": mapping.get("relation"),
                        "quality": mapping.get("quality"),
                        "note": mapping.get("note"),
                    }
                )
    schema = pa.schema(
        [
            pa.field("subject_id", pa.string(), nullable=False),
            pa.field("subject_kind", pa.string(), nullable=False),
            pa.field("target", pa.string(), nullable=True),
            pa.field("relation", pa.string(), nullable=True),
            pa.field("quality", pa.string(), nullable=True),
            pa.field("note", pa.string(), nullable=True),
        ]
    )
    return pa.Table.from_pylist(rows, schema=schema)


def _build_calc_arcs(concepts: list[Any]) -> pa.Table:
    rows: list[dict[str, Any]] = []
    for c in concepts:
        cid = c.front_matter["concept_id"]
        for parent_arc in c.front_matter.get("parents") or []:
            rows.append(
                {
                    "role": parent_arc["role"],
                    "parent_id": parent_arc["parent"],
                    "child_id": cid,
                    "weight": float(parent_arc["weight"]),
                    "order": parent_arc.get("order", 0),
                    "applicable_from_fiscal_year": parent_arc.get("applicable_from_fiscal_year"),
                    "applicable_to_fiscal_year": parent_arc.get("applicable_to_fiscal_year"),
                }
            )
    schema = pa.schema(
        [
            pa.field("role", pa.string(), nullable=False),
            pa.field("parent_id", pa.string(), nullable=False),
            pa.field("child_id", pa.string(), nullable=False),
            pa.field("weight", pa.float64(), nullable=False),
            pa.field("order", pa.int32(), nullable=False),
            pa.field("applicable_from_fiscal_year", pa.int32(), nullable=True),
            pa.field("applicable_to_fiscal_year", pa.int32(), nullable=True),
        ]
    )
    return pa.Table.from_pylist(rows, schema=schema)


def _build_axes(axes: list[Any]) -> pa.Table:
    rows: list[dict[str, Any]] = []
    for a in axes:
        fm = a.front_matter
        rows.append(
            {
                "axis_id": fm["axis_id"],
                "namespace": fm["namespace"],
                "axis_kind": fm["axis_kind"],
                "typed_datatype": fm.get("typed_datatype"),
                "default_member": fm.get("default_member"),
                "status": fm["status"],
                "introduced_version": fm["introduced_version"],
                "deprecated_date": _str(fm.get("deprecated_date")),
                "source_path": str(a.path.relative_to(REPO_ROOT)),
            }
        )
    schema = pa.schema(
        [
            pa.field("axis_id", pa.string(), nullable=False),
            pa.field("namespace", pa.string(), nullable=False),
            pa.field("axis_kind", pa.string(), nullable=False),
            pa.field("typed_datatype", pa.string(), nullable=True),
            pa.field("default_member", pa.string(), nullable=True),
            pa.field("status", pa.string(), nullable=False),
            pa.field("introduced_version", pa.string(), nullable=False),
            pa.field("deprecated_date", pa.string(), nullable=True),
            pa.field("source_path", pa.string(), nullable=False),
        ]
    )
    return pa.Table.from_pylist(rows, schema=schema)


def _build_axis_members(axes: list[Any]) -> pa.Table:
    rows: list[dict[str, Any]] = []
    for a in axes:
        aid = a.front_matter["axis_id"]
        for m in a.front_matter.get("members") or []:
            rows.append(
                {
                    "axis_id": aid,
                    "member_id": m["id"],
                    "parent_member_id": m.get("parent"),
                    "order": m.get("order", 0),
                    "usable": bool(m.get("usable", True)),
                    "status": m.get("status", "standard"),
                }
            )
    schema = pa.schema(
        [
            pa.field("axis_id", pa.string(), nullable=False),
            pa.field("member_id", pa.string(), nullable=False),
            pa.field("parent_member_id", pa.string(), nullable=True),
            pa.field("order", pa.int32(), nullable=False),
            pa.field("usable", pa.bool_(), nullable=False),
            pa.field("status", pa.string(), nullable=False),
        ]
    )
    return pa.Table.from_pylist(rows, schema=schema)


def _build_concept_hypercube(concepts: list[Any]) -> pa.Table:
    rows: list[dict[str, Any]] = []
    for c in concepts:
        cid = c.front_matter["concept_id"]
        for axis_use in c.front_matter.get("axes") or []:
            rows.append(
                {
                    "primary_item_id": cid,
                    "axis_id": axis_use["axis"],
                    "role": axis_use.get("role"),
                    "closed": bool(axis_use["closed"]),
                }
            )
    schema = pa.schema(
        [
            pa.field("primary_item_id", pa.string(), nullable=False),
            pa.field("axis_id", pa.string(), nullable=False),
            pa.field("role", pa.string(), nullable=True),
            pa.field("closed", pa.bool_(), nullable=False),
        ]
    )
    return pa.Table.from_pylist(rows, schema=schema)


def build_all(out_dir: Path) -> dict[str, int]:
    out_dir.mkdir(parents=True, exist_ok=True)
    concepts = load_concepts()
    axes = load_axes()

    artifacts: dict[str, pa.Table] = {
        "concepts": _build_concepts(concepts),
        "labels": _build_labels(concepts, axes),
        "definitions": _build_definitions(concepts),
        "references": _build_references(concepts, axes),
        "mappings": _build_mappings(concepts, axes),
        "calc_arcs": _build_calc_arcs(concepts),
        "axes": _build_axes(axes),
        "axis_members": _build_axis_members(axes),
        "concept_hypercube": _build_concept_hypercube(concepts),
    }

    counts: dict[str, int] = {}
    for name, table in artifacts.items():
        path = out_dir / f"{name}.parquet"
        pq.write_table(table, path, compression="snappy")
        counts[name] = table.num_rows
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Parquet artifacts.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path(os.environ.get("RNT_OUT_DIR") or REPO_ROOT / "artifacts"),
    )
    args = parser.parse_args()
    counts = build_all(args.out_dir)
    for name, n in sorted(counts.items()):
        print(f"  {name}.parquet  {n:>6d} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
