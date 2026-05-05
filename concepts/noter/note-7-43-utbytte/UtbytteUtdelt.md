---
concept_id: regnskap-no:UtbytteUtdelt
namespace: regnskap-no
period_type: duration
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Utdelt utbytte"
  - lang: en
    role: standardLabel
    text: "Dividends paid"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-43"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:DividendsPaidClassifiedAsFinancingActivities
    relation: skos:closeMatch
    quality: approximate
    note: "Dividends paid in the period; IFRS classifies in cash flow statement."
---

## Verbatim text (regnskapsloven § 7-43)

> Utdelt utbytte
