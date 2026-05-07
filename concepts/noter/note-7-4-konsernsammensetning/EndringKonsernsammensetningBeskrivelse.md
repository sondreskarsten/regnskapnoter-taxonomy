---
concept_id: regnskap-no:EndringKonsernsammensetningBeskrivelse
namespace: regnskap-no
period_type: duration
balance: null
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Endring i konsernsammensetning"
  - lang: en
    role: standardLabel
    text: "Change in group composition"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-4"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Ved endring i konsernsammensetningen skal det gis opplysninger som muliggjør sammenligning med tidligere årsregnskap."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-4"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfBusinessCombinationsExplanatory
    relation: skos:broadMatch
    quality: approximate
---
