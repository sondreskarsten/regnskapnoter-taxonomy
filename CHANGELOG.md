# Changelog

All notable changes to this project are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [1.0.3] - 2026-05-05

### Added
- **Dublin Core release metadata** in published RDF: `dct:creator`, `dct:publisher`, `dct:rightsHolder`, `dct:language`, `dct:modified`, `dct:conformsTo`, `dct:bibliographicCitation`, `dct:description`.
- **DCAT 2.0 catalog/dataset/distribution** triples in Turtle and JSON-LD describing the published artifacts (turtle, jsonld, parquet).
- **Dated IRIs**: every concept now also has a versioned IRI (`https://regnskapnoter-taxonomy/regnskap-no/v{X.Y.Z}/{Local}`) with `owl:sameAs` and `dct:isVersionOf` links to the stable IRI.
- **`owl:versionIRI`** on the SKOS Concept Scheme.
- **arelle XBRL validation** wired into CI via `build/validate_xbrl.py`. Validates the `xbrl/regnskap-no.xsd` package and label/calculation linkbases.
- **WADM annotation producer scaffold** at `build/annotations/emit_annotations.py`. Reads per-document extraction JSON, emits `annotations.parquet` with W3C Web Annotation Data Model fields (annotation_id, target_iri, text_quote, text_position, media_fragment, motivation).
- **`docs/skosmos-deploy.md`**: deployment guide for Skosmos publication site.
- **`docs/annotation-ui-deploy.md`**: deployment guide for Hypothes.is and INCEpTION.
- **`VERSION` and `RELEASE_DATE` files** as deterministic single-source-of-truth for version and date strings (used in DC/DCAT triples; preserves byte-identical reproducibility).
- **`.github/workflows/ci.yml` pre-commit step**: runs all pre-commit hooks against all files on every PR.

### Fixed
- XBRL XSD: `xmlns:xbrldt`, `xmlns:link`, `xmlns:xlink`, `xmlns:regnskap-no` now declared on root `<schema>` element (arelle conformance fix).
- XBRL XSD: replaced `us-types:textBlockItemType` and `num:percentItemType` with native `xbrli:stringItemType` / `xbrli:pureItemType` (no external schema imports needed).
- `pyproject.toml`: per-file ruff ignores for `reports/*` (snapshots) and `build/build_xbrl.py` (N817 ET acronym).

### Validation status (§10 tech stack + §6/§7 validation layers)
All §10.1 success criteria PASS. Standards compliance: SKOS, XBRL 2.1, XBRL Dimensions, SHACL, JSON Schema 2020-12, Dublin Core, DCAT 2.0, dated IRIs, SemVer 2.0.0, WADM (schema + producer scaffold).

## [1.0.2] - 2026-05-05

### Added
- 100% mapping (230/230) from build_tables CSV column names to regnskap-no concept_ids.
- Calc arc balance validator improvements: outlier orgnr exclusion, RegnskapstypeKode='R' filter, skip near-zero parents.
- Cross-references for § 7-44 (Opphevet 2021) concepts: 10 concepts now cite NRS 17 / NRS(F) Investering i tilknyttet selskap as primary, retain § 7-44 with applicable_to_fiscal_year=2020.
- `build/validators/build_tables_mapping.py` validator (closes CI gap).

### Fixed
- JSON-LD serialization deterministic (sorted keys + sorted lists) — byte-identical reproducibility for all 11 artifacts.
- `release.yml` rewritten to use existing modules.
- Ruff lint: 20 errors → 0.
- § 6-2 D III post numbering: `UtbytteForeslatt` deprecated post-2021, `AnnenKortsiktigGjeld` renumbered post 8 → 7.
- § 6-2 C/D verbatim parser refined: 42 concepts updated with hierarchical text.

## [1.0.1] - 2026-05-05

### Added
- 96 verbatim regnskapsloven definitions[*] entries on primary statement concepts.

## [1.0.0] - 2026-05-05

First operational release. 279 concepts, 4 axes, 31 members, 97 calc arcs.
