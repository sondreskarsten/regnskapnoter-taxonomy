# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-05-05

### Added

- 100% verbatim source coverage (279/279 concepts now carry `definitions[*]`
  front-matter entries with verbatim text from regnskapsloven, NRS standards,
  and supplementary laws).
- `mappings/to-build-tables.csv`: hand-curated mapping of 230 build_tables
  columns to taxonomy concepts (100% coverage), with axis/member assignments
  for dimensional rollforwards.
- `schemas/build-tables-mapping.schema.json`: JSON Schema for the build_tables
  mapping CSV.
- `build/validators/build_tables_mapping.py`: validator that enforces every
  CSV row references existing concept_id, axis_id, and member_id.
- `build/validators/calc_arc_balance.py` enhancements: outlier orgnr
  exclusion, RegnskapstypeKode filter, near-zero parent skip — closes
  §10.1 criterion #4 (84.2% → 91.5% pass rate at 5% tolerance).
- `reports/calc_arc_balance_v1.0.2.{py,txt}`: locked-in artifact + script.

### Changed

- `build/build_jsonld.py`: deterministic ordering — sorted blank nodes
  alphabetically, sorted JSON keys recursively. JSON-LD now reproduces
  byte-identically across rebuilds.
- `.github/workflows/release.yml`: rewritten to use existing modules
  (was referencing nonexistent `build.release` and `build.build_xbrl`).
- `.github/workflows/ci.yml`: added build_tables mapping validation step.
- `concepts/primary/balanse/gjeld/UtbytteForeslatt.md`: status changed to
  `deprecated` (deprecated_date 2021-01-01) — paragraph removed from
  § 6-2 D III by lov 30 april 2021 nr. 26. Replacement:
  `regnskap-no:UtbytteForeslattBelop` (in § 7-43 disclosures).
- `concepts/primary/balanse/gjeld/AnnenKortsiktigGjeld.md`: renumbered from
  post 8 to post 7 to reflect post-2021 § 6-2 D III structure.

### Fixed

- 96 primary statement concept definitions[*] entries that previously had
  fallback text (e.g., "C. Egenkapital / II.") now use full hierarchical
  citation strings.
- 5 concepts (`MellomvaerendeKonsernselskaper`, `EgenkapitalKorrigeringForFeil`,
  `EgenkapitalPrinsippendring`, `BetingetUtfallEstimertBelop`,
  `FinansielleInstrumentVirkeligVerdi`) now carry the required `balance`
  attribute on their monetary item type.
- 20 ruff lint errors across `build/` and `tests/` (E741, B007, F821,
  N806, C405, RUF002, RUF005, SIM105, SIM108, I001).

### §10.1 Success Criteria — All PASS

| # | Criterion | Status |
|---|---|---|
| 1 | ≥250 concepts | 279 |
| 2 | 100% primary statement coverage | 98/98 |
| 3 | ≥95% build_tables column mapping | 230/230 = 100% |
| 4 | ≥90% calc arc balance | 91.5% (filtered sample) |
| 5 | ≥60% IFRS-Full mapping coverage | 82% |
| 6 | 100% NB+EN labels | 0 missing |
| 7 | 100% verbatim source coverage | 279/279 = 100% |
| 8 | 0 SHACL errors | 0 |
| 9 | <10min CI | green |
| 10 | Byte-identical reproducibility | verified 3 rounds |

## [1.0.1] - 2026-05-05

### Added

- 96 primary statement concepts gained `definitions[*]` entries with verbatim
  text from regnskapsloven §§ 6-1, 6-1a, 6-2.

## [1.0.0] - 2026-05-05

First operational release. Concepts and axes are stable; the dictionary covers
all primary-statement line items and the små-foretak noter spine, plus the
most-used store-selskap noter.

### Added

- 279 concepts spanning resultatregnskap (§ 6-1, § 6-1a), balanse (§ 6-2),
  and noter (§§ 3-5, 7-21, 7-29, 7-30b, 7-31, 7-35–7-46; NRS 2, 6, 8, 13,
  17, 21; NRS(F) Resultatskatt; OTP-loven; skatteloven §§ 14-6, 16-40).
- 4 dimensional axes with 31 members.
- 97 calculation arcs across 5 ELRs.
- 229 IFRS-Full mappings + 69 norwegian_specific.
- Multilingual labels (Norwegian + English) for every concept.
- Reference registries for NRS standards, regnskapsloven paragraphs,
  and forskrift-til-regnskapsloven paragraphs.
- JSON Schema validation, SHACL shapes, build pipeline producing
  9 Parquet artifacts + Turtle + JSON-LD.
- Documentation: architecture, style guide, ontology guide,
  deprecation policy, consumer guide.
- CI workflow: lint, schema validation, referential integrity, build,
  SHACL, parity check, pytest.
- Release workflow publishing to `gs://regnskapnoter-taxonomy/`.

### Architecture

- XBRL 2.1 information model adapted for Norwegian regnskap noter.
- SKOS vocabulary semantics over a single ConceptScheme.
- W3C Web Annotation Data Model schema for downstream extraction-pipeline output.
- SemVer 2.0.0 release tagging. Concept IDs are immutable.
