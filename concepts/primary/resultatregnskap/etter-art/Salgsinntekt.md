---
concept_id: regnskap-no:Salgsinntekt
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Salgsinntekt"
  - lang: en
    role: standardLabel
    text: "Sales revenue"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 1"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:Revenue
    relation: skos:closeMatch
    quality: approximate
    note: "ifrs-full:Revenue under IFRS 15 includes contract-asset and variable-consideration adjustments; regnskapsloven § 6-1 post 1 is 'inntekt fra salg av varer og tjenester' uten tilsvarende differensiering."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:SumDriftsinntekter
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-1 (1) post 1)

> 1. Salgsinntekt
