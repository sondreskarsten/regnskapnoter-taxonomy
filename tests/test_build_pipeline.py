import os
from pathlib import Path

import pyarrow.parquet as pq

from build import build_parquet, build_turtle, check_parquet_rdf_parity, validate_jsonschema, validate_referential, validate_shacl

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_jsonschema_validation_passes():
    assert validate_jsonschema.main() == 0


def test_referential_validation_passes():
    assert validate_referential.main() == 0


def test_parquet_build(tmp_path: Path):
    counts = build_parquet.build_all(tmp_path)
    assert counts["concepts"] >= 1
    assert (tmp_path / "concepts.parquet").exists()
    assert (tmp_path / "labels.parquet").exists()
    assert (tmp_path / "axes.parquet").exists()


def test_concept_parquet_schema(tmp_path: Path):
    build_parquet.build_all(tmp_path)
    table = pq.read_table(tmp_path / "concepts.parquet")
    fields = {f.name for f in table.schema}
    assert "concept_id" in fields
    assert "period_type" in fields
    assert "balance" in fields
    assert "data_type" in fields
    assert "status" in fields


def test_turtle_build(tmp_path: Path):
    g = build_turtle.build_graph("test")
    g.serialize(destination=str(tmp_path / "taxonomy.ttl"), format="turtle")
    assert (tmp_path / "taxonomy.ttl").exists()
    assert len(g) > 0


def test_full_pipeline_with_seed(tmp_path: Path):
    os.environ["RNT_OUT_DIR"] = str(tmp_path)
    counts = build_parquet.build_all(tmp_path)
    assert counts["concepts"] >= 1
    g = build_turtle.build_graph("test")
    g.serialize(destination=str(tmp_path / "taxonomy.ttl"), format="turtle")
    g.serialize(destination=str(tmp_path / "taxonomy.jsonld"), format="json-ld", indent=2)
    import sys
    saved = sys.argv
    sys.argv = ["validate_shacl", "--out-dir", str(tmp_path)]
    try:
        assert validate_shacl.main() == 0
    finally:
        sys.argv = saved
    sys.argv = ["check_parity", "--out-dir", str(tmp_path)]
    try:
        assert check_parquet_rdf_parity.main() == 0
    finally:
        sys.argv = saved
