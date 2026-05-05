---
concept_id: regnskap-no:AnleggsmiddelAretsNedskrivning
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
    text: "Årets nedskrivning"
  - lang: en
    role: standardLabel
    text: "Impairment for the year"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-39"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:ImpairmentLossRecognisedInProfitOrLossPropertyPlantAndEquipment
    relation: skos:exactMatch
    quality: exact
axes:
  - axis: regnskap-no:KlassifiseringAvAnleggsmidlerAxis
    closed: true
---

## Verbatim text (regnskapsloven § 7-39)

> Årets nedskrivning
