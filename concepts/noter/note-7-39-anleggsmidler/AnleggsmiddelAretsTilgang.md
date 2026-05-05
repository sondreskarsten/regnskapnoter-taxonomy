---
concept_id: regnskap-no:AnleggsmiddelAretsTilgang
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
    text: "Tilgang anleggsmiddel"
  - lang: en
    role: standardLabel
    text: "Additions of non-current asset"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-39"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:AdditionsOtherThanThroughBusinessCombinationsPropertyPlantAndEquipment
    relation: skos:closeMatch
    quality: approximate
    note: "Year additions of anleggsmidler; IFRS distinguishes additions via business combinations."
axes:
  - axis: regnskap-no:KlassifiseringAvAnleggsmidlerAxis
    closed: true
---

## Verbatim text (regnskapsloven § 7-39)

> Tilgang anleggsmiddel
