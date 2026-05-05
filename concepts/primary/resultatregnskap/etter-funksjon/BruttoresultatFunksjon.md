---
concept_id: regnskap-no:BruttoresultatFunksjon
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
    text: "Bruttoresultat"
  - lang: en
    role: standardLabel
    text: "Gross profit"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 3"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "3. Brutto resultat"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1a (1) post 3"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:GrossProfit
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:DriftsresultatFunksjon
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-1a (1) post 3)

> 3. Brutto resultat
