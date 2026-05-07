---
concept_id: regnskap-no:GarantiforpliktelserIkkeRegnskapsfourt
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Garantiforpliktelser som ikke er regnskapsført"
  - lang: en
    role: standardLabel
    text: "Unrecognised guarantee obligations"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-28"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Summen av garantiforpliktelser som ikke er regnskapsført. Det skal opplyses særskilt dersom slike garantiforpliktelser er sikret ved pant."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-28"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ContingentLiabilitiesIncurredByVenturer
    relation: skos:broadMatch
    quality: approximate
---
