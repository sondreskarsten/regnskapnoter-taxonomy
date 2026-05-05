# Style Guide

## Concept ID Naming

- Format: `regnskap-no:<UpperCamelCaseName>`
- Norwegian roots, never English: `Lonnskostnad`, not `EmployeeBenefitsExpense`.
- Drop short connector words: `og`, `i`, `av`, `til`, `for`, `med`, `eller`.
- Singular preferred unless concept aggregates: `Aksjonaerer`, `Datterselskap` (singular).
- Sums prefixed `Sum`: `SumDriftsinntekter`.
- Members end in `Member`: `AksjekapitalMember`.
- Axes end in `Axis`: `EgenkapitalKomponentAxis`.

## Labels

Every concept must have:
- `lang: nb, role: standardLabel` (Norwegian)
- `lang: en, role: standardLabel` (English)

Optional roles: `terseLabel`, `verboseLabel`, `documentationLabel`, `totalLabel`, `periodStartLabel`, `periodEndLabel`, `negatedLabel`, `deprecatedLabel`.

## Definitions and Verbatim Quoting

Definitions in `definitions[*]` must be verbatim from authoritative sources. Paraphrasing is rejected by review.

The Markdown body should contain at least one verbatim quotation block:

```markdown
## Verbatim text (regnskapsloven § 6-1 (1) post 1)

> 1. Salgsinntekt
```

## References

Every concept must cite at least one regnskapsloven paragraph or NRS standard, listed in `references[*]`. Citations must resolve to entries in `references/regnskapsloven-paragraphs.yaml`, `references/forskrift-paragraphs.yaml`, or `references/nrs-standards.yaml`.

## IFRS-Full Mappings

Every monetary concept should have an `ifrs-full:` mapping where one exists. Use:

- `skos:exactMatch` only when concepts are substitutable in any analytical context.
- `skos:closeMatch` when concepts are mostly equivalent but with caveats; the `note` field is required.
- `quality: norwegian_specific` when no IFRS-Full equivalent exists; `to` and `relation` are null.

## Calculation Arcs

Use `parents[*]`:

- `role`: ELR notation, e.g., `[610000] Resultatregnskap etter art`.
- `parent`: the parent concept ID.
- `weight`: `+1` (added) or `-1` (subtracted).
- `order`: ≥ 1, used for presentation ordering.

A concept may appear as a child in multiple roles (different views of the same fact).

## Forbidden Patterns

- Paraphrased definitions (use verbatim quotes only).
- Concept ID renames (deprecate and replace).
- Reused concept IDs (forever forbidden).
- IFRS-Full mappings without `note` when `quality: approximate`.
- `weight` values other than `+1` or `-1`.
- `balance` on non-monetary concepts.
