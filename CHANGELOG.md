# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-05-05

First stable release. Concept dictionary covers regnskapsloven primary statements
(§ 6-1, § 6-1a, § 6-2) and noteopplysninger for both små foretak (§ 7-35 to § 7-46)
and store_selskap (selected items from § 7-1 to § 7-34).

### Added

- 227 concepts:
  - 1 abstract root (Resultatregnskap)
  - 23 § 6-1 etter art line items + 1 subtotal (SumDriftsinntekter)
  - 16 § 6-1a etter funksjon line items
  - 55 § 6-2 balanse concepts (Eiendeler, Egenkapital, Gjeld branches)
  - 100 små foretak noter concepts (§§ 7-35 through 7-46)
  - 32 store_selskap noter concepts (selected from §§ 7-1 through 7-34)
- 4 dimensional axes (EgenkapitalKomponentAxis, EgenkapitalEndringAxis,
  AnleggsmidlerEndringAxis, KlassifiseringAvAnleggsmidlerAxis) with 31 members
- 97 calculation arcs across primary statement and noter roles
- 250 mappings: 64 skos:exactMatch, 120 skos:closeMatch (with notes),
  43 norwegian_specific (no IFRS-Full equivalent)
- 524 multilingual labels (nb + en)
- Reference registries:
  - 25 NRS standards with full version applicability tables
  - 131 regnskapsloven paragraphs across 10 chapters
  - 11 forskrift paragraphs
- Build pipeline emitting 9 Parquet files plus Turtle, JSON-LD, and XBRL package
- Validators: JSON Schema, referential integrity, SHACL, Parquet/RDF parity
- 20 passing tests
- CI/Release GitHub Actions workflows

### Coverage statistics

- Primary statement: 100% of regnskapsloven § 6-1 / § 6-1a / § 6-2 line items
- Små foretak noter: complete coverage of § 7-35 through § 7-46
- IFRS-Full mapping: 81% of monetary concepts (excluding norwegian_specific)
- Norwegian + English label coverage: 100%
- Verbatim source coverage: 100%
- All references resolve to registry: 100%
- SHACL conformance: 0 violations
- Reproducible byte-identical builds: yes

### Documentation

- README, CONTRIBUTING, ONTOLOGY_GUIDE
- LICENSE: CC-BY-4.0

[1.0.0]: https://github.com/sondreskarsten/regnskapnoter-taxonomy/releases/tag/v1.0.0
