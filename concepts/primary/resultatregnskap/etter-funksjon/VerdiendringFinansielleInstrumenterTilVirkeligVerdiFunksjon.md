---
concept_id: regnskap-no:VerdiendringFinansielleInstrumenterTilVirkeligVerdiFunksjon
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
    text: "Verdiendring av finansielle instrumenter vurdert til virkelig verdi"
  - lang: en
    role: standardLabel
    text: "Fair value gains/losses on financial instruments"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 13"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "13. Verdiendring av finansielle instrumenter vurdert til virkelig verdi"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1a (1) post 13"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:GainsLossesOnFinancialAssetsAtFairValueThroughProfitOrLoss
    relation: skos:closeMatch
    quality: approximate
    note: "Samme begrep som § 6-1 post 15."

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:ResultatForSkattekostnadFunksjon
    weight: +1
    order: 13
---

## Verbatim text (regnskapsloven § 6-1a (1) post 13)

> 13. Verdiendring av finansielle instrumenter vurdert til virkelig verdi
