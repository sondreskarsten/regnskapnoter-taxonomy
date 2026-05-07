---
concept_id: regnskap-no:OmregningskursBalansedagen
namespace: regnskap-no
period_type: instant
balance: null
data_type: decimalItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Omregningskurs ved balansedagen"
  - lang: en
    role: standardLabel
    text: "Exchange rate at balance sheet date"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-2a"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Omregningskurs fra regnskapsvaluta til presentasjonsvaluta ved balansedagen."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-2a"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ExchangeRateAtEndOfReportingPeriod
    relation: skos:exactMatch
    quality: approximate
---
