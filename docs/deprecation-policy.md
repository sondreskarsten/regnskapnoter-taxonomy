# Deprecation Policy

## Lifecycle

Every concept has a `status` field that moves through:

```
candidate → standard → deprecated → retired
```

### candidate

A new concept introduced in a release but not yet operational. Consumers should not depend on candidate concepts. Promote to `standard` in a later release.

### standard

The default. Operational and committed.

### deprecated

The concept is replaced by another concept or rendered obsolete by a regnskapsloven amendment or NRS revision. The concept retains its `concept_id` forever. Required fields when transitioning to deprecated:

- `deprecated_date`: the date the concept was deprecated.
- `deprecated_replacement`: recommended; the concept_id of the replacement, if any.

### retired

The concept is no longer used in any active fiscal year. The `concept_id` remains reserved.

## Concept ID Immutability

A concept's `concept_id` is immutable once it has appeared in a published release. To "rename" a concept, you must:

1. Mark the old concept as `deprecated` with the appropriate `deprecated_date`.
2. Create a new concept with the new ID.
3. Add a mapping from old to new in `mappings/old-to-new.csv` (or via `mappings[*]` on the new concept with `relation: skos:exactMatch` and a `note` indicating the replacement relationship).

The old `concept_id` is never reassigned to a different concept.

## Backward Compatibility

A consumer pinned to v1.5.0 must function unchanged against v1.7.0. A consumer pinned to v1.5.0 may need code changes for v2.0.0; these are documented in `CHANGELOG.md` with a migration guide.

## Removal

Concepts are never removed. They progress through `deprecated → retired`. Concepts can be retired only when no active fiscal year requires them.
