---
concept_id: regnskap-no:AnleggsmiddelAnskaffelseskost
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Anskaffelseskost anleggsmiddel"
  - lang: en
    role: standardLabel
    text: "Cost of non-current asset"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-39"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:PropertyPlantAndEquipmentGrossCarryingAmount
    relation: skos:closeMatch
    quality: approximate
    note: "Anskaffelseskost (historical cost basis) per regnskapsloven § 5-1; IFRS reports gross carrying amount."
axes:
  - axis: regnskap-no:KlassifiseringAvAnleggsmidlerAxis
    closed: true
---

## Verbatim text (regnskapsloven § 7-39)

> Anskaffelseskost anleggsmiddel
