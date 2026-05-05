---
concept_id: regnskap-no:AnleggsmiddelAkkumulerteAvskrivninger
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
    text: "Akkumulerte avskrivninger"
  - lang: en
    role: standardLabel
    text: "Accumulated depreciation"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-39"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:PropertyPlantAndEquipmentAccumulatedDepreciationAndImpairment
    relation: skos:closeMatch
    quality: approximate
    note: "Norwegian disclosure separates accumulated depreciation per anleggsmiddel class; IFRS aggregates depreciation and impairment."
axes:
  - axis: regnskap-no:KlassifiseringAvAnleggsmidlerAxis
    closed: true
---

## Verbatim text (regnskapsloven § 7-39)

> Akkumulerte avskrivninger
