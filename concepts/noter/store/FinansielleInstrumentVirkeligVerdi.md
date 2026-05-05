---
concept_id: regnskap-no:FinansielleInstrumentVirkeligVerdi
namespace: regnskap-no
period_type: instant
balance: null
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Virkelig verdi finansielle instrumenter"
  - lang: en
    role: standardLabel
    text: "Fair value of financial instruments"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-17"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:FinancialAssetsAtFairValueThroughProfitOrLoss
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konseptet aggregerer; ifrs-full splitter etter klassifisering."
---

## Verbatim text (regnskapsloven § 7-17)

> Virkelig verdi finansielle instrumenter
