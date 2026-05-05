---
concept_id: regnskap-no:AntallAnsatte
namespace: regnskap-no
period_type: duration
data_type: integerItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Antall ansatte"
  - lang: en
    role: standardLabel
    text: "Number of employees"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-38"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:NumberOfEmployees
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-38)

> Antall ansatte
