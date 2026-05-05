# Ontology Guide

This document defines the design rules for `regnskapnoter-taxonomy`. It is the authoritative answer to "how do I model X?" questions.

## Information Model

The taxonomy adopts the XBRL 2.1 information model adapted to Norwegian regnskap noter. Each concept has the attributes:

- `concept_id`: globally unique identifier in the form `regnskap-no:<UpperCamelCaseName>`.
- `period_type`: `instant` for balance-sheet-style facts, `duration` for P&L and movement-style facts.
- `balance`: `debit` or `credit`. Required when `data_type` is `monetaryItemType`. Drives sign conventions in calculation arcs.
- `data_type`: one of `monetaryItemType`, `stringItemType`, `decimalItemType`, `sharesItemType`, `pureItemType`, `dateItemType`, `textBlockItemType`, `booleanItemType`, `integerItemType`.
- `substitution_group`: `item` for ordinary facts, `hypercubeItem` for tables, `dimensionItem` for axes.
- `abstract`: `true` for grouping concepts; `false` for reportable facts.

Together with a label set, a definition set, references, mappings, calculation arcs, and dimensional structure, these attributes form the complete concept declaration.

## Naming Conventions

Concept names follow IFRS Foundation conventions adapted for Norwegian:

- UpperCamelCase, no spaces.
- Norwegian roots; do not translate (`Lonnskostnad`, not `EmployeeBenefitsExpense`).
- Drop short connector words: `og`, `i`, `av`, `til`, `for`, `med`, `eller`.
- Plural vs singular: prefer singular; use plural only when the concept inherently aggregates (`Aksjonaerer` for shareholder list).
- Sub-decompositions retain the parent root: `Lonnskostnad` → `LonnskostnadPensjon`, `LonnskostnadAndreYtelser`.
- Sums are prefixed `Sum`: `SumDriftsinntekter`, `SumEgenkapital`.
- Members end in `Member`: `AksjekapitalMember`.
- Axes end in `Axis`: `EgenkapitalKomponentAxis`.
- Hypercubes end in `Table`: `EgenkapitalRollforwardTable`.
- Domains (root of an axis hierarchy) end in `Domain`: `EgenkapitalKomponentDomain`.

## Definitions

Definitions are verbatim quotes from authoritative sources. Paraphrasing is rejected by CI.

For each concept, at least one of the following must be present:

- A `definitions[*]` entry with `text` quoted verbatim from regnskapsloven, forskriften, or an NRS standard, with citation in `source_publisher`, `source_document`, `source_paragraph`, and `applicable_from_fiscal_year`.
- A verbatim quotation block in the Markdown body under a heading "Verbatim text (...)" with the citation in the heading.

Both are recommended. The YAML `definitions` field drives the Parquet/RDF distribution; the Markdown body drives human-readable display.

## References

Every concept must cite at least one regnskapsloven paragraph or NRS standard. References are stored in `references[*]` with:

- `publisher`: `Stortinget`, `NRS`, `IFRS Foundation`.
- `document`: `regnskapsloven`, `forskrift-til-regnskapsloven`, `NRS 8`, `NRS(F) Resultatskatt`, etc.
- `paragraph`: the cited paragraph in the source document's notation (`§ 6-1 (1) post 1`, `kap. 5.3`).
- `version`: the source-document version (relevant when NRS standards are revised; not used for regnskapsloven where the law is identified by its lov-date).
- `applicable_from_fiscal_year`: the fiscal year from which this reference is operative.
- `applicable_to_fiscal_year`: the last fiscal year for which this reference is operative; `null` if current.

References to NRS standards must cite a `(document, version)` pair listed in `references/nrs-standards.yaml`. References to regnskapsloven must cite a paragraph listed in `references/regnskapsloven-paragraphs.yaml`. CI enforces this.

## Calculation Arcs

Calculation arcs express arithmetic constraints: parent value equals weighted sum of children. Stored in `parents[*]` on the child concept:

- `role`: the Extended Link Role (ELR) name. Format: `[NNNNNN] Description`. Example: `[610000] Resultatregnskap etter art`.
- `parent`: the parent concept ID.
- `weight`: `+1` (added) or `-1` (subtracted).
- `order`: integer for presentation ordering within the parent.

Calculation arcs are role-scoped. The same parent can have different children in different roles (a balance-sheet view vs a note view). XBRL 2.1 restricts calculations to facts in the same context (same period and dimensions); the taxonomy mirrors this.

## Dimensional Structure

Some disclosures decompose along axes (dimensions) rather than into separate concepts. The pattern, from XBRL Dimensions 1.0:

```
[Primary item] --has-hypercube--> [Hypercube] --hypercube-dimension--> [Axis]
                                                                       |
                                                              dimension-domain
                                                                       ↓
                                                                  [Domain]
                                                                       |
                                                              domain-member
                                                                       ↓
                                                                  [Member]
```

Use dimensional modeling when:
- The same set of line items is reported across multiple categories (e.g., equity rollforward across share classes).
- The categories are an enumerable set known in advance (explicit dimensions).
- The categories are open-ended but typed (typed dimensions, e.g., a list of subsidiary names).

Use distinct concepts when:
- The categories are few (≤4) and naming each is clearer.
- The decomposition is one-off and not reused elsewhere in the taxonomy.

## IFRS-Full Mappings

Every monetary concept should have an `ifrs-full:` mapping where one exists. Stored in `mappings[*]`:

- `to`: the IFRS-Full concept ID.
- `relation`: `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, or `skos:relatedMatch`.
- `quality`: `exact`, `approximate`, or `norwegian_specific`. If `norwegian_specific`, `to` and `relation` are null.
- `note`: required when `quality` is `approximate`. Explains the divergence between regnskap-no and ifrs-full semantics.

Use `skos:exactMatch` only when concepts are substitutable in any analytical context. When in doubt, use `skos:closeMatch` and document the divergence in `note`.

## Status Lifecycle

Concepts move through `candidate → standard → deprecated → retired`.

- `candidate`: introduced but not yet operational. Consumers should not depend on it.
- `standard`: operational.
- `deprecated`: replaced by another concept or rendered obsolete. Retains its ID forever.
- `retired`: no longer used in any active fiscal year. ID remains reserved.

A concept marked `deprecated` must have a `deprecated_date`. A `deprecated_replacement` is recommended but not required (a concept may simply be obsolete with no replacement).

A concept's `concept_id` is never reused once it has appeared in a published release.

## Fiscal Year Applicability

References and definitions can be year-scoped via `applicable_from_fiscal_year` and `applicable_to_fiscal_year`. This handles regnskapsloven amendments and NRS standard revisions:

- A concept whose definition was updated by an NRS revision has two `definitions[*]` entries: one with `applicable_to_fiscal_year` closing at the end of the prior version's effectivity, one with `applicable_from_fiscal_year` opening at the start of the new version's effectivity.
- A concept introduced by a regnskapsloven amendment has `introduced_version` reflecting the taxonomy release that added the concept; references carry `applicable_from_fiscal_year` reflecting the law's effective date.

The applicability windows must be contiguous: there must be no gap between the end of one window and the start of the next.

## Forbidden Patterns

The following are rejected by CI or by review:

- Paraphrased definitions. Verbatim quoting only.
- Concept renames. Deprecate and replace.
- Removed concepts. Deprecate.
- Reused concept IDs. Forever forbidden.
- IFRS-Full mappings without `note` when `quality` is `approximate`.
- Calculation arcs that form cycles.
- References to NRS standards or regnskapsloven paragraphs not in the registry.
- `weight` values other than `+1` or `-1`.
- `period_type` values other than `instant` or `duration`.
- `balance` on non-monetary concepts.
- Two `definitions[*]` entries with overlapping applicability windows for the same `(lang, role)`.
