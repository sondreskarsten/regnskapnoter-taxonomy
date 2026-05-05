# Consumer Guide

This guide explains how downstream pipelines pin to and consume regnskapnoter-taxonomy.

## Pinning

Always pin to a specific version. Use the major version for compatibility, the minor version for new concepts you've adopted, and the patch version for bug fixes.

```python
TAXONOMY_VERSION = "1.0.0"
TAXONOMY_GCS_PREFIX = f"gs://regnskapnoter-taxonomy/v{TAXONOMY_VERSION}/"
```

Never pin to `latest/` in production. The `latest/` prefix exists only for inspection and ad-hoc queries.

## Loading from GCS

```python
import pyarrow.parquet as pq
from google.cloud import storage

client = storage.Client()
bucket = client.bucket("regnskapnoter-taxonomy")

def load_artifact(name: str, version: str) -> pq.Table:
    blob = bucket.blob(f"v{version}/{name}.parquet")
    blob.download_to_filename(f"/tmp/{name}.parquet")
    return pq.read_table(f"/tmp/{name}.parquet")

concepts = load_artifact("concepts", "1.0.0")
calc_arcs = load_artifact("calc_arcs", "1.0.0")
references = load_artifact("references", "1.0.0")
mappings = load_artifact("mappings", "1.0.0")
```

## Querying with DuckDB

DuckDB reads Parquet directly:

```python
import duckdb

con = duckdb.connect()
con.execute(f"CREATE VIEW concepts AS SELECT * FROM read_parquet('{TAXONOMY_GCS_PREFIX}concepts.parquet')")
con.execute(f"CREATE VIEW references AS SELECT * FROM read_parquet('{TAXONOMY_GCS_PREFIX}references.parquet')")

# Find all concepts derived from regnskapsloven § 7-38
result = con.execute("""
    SELECT c.concept_id, c.data_type, c.balance, l.text AS label_nb
    FROM concepts c
    JOIN references r ON c.concept_id = r.subject_id
    LEFT JOIN read_parquet('artifacts/labels.parquet') l
        ON l.subject_id = c.concept_id AND l.lang = 'nb' AND l.role = 'standardLabel'
    WHERE r.publisher = 'Stortinget'
      AND r.document = 'regnskapsloven'
      AND r.paragraph LIKE '§ 7-38%'
""").fetchall()
```

## Annotation Output Schema

When emitting `annotations.parquet`, conform to the schema in §5.1 of the implementation plan.
The minimum required fields:

```python
ANNOTATION_SCHEMA = {
    "annotation_id": str,         # UUIDv4
    "orgnr": str,                 # 9-digit
    "fiscal_year": int,
    "body_concept_id": str,       # must exist in concepts.parquet
    "body_value": "decimal(38,2)",
    "body_unit": str,             # NOK | EUR | shares | pure
    "body_period_type": str,      # instant | duration
    "body_period_start": "date",
    "body_period_end": "date",
    "target_source_uri": str,
    "target_source_sha256": str,
    "selector_type": str,
    "selector_exact": str,
    "selector_page": int,
    "motivation": str,            # tagging
    "creator": str,               # pipeline name + version
    "created": "timestamp",
    "taxonomy_version": str,      # "1.0.0"
    "confidence": float,
    "provenance_source": str,
}
```

## Validating Annotations Against the Taxonomy

Every `body_concept_id` must exist in `concepts.parquet`. CI in your consumer pipeline should enforce this:

```python
def validate_annotations(annotations: pq.Table, concepts: pq.Table) -> list[str]:
    valid_ids = set(concepts["concept_id"].to_pylist())
    bad = [
        cid for cid in annotations["body_concept_id"].to_pylist()
        if cid not in valid_ids
    ]
    return bad
```

## Migration Across Major Versions

When the taxonomy releases a major version (e.g., v2.0.0), check `mappings.parquet` for `dct:isReplacedBy`-style entries:

```sql
SELECT subject_id AS old_concept, target AS new_concept
FROM read_parquet('gs://regnskapnoter-taxonomy/v2.0.0/mappings.parquet')
WHERE relation = 'skos:exactMatch'
  AND quality = 'exact'
  AND note LIKE 'replaces v1%'
```

Apply these substitutions to your historical annotation set before re-validating.

## Recommended Consumers

- `noter-text-extraction`: emits annotations from PDF source text.
- `noter-canonicalizer`: reconciles annotations from multiple sources (nokkeltall, tesseract, gemini extraction) into a single fact-grain output keyed on (orgnr, fiscal_year, concept_id).
- `firm-deterioration`: feature engineering reads annotations grouped by concept_id and time-evolution.
