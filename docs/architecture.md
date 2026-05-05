# Architecture

The regnskapnoter-taxonomy adopts conventions from XBRL 2.1, SKOS, and the W3C Web Annotation Data Model. See the literature review in the project root for the full justification.

## Information Model

- Concept attributes per XBRL 2.1: `period_type` (instant/duration), `balance` (debit/credit), `data_type`, `substitution_group`, `abstract`.
- Multilingual labels per IFRS Foundation taxonomy convention: standardLabel, terseLabel, documentationLabel, totalLabel, periodStartLabel, periodEndLabel, negatedLabel, deprecatedLabel.
- Calculation arcs per XBRL 2.1: parent + child + weight (+1 / -1) + role.
- Dimensional structure per XBRL Dimensions 1.0: hypercubes, axes, members, default member.
- References per XBRL reference linkbase: publisher, document, paragraph, version, applicability window.
- Mappings per SKOS: exactMatch, closeMatch, broadMatch, narrowMatch, relatedMatch.

## Source of Truth

Markdown files with YAML front-matter under `concepts/` and `axes/`. The YAML carries structured metadata; the body carries verbatim quotations from authoritative sources.

## Build Artifacts

CI generates nine Parquet files (concepts, labels, definitions, references, mappings, calc_arcs, axes, axis_members, concept_hypercube), plus Turtle (SKOS view) and JSON-LD. All artifacts validated via JSON Schema (front-matter), referential integrity (cross-file), SHACL (RDF graph), and parity checks (Parquet ↔ RDF).

## Annotation Layer

Downstream pipelines emit `(note_text, value) → concept` annotations conforming to the W3C Web Annotation Data Model. The annotation Parquet schema (defined in `docs/consumer-guide.md`) mirrors WADM body/target/selector structure.
