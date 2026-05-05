---
concept_id: regnskap-no:AksjekapitalPalydendeVerdi
namespace: regnskap-no
period_type: instant
data_type: decimalItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Pålydende verdi per aksje"
  - lang: en
    role: standardLabel
    text: "Par value per share"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-42"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:ParValuePerShare
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-42)

> Pålydende verdi per aksje
