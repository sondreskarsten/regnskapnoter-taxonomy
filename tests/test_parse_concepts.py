from pathlib import Path

from build.parse_concepts import load_all, load_concepts, load_axes, parse_markdown_file

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_load_all_returns_parse_result():
    result = load_all()
    assert hasattr(result, "concepts")
    assert hasattr(result, "axes")
    assert hasattr(result, "references")


def test_seed_concept_loads():
    concepts = load_concepts()
    cids = {c.front_matter["concept_id"] for c in concepts}
    assert "regnskap-no:Resultatregnskap" in cids


def test_references_present():
    result = load_all()
    assert "nrs-standards" in result.references
    assert "regnskapsloven-paragraphs" in result.references
    assert "forskrift-paragraphs" in result.references


def test_parse_markdown_rejects_missing_front_matter(tmp_path: Path):
    bad = tmp_path / "no_fm.md"
    bad.write_text("# Hello\n\nNo front matter here.\n", encoding="utf-8")
    try:
        parse_markdown_file(bad)
    except ValueError as e:
        assert "front-matter" in str(e)
        return
    raise AssertionError("expected ValueError")
