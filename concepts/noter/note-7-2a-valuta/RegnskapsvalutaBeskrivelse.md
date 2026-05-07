---
concept_id: regnskap-no:RegnskapsvalutaBeskrivelse
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
    text: "Regnskapsvaluta og presentasjonsvaluta"
  - lang: en
    role: standardLabel
    text: "Functional and presentation currency"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-2a"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Dersom årsregnskapet presenteres i en annen valuta enn regnskapsvalutaen, skal regnskapsvalutaen og omregningskurser opplyses. I selskapsregnskapet skal det opplyses om tilsvarende omregningskurser til norske kroner."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-2a"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DescriptionOfFunctionalCurrency
    relation: skos:closeMatch
    quality: approximate
---
