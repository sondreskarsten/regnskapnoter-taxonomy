---
concept_id: regnskap-no:FortsattDriftForutsetning
namespace: regnskap-no
period_type: duration
data_type: booleanItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Fortsatt drift forutsetning"
  - lang: en
    role: standardLabel
    text: "Going concern assumption"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:DisclosureOfMaterialUncertaintiesThatMayCastSignificantDoubtOnEntitysAbilityToContinueAsGoingConcern
    relation: skos:closeMatch
    quality: approximate
    note: "Boolean flag whether going-concern assumption is applied."
---

## Verbatim text (regnskapsloven § 7-46)

> Fortsatt drift forutsetning
