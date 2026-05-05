# Deprecation Policy

## Lifecycle

Every concept moves through `candidate → standard → deprecated → retired`.

- `candidate`: introduced but not yet operational. Consumers should not depend on it.
- `standard`: operational. The default for new concepts after their candidacy period.
- `deprecated`: replaced by another concept or rendered obsolete. Retains its ID forever. Has `deprecated_date` (required) and `deprecated_replacement` (recommended but not required).
- `retired`: no longer used in any active fiscal year. ID remains reserved.

## Immutability of Concept IDs

Once a concept_id has appeared in a published release, it cannot be reassigned. Concept renames are forbidden. To rename a concept:

1. Set the old concept's status to `deprecated` with `deprecated_date` and `deprecated_replacement` set to the new concept's ID.
2. Add a new concept with the new ID.
3. Add a `dct:isReplacedBy` triple in the RDF and a `mappings[*]` entry of relation `skos:isReplacedBy`.

## SemVer Mapping

- Concept removed: major version bump. (Concepts are deprecated, not removed; this rule is only triggered if a concept is moved to `retired` and downstream consumers depend on its presence.)
- Concept_id changed: forbidden.
- Concept's `period_type`, `balance`, or `data_type` changed: major version bump.
- New concepts added: minor version bump.
- New labels in any language added: minor version bump.
- New references or mappings added: minor version bump.
- Typo or label refinement: patch version bump.
