---
concept_id: regnskap-no:Gjeld
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
    text: "Gjeld"
  - lang: en
    role: standardLabel
    text: "Liabilities"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:Liabilities
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 6-2 D)

> Gjeld
