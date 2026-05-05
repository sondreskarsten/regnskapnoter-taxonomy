# Architecture

## Information Model

The taxonomy adopts the XBRL 2.1 information model adapted for Norwegian regnskap noter, with SKOS as the vocabulary semantics layer and W3C Web Annotation Data Model (WADM) for the annotation layer (lives in consumer pipelines, not here).

## Source-of-Truth Layer

Each concept and axis is one Markdown file with YAML front-matter and a Markdown body. The YAML carries structured metadata that drives all build artifacts; the body carries verbatim quotations from authoritative sources (regnskapsloven, forskriften, NRS standards) plus editorial scope notes.

This format gives:
- Git-diffable concept evolution.
- Machine-readable structured metadata.
- Human-readable verbatim source binding.
- Schema-validatable front-matter.

## Build Pipeline

```
concepts/*.md  ──┐
axes/*.md      ──┤
                 ├─→ parse_concepts ──→ in-memory dict
references/*.yaml ┘                      │
                                         ├─→ build_parquet  → concepts.parquet, labels.parquet, ...
                                         ├─→ build_turtle   → taxonomy.ttl
                                         ├─→ build_jsonld   → taxonomy.jsonld
                                         └─→ build_xbrl     → regnskap-no.xsd + linkbases
```

## Validation Layer

Three validation strata:

1. **JSON Schema** validates each `.md` file's YAML front-matter against `schemas/concept-frontmatter.schema.json` and `schemas/axis-frontmatter.schema.json`.
2. **Referential integrity** (custom Python in `build/validate_referential.py`) enforces cross-file invariants: parent concept IDs exist, axis member references resolve, NRS and regnskapsloven citations resolve to the registry.
3. **SHACL** (`schemas/shapes.ttl` + pyshacl) enforces graph-level constraints over the RDF projection: prefLabel uniqueness per language, scheme membership, periodType/balance/status enums, deprecation lifecycle invariants, calculation arc weights.

A fourth optional layer is **Arelle XBRL round-trip** validation; the build pipeline emits an XBRL package which Arelle can validate end-to-end.

A fifth layer is **Parquet/RDF parity**: the count of concepts, axes, members, and mapping triples must match between the Parquet and RDF distributions. This catches drift between formats, the most common source of consumer bugs.

## Distribution

Each release publishes:

- 9 Parquet artifacts (snappy, row-group 128 MB)
- `taxonomy.ttl` (SKOS Turtle)
- `taxonomy.jsonld` (JSON-LD with stable `@context`)
- `xbrl/regnskap-no-{version}.zip` (XBRL package per Taxonomy Packages 1.0)
- `release-manifest.json` (DCAT distribution catalog with SHA-256 checksums)

Artifacts go to `gs://regnskapnoter-taxonomy/v<X.Y.Z>/` and `gs://regnskapnoter-taxonomy/latest/`.

## SemVer

- Major: any concept_id removed, period_type/balance/data_type changed, or breaking schema change.
- Minor: new concepts, axes, mappings, labels, references.
- Patch: typo fixes, build script bug fixes that don't change artifact content.

## Deprecation

`candidate → standard → deprecated → retired`. Concept IDs are forever. A deprecated concept retains its ID and gets `deprecated_date` and (recommended) `deprecated_replacement`.
