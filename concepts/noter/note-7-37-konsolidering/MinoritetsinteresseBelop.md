---
concept_id: regnskap-no:MinoritetsinteresseBelop
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
    text: "Minoritetsinteresse beløp"
  - lang: en
    role: standardLabel
    text: "Non-controlling interest amount"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-37"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NoncontrollingInterests
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-37)

> Minoritetsinteresse beløp
