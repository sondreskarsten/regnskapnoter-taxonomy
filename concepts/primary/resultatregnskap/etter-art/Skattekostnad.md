---
concept_id: regnskap-no:Skattekostnad
namespace: regnskap-no
period_type: duration
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Skattekostnad"
  - lang: en
    role: standardLabel
    text: "Tax expense"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 20"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "20. Skattekostnad"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1 (1) post 20"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:IncomeTaxExpenseContinuingOperations
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:Aarsresultat
    weight: -1
    order: 20
---

## Verbatim text (regnskapsloven § 6-1 (1) post 20)

> 20. Skattekostnad
