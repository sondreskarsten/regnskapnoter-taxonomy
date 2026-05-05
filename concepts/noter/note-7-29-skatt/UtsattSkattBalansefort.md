---
concept_id: regnskap-no:UtsattSkattBalansefort
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
    text: "Utsatt skatt balanseført"
  - lang: en
    role: standardLabel
    text: "Deferred tax recognized in balance sheet"

references:
  - publisher: NRS
    document: Resultatskatt
    paragraph: "kap. 5"
    applicable_from_fiscal_year: 2014
mappings:
  - to: ifrs-full:DeferredTaxLiabilities
    relation: skos:closeMatch
    quality: approximate
    note: "Net deferred tax position; IFRS distinguishes asset and liability sides."
---

## Verbatim text (NRS(F) Resultatskatt kap. 5)

> Utsatt skatt balanseført
