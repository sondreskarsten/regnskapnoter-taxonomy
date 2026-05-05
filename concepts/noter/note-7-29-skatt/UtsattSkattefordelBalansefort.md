---
concept_id: regnskap-no:UtsattSkattefordelBalansefort
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Utsatt skattefordel balanseført"
  - lang: en
    role: standardLabel
    text: "Deferred tax asset recognized in balance sheet"

references:
  - publisher: NRS
    document: Resultatskatt
    paragraph: "kap. 5"
    applicable_from_fiscal_year: 2014
mappings:
  - to: ifrs-full:DeferredTaxAssets
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (NRS(F) Resultatskatt kap. 5)

> Utsatt skattefordel balanseført
