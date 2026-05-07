---
concept_id: regnskap-no:KonsernMellomvaerendeFordringer
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Mellomværende konsern – fordringer"
  - lang: en
    role: standardLabel
    text: "Intercompany receivables"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-22"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Samlet beløp som gjelder foretak i samme konsern, tilknyttet selskap og felles kontrollert virksomhet under fordringer."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-22"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:AmountsReceivableFromRelatedParties
    relation: skos:closeMatch
    quality: approximate
---
