---
concept_id: regnskap-no:InnskuttEgenkapital
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
    text: "Innskutt egenkapital"
  - lang: en
    role: standardLabel
    text: "Contributed equity"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 C I"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:IssuedCapital
    relation: skos:closeMatch
    quality: approximate
    note: "Aggregation of share capital + share premium + other contributed equity."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Egenkapital
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 C I)

> Innskutt egenkapital
