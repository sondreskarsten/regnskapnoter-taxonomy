---
concept_id: regnskap-no:KostnadSolgteVarer
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
    text: "Kostnad solgte varer"
  - lang: en
    role: standardLabel
    text: "Cost of sales"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 2"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:CostOfSales
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:BruttoresultatFunksjon
    weight: -1
    order: 2
---

## Verbatim text (regnskapsloven § 6-1a (1) post 2)

> 2. Kostnad solgte varer
