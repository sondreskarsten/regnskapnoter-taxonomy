# regnskapnoter-taxonomy

Concept dictionary for Norwegian financial statement notes (regnskap noter).

## Purpose

This repository defines the concept dictionary, dimensional structure, calculation arcs, multilingual labels, references to authoritative sources (regnskapsloven and NRS standards), and IFRS-Full mappings used to label `(note_text, value)` facts extracted from Norwegian regnskap PDFs. The repository is the source of truth for noter categorization across the Registrum platform.

The repository does not perform extraction, OCR, classification, or reconciliation. Those responsibilities remain in `noter-text-extraction`, `noter-extraction-tidy-tables`, `noter-prompt-optimizer`, and `noter-canonicalizer`. The taxonomy is consumed by these pipelines as a versioned dependency.

## Architecture

The design adopts established conventions:

- **XBRL 2.1 information model** for concept attributes (periodType, balance, item types), calculation linkbases, and dimensional hypercubes (XBRL Dimensions XDT).
- **SKOS** for vocabulary semantics (Concept, prefLabel, altLabel, definition, broader/narrower, mappings).
- **W3C Web Annotation Data Model (WADM)** for the `(note_text, value) → concept` annotation layer emitted by downstream pipelines.
- **SHACL + JSON Schema** for validation.
- **SemVer 2.0.0** for releases. Concept IDs are forever; deprecation never reuses them.
- **Markdown + YAML front-matter** as source of truth, with built artifacts in Parquet, Turtle, and JSON-LD.

See `docs/architecture.md` for the full design rationale.

## Repository Layout

```
concepts/         source of truth, one .md per concept
axes/             one .md per dimensional axis
references/       NRS standards and regnskapsloven citation registries
mappings/         to-ifrs-full.csv and other cross-taxonomy mappings
schemas/          JSON Schema and SHACL shapes
build/            Python build pipeline (parse → Parquet/Turtle/JSON-LD)
tests/            pytest suite
docs/             architecture, style guide, deprecation policy, consumer guide
artifacts/        gitignored; CI publishes to GCS
```

## Distribution

Each release publishes nine Parquet files plus a Turtle SKOS view plus a JSON-LD serialization to:

- `gs://regnskapnoter-taxonomy/v<X.Y.Z>/`
- `gs://regnskapnoter-taxonomy/latest/`

Consumers pin to a specific version. See `docs/consumer-guide.md`.

## Status

Pre-v1.0.0. See `CHANGELOG.md` for release history.

## License

CC-BY-4.0. See `LICENSE`.
