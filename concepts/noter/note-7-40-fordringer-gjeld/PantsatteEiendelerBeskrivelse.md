---
concept_id: regnskap-no:PantsatteEiendelerBeskrivelse
namespace: regnskap-no
period_type: instant
balance: null
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Beskrivelse av pantsatte eiendeler"
  - lang: en
    role: standardLabel
    text: "Description of pledged assets"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:DescriptionOfNatureAndCarryingAmountOfAssetsPledgedAsCollateralForLiabilities
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept er beskrivelse av pantsatte eiendeler; IFRS-Full har lignende men er gruppert under sikkerhetsstillelse."

---

## Verbatim text (regnskapsloven § 7-40)

> Beskrivelse av pantsatte eiendeler
