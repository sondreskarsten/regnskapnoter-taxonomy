---
concept_id: regnskap-no:FoUUtgifterRegnskapsaret
namespace: regnskap-no
period_type: duration
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Utgifter til forskning og utvikling i regnskapsåret"
  - lang: en
    role: standardLabel
    text: "R&D expenditure in the financial year"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-14"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Utgifter som har gått med til forskning og utvikling i regnskapsåret."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-14"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ResearchAndDevelopmentExpense
    relation: skos:closeMatch
    quality: approximate
---
