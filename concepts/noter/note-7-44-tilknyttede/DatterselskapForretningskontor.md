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
  - publisher: NRS
    document: NRS 17
    paragraph: "kap. 6"
    applicable_from_fiscal_year: 2018
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999
    applicable_to_fiscal_year: 2020
definitions:
  - lang: nb
    role: definition
    text: "(Opphevet)"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999
    applicable_to_fiscal_year: 2020
    authoritative: true

mappings:
  - to: ifrs-full:CountryOfIncorporationOfSubsidiary
    relation: skos:closeMatch
    quality: approximate
    note: "Norwegian disclosure includes registered office (forretningskontor); IFRS uses country of incorporation."
---

## Verbatim text (regnskapsloven § 7-44)

> Datterselskap - forretningskontor
