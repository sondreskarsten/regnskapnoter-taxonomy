"""Tests for the parser."""

from pathlib import Path

from build.parse_concepts import load_all, load_axes, load_concepts, parse_markdown_file


def test_load_all_returns_parse_result():
    result = load_all()
    assert hasattr(result, "concepts")
    assert hasattr(result, "axes")
    assert hasattr(result, "references")


def test_concepts_loaded():
    concepts = load_concepts()
    assert len(concepts) > 0
    cids = {c.front_matter["concept_id"] for c in concepts}
    assert "regnskap-no:Salgsinntekt" in cids


def test_references_present():
    result = load_all()
    assert "nrs-standards" in result.references
    assert "regnskapsloven-paragraphs" in result.references


def test_parse_markdown_rejects_missing_front_matter(tmp_path: Path):
    bad = tmp_path / "no_fm.md"
    bad.write_text("# Hello\n\nNo front matter here.\n", encoding="utf-8")
    try:
        parse_markdown_file(bad)
    except ValueError as e:
        assert "front-matter" in str(e)
        return
    raise AssertionError("expected ValueError")


def test_axes_loaded():
    axes = load_axes()
    assert len(axes) >= 4
    aids = {a.front_matter["axis_id"] for a in axes}
    assert "regnskap-no:EgenkapitalKomponentAxis" in aids
