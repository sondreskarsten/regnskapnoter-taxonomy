# Consumer Guide

## Pinning a Version

Downstream pipelines pin to a specific taxonomy version. The version is published to:

- `gs://regnskapnoter-taxonomy/v<X.Y.Z>/` (immutable per release)
- `gs://regnskapnoter-taxonomy/latest/` (always points to the most recent release)

Pin to `v<X.Y.Z>` in production; never pin to `latest/`.

## Loading the Dictionary

```python
import duckdb
conn = duckdb.connect()
conn.execute("CREATE VIEW concepts AS SELECT * FROM 'gs://regnskapnoter-taxonomy/v1.0.0/concepts.parquet'")
conn.execute("CREATE VIEW labels AS SELECT * FROM 'gs://regnskapnoter-taxonomy/v1.0.0/labels.parquet'")
conn.execute("CREATE VIEW references AS SELECT * FROM 'gs://regnskapnoter-taxonomy/v1.0.0/references.parquet'")
```

## Common Query Patterns

### Look up all concepts derived from a regnskapsloven paragraph

```sql
SELECT c.concept_id, l.text AS label_nb
FROM concepts c
JOIN labels l USING (concept_id)
JOIN references r ON r.subject_id = c.concept_id AND r.subject_kind = 'concept'
WHERE r.publisher = 'Stortinget'
  AND r.document = 'regnskapsloven'
  AND r.paragraph LIKE '§ 7-38%'
  AND l.lang = 'nb' AND l.role = 'standardLabel'
```

### Get IFRS-Full equivalent for a regnskap-no concept

```sql
SELECT subject_id AS regnskap_no, target AS ifrs_full, relation, quality, note
FROM mappings
WHERE subject_id = 'regnskap-no:Lonnskostnad'
  AND target LIKE 'ifrs-full:%'
```

### Walk calculation arcs to compute a parent's expected sum

```sql
SELECT child_id, weight, "order"
FROM calc_arcs
WHERE parent_id = 'regnskap-no:SumDriftsinntekter'
  AND role = '[610000] Resultatregnskap etter art'
ORDER BY "order"
```

## Annotation Layer

Annotations from extraction pipelines conform to the W3C Web Annotation Data Model and are emitted as Parquet partitioned by `(fiscal_year, orgnr)`. Schema:

| Column | Type | Notes |
|---|---|---|
| annotation_id | string | UUIDv4 |
| orgnr | string | filing identifier |
| fiscal_year | int | period anchor |
| body_concept_id | string | reference to concepts.concept_id |
| body_value | decimal(38, 2) | fact value (monetary or pure) |
| body_unit | string | NOK, EUR, shares, pure |
| body_period_start | date | XBRL context start |
| body_period_end | date | XBRL context end |
| body_axis_members | list<struct> | dimensional context |
| target_source_uri | string | PDF URI |
| selector_type | string | `TextQuoteSelector` etc. |
| selector_exact, selector_prefix, selector_suffix | string | WADM TextQuoteSelector |
| selector_page | int | PDF page number |
| selector_xywh | struct | Media Fragments bbox |
| motivation | string | `tagging` |
| creator | string | pipeline name + version |
| created | timestamp | event time |
| taxonomy_version | string | regnskapnoter-taxonomy SemVer |
| confidence | float | extraction confidence 0-1 |
| provenance_source | string | extraction tool identifier |
