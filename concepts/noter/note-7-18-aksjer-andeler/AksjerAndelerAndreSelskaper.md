---
concept_id: regnskap-no:AksjerAndelerAndreSelskaper
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
    text: "Aksjer og andeler i andre selskaper (>10%)"
  - lang: en
    role: standardLabel
    text: "Shares in other companies (>10%)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-18"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Aksjer og andeler i selskaper hvor den regnskapspliktiges eierandel er over 10 prosent eller investeringen utgjør mer enn 50 prosent av den regnskapspliktiges egenkapital, skal spesifiseres etter selskap dersom investeringen ikke omfattes av §§ 7-15 og 7-16 . Det skal opplyses om balanseført verdi, eventuell markedsverdi og eierandel i hvert selskap."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-18"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfInvestmentsOtherThanInvestmentsAccountedForUsingEquityMethodExplanatory
    relation: skos:broadMatch
    quality: approximate
---
