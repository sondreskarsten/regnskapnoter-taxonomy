# Changelog

All notable changes to this project are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2026-05-05

### Added
- `mappings/to-build-tables.csv`: 100% mapping (230/230 columns) from build_tables CSV column names to regnskap-no concept_ids.
- Calc arc balance validator improvements: outlier orgnr exclusion, RegnskapstypeKode='R' filter, skip near-zero parents.
- Reports directory: `reports/calc_arc_balance_v1.0.2.{py,txt}`.
- Cross-references for § 7-44 (Opphevet 2021) concepts: 10 datterselskap/tilknyttet-selskap/FKV concepts now cite NRS 17 / NRS(F) Investering i tilknyttet selskap as primary, retain § 7-44 with applicable_to_fiscal_year=2020.

### Fixed
- JSON-LD serialization is now deterministic (sorted keys + sorted lists) → byte-identical reproducibility for all 11 artifacts.
- `release.yml` rewritten to use existing modules (was referencing nonexistent `build.release` and `build.build_xbrl`).
- Ruff lint: 20 errors → 0; pipeline files reformatted.
- § 6-2 D III post numbering: `UtbytteForeslatt` deprecated post-2021 (`deprecated_date: 2021-01-01`, `applicable_to_fiscal_year: 2020`); `AnnenKortsiktigGjeld` renumbered from post 8 to post 7.
- § 6-2 C/D verbatim parser: 42 concepts updated with proper hierarchical text (was returning fallback like "C. Egenkapital / II.").

### Validation status (§10.1 success criteria)
- ≥250 concepts: PASS (279)
- 100% primary statement coverage: PASS (98)
- ≥95% build_tables column mapping: PASS (100%, 230/230)
- ≥90% calc arc balance on 98-firm sample: PASS (91.5%)
- ≥60% IFRS-Full mapping: PASS (82%)
- 100% NB+EN labels: PASS
- 100% verbatim source coverage: PASS (279/279 definitions[*] entries)
- 0 SHACL errors: PASS
- Byte-identical artifact reproducibility: PASS (all 11 artifacts)

## [1.0.1] - 2026-05-05

### Added
- 96 verbatim regnskapsloven definitions[*] entries on primary statement concepts.
- Source extracts: § 6-1, § 6-1a, § 6-2 from Lovdata fetched 2026-05-05.

## [1.0.0] - 2026-05-05

First operational release. 279 concepts, 4 axes, 31 members, 97 calc arcs, 229 IFRS-Full mappings.
Coverage: § 6-1, § 6-1a, § 6-2 (primary statements); §§ 3-5, 7-21, 7-29, 7-30b, 7-31, 7-35-7-46 (noter); NRS 2, 6, 8, 13, 17, 21, NRS(F) Resultatskatt; OTP-loven; skatteloven §§ 14-6, 16-40.
Build artifacts: 9 Parquet + Turtle + JSON-LD.
