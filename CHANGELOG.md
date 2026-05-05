# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-05-05

First operational release. Concepts and axes are stable; the dictionary covers all
primary-statement line items and the små-foretak noter spine, plus the most-used
store-selskap noter (skatt, pensjon, bankinnskudd, anleggskontrakter, related parties,
contingent liabilities, SkatteFUNN).

### Added

- 279 concepts spanning resultatregnskap (§ 6-1 etter art, § 6-1a etter funksjon),
  balanse (§ 6-2), and noter (§§ 3-5, 7-21, 7-29, 7-30b, 7-31, 7-35 through 7-46;
  NRS 2, NRS 6, NRS 8, NRS 13, NRS 17, NRS 21, NRS(F) Resultatskatt; OTP-loven;
  skatteloven § 16-40).
- 4 dimensional axes (EgenkapitalKomponent, EgenkapitalEndring,
  KlassifiseringAvAnleggsmidler, AnleggsmidlerEndring) with 31 members.
- 97 calculation arcs across 5 Extended Link Roles (resultatregnskap etter art,
  resultatregnskap etter funksjon, balanse, note 7-38 lønnskostnader, note ELRs).
- 229 IFRS-Full mappings (skos:exactMatch, closeMatch, broadMatch, narrowMatch).
- 69 concepts marked `norwegian_specific` (no IFRS-Full equivalent).
- Multilingual labels (Norwegian + English) for every concept.
- Reference registries for NRS standards, regnskapsloven paragraphs, and
  forskrift-til-regnskapsloven paragraphs, with full version applicability windows.
- JSON Schema validation for concept and axis front-matter.
- SHACL shapes for RDF projection.
- Build pipeline producing 9 Parquet artifacts (concepts, labels, definitions,
  references, mappings, calc_arcs, axes, axis_members, concept_hypercube),
  Turtle (3877 triples), and JSON-LD.
- Documentation: architecture, style guide, ontology guide, deprecation policy,
  consumer guide.
- CI workflow: lint, schema validation, referential integrity, build, SHACL,
  parity check, pytest.
- Release workflow publishing to `gs://regnskapnoter-taxonomy/v<X.Y.Z>/` and
  `gs://regnskapnoter-taxonomy/latest/`.

### Architecture

- XBRL 2.1 information model adapted for Norwegian regnskap noter.
- SKOS vocabulary semantics over a single ConceptScheme.
- W3C Web Annotation Data Model schema for downstream extraction-pipeline output.
- SemVer 2.0.0 release tagging. Concept IDs are immutable; renames are forbidden.
