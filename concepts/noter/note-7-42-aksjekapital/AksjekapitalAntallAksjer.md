---
concept_id: regnskap-no:AksjekapitalAntallAksjer
namespace: regnskap-no
period_type: instant
data_type: sharesItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Antall aksjer"
  - lang: en
    role: standardLabel
    text: "Number of shares"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-42"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:NumberOfSharesIssued
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-42)

> Antall aksjer
