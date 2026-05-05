---
concept_id: regnskap-no:Gjeld5arPlus
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Gjeld med forfall over 5 år"
  - lang: en
    role: standardLabel
    text: "Debt due after 5 years"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40 (1)"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:NoncurrentBorrowings
    relation: skos:closeMatch
    quality: approximate
    note: "Norwegian disclosure of debt with maturity > 5 years; IFRS uses contractual maturity analysis (IFRS 7)."
---

## Verbatim text (regnskapsloven § 7-40 (1))

> Gjeld med forfall over 5 år
