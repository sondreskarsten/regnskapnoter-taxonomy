---
concept_id: regnskap-no:AdministrativeKostnader
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
    text: "Administrative kostnader"
  - lang: en
    role: standardLabel
    text: "Administrative expenses"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 5"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:AdministrativeExpense
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:DriftsresultatFunksjon
    weight: -1
    order: 5
---

## Verbatim text (regnskapsloven § 6-1a (1) post 5)

> 5. Administrative kostnader
