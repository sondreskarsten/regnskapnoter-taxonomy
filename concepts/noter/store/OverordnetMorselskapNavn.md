---
concept_id: regnskap-no:OverordnetMorselskapNavn
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
    text: "Navn på overordnet morselskap"
  - lang: en
    role: standardLabel
    text: "Name of ultimate parent"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-5"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NameOfUltimateParentOfGroup
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-5)

> Navn på overordnet morselskap
