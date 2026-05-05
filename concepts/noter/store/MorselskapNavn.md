---
concept_id: regnskap-no:MorselskapNavn
namespace: regnskap-no
period_type: instant
balance: null
data_type: stringItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Navn på morselskap"
  - lang: en
    role: standardLabel
    text: "Name of parent"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-5"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NameOfParentEntity
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-5)

> Navn på morselskap
