---
concept_id: regnskap-no:AnnenFinansinntektFunksjon
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Annen finansinntekt"
  - lang: en
    role: standardLabel
    text: "Other finance income"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 11"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "11. Annen finansinntekt"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1a (1) post 11"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:FinanceIncome
    relation: skos:closeMatch
    quality: approximate
    note: "Samme begrep som § 6-1 post 14."

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:ResultatForSkattekostnadFunksjon
    weight: +1
    order: 11
---

## Verbatim text (regnskapsloven § 6-1a (1) post 11)

> 11. Annen finansinntekt
