---
concept_id: regnskap-no:Aksjekapital
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
    text: "Aksjekapital"
  - lang: en
    role: standardLabel
    text: "Share capital"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 C I 1"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "C. Egenkapital — I. Innskutt egenkapital — 1. Selskapskapital"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 C I 1"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:IssuedCapital
    relation: skos:exactMatch
    quality: exact
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:InnskuttEgenkapital
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 C I 1)

> Aksjekapital
