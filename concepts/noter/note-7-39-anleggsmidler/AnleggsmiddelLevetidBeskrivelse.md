---
concept_id: regnskap-no:AnleggsmiddelLevetidBeskrivelse
namespace: regnskap-no
period_type: duration
balance: null
data_type: stringItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Beskrivelse av forventet levetid"
  - lang: en
    role: standardLabel
    text: "Description of useful life"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-39"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:UsefulLivesOrDepreciationRatesPropertyPlantAndEquipment
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept inkluderer immaterielle eiendeler og varige driftsmidler; IFRS-Full er begrenset til PP&E."

---

## Verbatim text (regnskapsloven § 7-39)

> Beskrivelse av forventet levetid
