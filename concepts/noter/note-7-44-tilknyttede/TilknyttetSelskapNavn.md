---
concept_id: regnskap-no:TilknyttetSelskapNavn
namespace: regnskap-no
period_type: instant
data_type: stringItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Tilknyttet selskap - navn"
  - lang: en
    role: standardLabel
    text: "Associate - name"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:NameOfAssociate
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-44)

> Tilknyttet selskap - navn
