---
concept_id: regnskap-no:GjeldTilForetakSammeKonsern
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
    text: "Øvrig gjeld til foretak i samme konsern"
  - lang: en
    role: standardLabel
    text: "Long-term debt to group enterprises"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D II 4"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "D. Gjeld / II."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 D II 4"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Long-term inter-company debt; Norwegian-specific separation."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:AnnenLangsiktigGjeld
    weight: +1
    order: 4
---

## Verbatim text (regnskapsloven § 6-2 D II 4)

> Øvrig gjeld til foretak i samme konsern
