---
concept_id: regnskap-no:Goodwill
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
    text: "Goodwill"
  - lang: en
    role: standardLabel
    text: "Goodwill"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A I 4"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:Goodwill
    relation: skos:exactMatch
    quality: exact
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:ImmaterielleEiendeler
    weight: +1
    order: 4
---

## Verbatim text (regnskapsloven § 6-2 A I 4)

> Goodwill
