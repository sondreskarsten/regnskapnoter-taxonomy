---
concept_id: regnskap-no:Omlopsmidler
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
    text: "Omløpsmidler"
  - lang: en
    role: standardLabel
    text: "Current assets"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 B"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "B. Omløpsmidler"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 B"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:CurrentAssets
    relation: skos:closeMatch
    quality: approximate
    note: "regnskapsloven § 5-1: 'andre eiendeler er omløpsmidler'."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Eiendeler
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 6-2 B)

> Omløpsmidler
