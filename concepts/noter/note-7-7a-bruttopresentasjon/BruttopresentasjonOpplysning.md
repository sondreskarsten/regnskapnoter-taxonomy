---
concept_id: regnskap-no:BruttopresentasjonOpplysning
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
    text: "Bruttopresentasjon – opplysninger"
  - lang: en
    role: standardLabel
    text: "Gross presentation disclosures"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-7 a"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Det skal opplyses om bruttobeløp for eiendeler og forpliktelser, samt inntekter og kostnader som presenteres netto i resultat- eller balanseoppstilling."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-7 a"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfOffsettingOfFinancialAssetsAndFinancialLiabilitiesExplanatory
    relation: skos:broadMatch
    quality: approximate
---
