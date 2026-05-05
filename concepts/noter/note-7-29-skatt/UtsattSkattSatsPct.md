---
concept_id: regnskap-no:UtsattSkattSatsPct
namespace: regnskap-no
period_type: instant
data_type: percentItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Utsatt skatt - skattesats"
  - lang: en
    role: standardLabel
    text: "Deferred tax rate"

references:
  - publisher: NRS
    document: Resultatskatt
    paragraph: "kap. 5"
    applicable_from_fiscal_year: 2014
mappings:
  - to: ifrs-full:AverageEffectiveTaxRate
    relation: skos:closeMatch
    quality: approximate
    note: "Norwegian corporate tax rate (typically 22%); IFRS uses effective tax rate reconciliation."
---

## Verbatim text (NRS(F) Resultatskatt kap. 5)

> Utsatt skatt - skattesats
