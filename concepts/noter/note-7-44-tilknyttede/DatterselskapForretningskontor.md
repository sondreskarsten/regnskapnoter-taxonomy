---
concept_id: regnskap-no:DatterselskapForretningskontor
namespace: regnskap-no
period_type: instant
data_type: stringItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Datterselskap - forretningskontor"
  - lang: en
    role: standardLabel
    text: "Subsidiary - registered office"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:CountryOfIncorporationOfSubsidiary
    relation: skos:closeMatch
    quality: approximate
    note: "Norwegian disclosure includes registered office (forretningskontor); IFRS uses country of incorporation."
---

## Verbatim text (regnskapsloven § 7-44)

> Datterselskap - forretningskontor
