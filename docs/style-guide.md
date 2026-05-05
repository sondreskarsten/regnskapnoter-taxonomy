# Style Guide

## Concept ID Format

`regnskap-no:UpperCamelCaseName`

- UpperCamelCase, no spaces.
- Norwegian roots (e.g., `Salgsinntekt`, not `SalesRevenue`).
- Drop short connector words (`og`, `i`, `av`, `til`, `for`, `med`, `eller`).
- Members end in `Member`: `AksjekapitalMember`.
- Axes end in `Axis`: `EgenkapitalKomponentAxis`.
- Hypercubes end in `Table`: `EgenkapitalRollforwardTable`.
- Sums prefix `Sum`: `SumDriftsinntekter`, `SumEgenkapital`.

## Labels

Norwegian standardLabel uses sentence-case Norwegian financial terminology as found in regnskapsloven. English standardLabel uses the IFRS-Full label where the concepts map exactly; otherwise a faithful translation that preserves Norwegian semantic distinctions.

## Verbatim Quotations

Every concept's Markdown body must contain at least one verbatim quote from the cited authoritative source, formatted as a Markdown blockquote with the citation in the heading.

## File Organization

Concepts under `concepts/<domain>/<sub-domain>/<ConceptId>.md` where `<domain>` is `primary` or `noter`. For noter, sub-domains follow the regnskapsloven § numbering: `note-7-38-loennskostnader`, etc.

Axes under `axes/<AxisId>.md` (flat).
