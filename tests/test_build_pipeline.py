"""Tests for the build pipeline."""

from __future__ import annotations

from pathlib import Path

import pyarrow.parquet as pq
import pytest

from build.build_parquet import build_all
from build.parse_concepts import REPO_ROOT, load_axes, load_concepts
from build.validate_jsonschema import validate_axes as v_axes
from build.validate_jsonschema import validate_concepts as v_concepts
from build.validate_referential import _violations


def test_jsonschema_clean():
    assert v_concepts() == [], "concept JSON-Schema violations"
    assert v_axes() == [], "axis JSON-Schema violations"


def test_referential_clean():
    assert _violations() == [], "referential violations"


def test_parquet_builds(tmp_path: Path):
    counts = build_all(tmp_path)
    assert counts["concepts"] > 0
    assert counts["labels"] >= counts["concepts"] * 2
    assert counts["axes"] >= 4
    assert (tmp_path / "concepts.parquet").exists()
    table = pq.read_table(tmp_path / "concepts.parquet")
    assert "concept_id" in table.column_names


def test_concept_id_unique():
    seen: set[str] = set()
    for c in load_concepts():
        cid = c.front_matter["concept_id"]
        assert cid not in seen, f"duplicate concept_id: {cid}"
        seen.add(cid)


def test_axis_id_unique():
    seen: set[str] = set()
    for a in load_axes():
        aid = a.front_matter["axis_id"]
        assert aid not in seen, f"duplicate axis_id: {aid}"
        seen.add(aid)


def test_calc_arcs_have_valid_weights():
    for c in load_concepts():
        for arc in c.front_matter.get("parents") or []:
            assert arc["weight"] in (-1, 1, -1.0, 1.0), f"bad weight in {c.path}: {arc['weight']}"


def test_monetary_concepts_have_balance():
    for c in load_concepts():
        fm = c.front_matter
        if fm["data_type"] == "monetaryItemType":
            assert fm.get("balance") in ("debit", "credit"), (
                f"{c.path}: monetary concept missing balance"
            )


def test_every_concept_has_norwegian_label():
    for c in load_concepts():
        labs = c.front_matter.get("labels") or []
        nb_std = [l for l in labs if l["lang"] == "nb" and l["role"] == "standardLabel"]
        assert len(nb_std) >= 1, f"{c.path}: missing Norwegian standardLabel"


def test_every_concept_has_english_label():
    for c in load_concepts():
        labs = c.front_matter.get("labels") or []
        en_std = [l for l in labs if l["lang"] == "en" and l["role"] == "standardLabel"]
        assert len(en_std) >= 1, f"{c.path}: missing English standardLabel"


def test_axes_have_members():
    for a in load_axes():
        assert len(a.front_matter.get("members") or []) > 0, f"{a.path}: axis has no members"


def test_no_concept_references_unknown_axis():
    axis_ids = {a.front_matter["axis_id"] for a in load_axes()}
    for c in load_concepts():
        for use in c.front_matter.get("axes") or []:
            assert use["axis"] in axis_ids, f"{c.path}: unknown axis {use['axis']}"


@pytest.mark.parametrize(
    "expected_root_concept",
    [
        "regnskap-no:Salgsinntekt",
        "regnskap-no:Lonnskostnad",
        "regnskap-no:Eiendeler",
        "regnskap-no:Egenkapital",
        "regnskap-no:Gjeld",
    ],
)
def test_root_concepts_present(expected_root_concept):
    cids = {c.front_matter["concept_id"] for c in load_concepts()}
    assert expected_root_concept in cids
