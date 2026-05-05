---
concept_id: regnskap-no:AnleggsmiddelOkonomiskLevetid
namespace: regnskap-no
period_type: duration
data_type: decimalItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Økonomisk levetid"
  - lang: en
    role: standardLabel
    text: "Economic useful life"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-39"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:UsefulLifeMeasuredAsPeriodOfTimePropertyPlantAndEquipment
    relation: skos:closeMatch
    quality: approximate
    note: "Economic useful life used for depreciation; IFRS records as useful-life period (IAS 16.50)."
axes:
  - axis: regnskap-no:KlassifiseringAvAnleggsmidlerAxis
    closed: true
---

## Verbatim text (regnskapsloven § 7-39)

> Økonomisk levetid
