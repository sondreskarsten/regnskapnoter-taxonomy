# Annotation UI Deployment Options

The taxonomy emits `annotations.parquet` via `build.annotations.emit_annotations`, conformant with the W3C Web Annotation Data Model (WADM). Two UI options can sit on top:

## Hypothes.is (WADM-native)

Hypothes.is uses WADM as its native data model. To export annotations from this repo into Hypothes.is:

1. Convert each `annotations.parquet` row to WADM JSON-LD using the Hypothes.is API format.
2. POST to `https://hypothes.is/api/annotations` with bearer token.
3. The `target.selector` array combines `FragmentSelector` (`#page=N`), `TextQuoteSelector` (with `prefix`/`exact`/`suffix`), and optionally `TextPositionSelector`.

Best for: web/PDF readers, lightweight reviewer workflow, public sharing.

## INCEpTION (CAS-based annotation studio)

INCEpTION uses UIMA CAS internally but exports to many formats including WADM. To bootstrap a project:

1. Install INCEpTION (Java application).
2. Create a project with the regnskap-no concept scheme as a "tagset".
3. Import per-orgnr PDFs as documents.
4. Export annotations as JSON-LD or RDF for round-trip into `annotations.parquet`.

Best for: heavy-weight annotation campaigns, multi-annotator workflows with adjudication, machine-learning training data curation.

## Decision

Hypothes.is is recommended for routine analyst review; INCEpTION for ground-truth labeling campaigns.
