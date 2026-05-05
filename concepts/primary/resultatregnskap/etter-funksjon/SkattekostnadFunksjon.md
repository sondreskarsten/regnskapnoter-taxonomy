---
concept_id: regnskap-no:SkattekostnadFunksjon
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
    paragraph: "§ 6-1a (1) post 15"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "15. Skattekostnad"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1a (1) post 15"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:IncomeTaxExpenseContinuingOperations
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:AarsresultatFunksjon
    weight: -1
    order: 15
---

## Verbatim text (regnskapsloven § 6-1a (1) post 15)

> 15. Skattekostnad
