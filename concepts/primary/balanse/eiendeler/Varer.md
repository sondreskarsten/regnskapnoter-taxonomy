---
concept_id: regnskap-no:Varer
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Varer"
  - lang: en
    role: standardLabel
    text: "Inventories"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 B I"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:Inventories
    relation: skos:exactMatch
    quality: exact
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Omlopsmidler
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 B I)

> Varer
