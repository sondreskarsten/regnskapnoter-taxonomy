---
concept_id: regnskap-no:AnleggsmiddelAretsAvgang
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
    text: "Avgang anleggsmiddel"
  - lang: en
    role: standardLabel
    text: "Disposals of non-current asset"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-39"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:DisposalsPropertyPlantAndEquipment
    relation: skos:closeMatch
    quality: approximate
    note: "Year disposals of anleggsmidler; IFRS distinguishes disposals via business combinations."
axes:
  - axis: regnskap-no:KlassifiseringAvAnleggsmidlerAxis
    closed: true
---

## Verbatim text (regnskapsloven § 7-39)

> Avgang anleggsmiddel
