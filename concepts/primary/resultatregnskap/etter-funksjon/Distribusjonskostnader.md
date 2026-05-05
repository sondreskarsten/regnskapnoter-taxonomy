---
concept_id: regnskap-no:Distribusjonskostnader
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
    text: "Distribusjonskostnader"
  - lang: en
    role: standardLabel
    text: "Distribution costs"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 4"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:DistributionCosts
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:DriftsresultatFunksjon
    weight: -1
    order: 4
---

## Verbatim text (regnskapsloven § 6-1a (1) post 4)

> 4. Distribusjonskostnader
