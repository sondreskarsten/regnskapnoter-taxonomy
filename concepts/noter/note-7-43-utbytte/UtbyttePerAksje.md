---
concept_id: regnskap-no:UtbyttePerAksje
namespace: regnskap-no
period_type: duration
data_type: decimalItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Utbytte per aksje"
  - lang: en
    role: standardLabel
    text: "Dividend per share"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-43"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:DividendsPerShare
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-43)

> Utbytte per aksje
