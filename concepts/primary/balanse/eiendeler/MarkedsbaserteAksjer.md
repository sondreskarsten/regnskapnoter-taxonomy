---
concept_id: regnskap-no:MarkedsbaserteAksjer
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
    text: "Markedsbaserte aksjer"
  - lang: en
    role: standardLabel
    text: "Marketable shares"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 B III 2"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "B. Omløpsmidler / III."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 B III 2"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:CurrentEquityInvestments
    relation: skos:closeMatch
    quality: approximate
    note: "Marketable short-term equity investments."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:InvesteringerOmlopsmidler
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 6-2 B III 2)

> Markedsbaserte aksjer
