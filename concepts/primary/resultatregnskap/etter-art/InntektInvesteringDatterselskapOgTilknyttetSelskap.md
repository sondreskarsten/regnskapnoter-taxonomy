---
concept_id: regnskap-no:InntektInvesteringDatterselskapOgTilknyttetSelskap
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
    text: "Inntekt på investering i datterselskap og tilknyttet selskap"
  - lang: en
    role: standardLabel
    text: "Income from investment in subsidiaries and associates"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 11"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "11. Inntekt på investering i datterselskap og tilknyttet selskap"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1 (1) post 11"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ShareOfProfitLossOfAssociatesAndJointVenturesAccountedForUsingEquityMethod
    relation: skos:closeMatch
    quality: approximate
    note: "IFRS-Full splitter datterselskap (konsolidert) fra tilknyttet (egenkapitalmetoden); norsk konseptet aggregerer."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:ResultatForSkattekostnad
    weight: +1
    order: 11
---

## Verbatim text (regnskapsloven § 6-1 (1) post 11)

> 11. Inntekt på investering i datterselskap og tilknyttet selskap
