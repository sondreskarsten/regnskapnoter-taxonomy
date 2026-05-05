---
concept_id: regnskap-no:UtsattSkatt
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Utsatt skatt"
  - lang: en
    role: standardLabel
    text: "Deferred tax"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D I 2"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "D. Gjeld — I. Avsetning for forpliktelser — 2. Utsatt skatt"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 D I 2"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DeferredTaxLiabilities
    relation: skos:exactMatch
    quality: exact
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:AvsetningForForpliktelser
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 6-2 D I 2)

> Utsatt skatt
