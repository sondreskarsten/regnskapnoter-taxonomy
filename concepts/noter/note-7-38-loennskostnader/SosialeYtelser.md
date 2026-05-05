---
concept_id: regnskap-no:SosialeYtelser
namespace: regnskap-no
period_type: duration
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Sosiale ytelser"
  - lang: en
    role: standardLabel
    text: "Social benefits"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-38"
    applicable_from_fiscal_year: 1999

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Andre sosiale kostnader utenom folketrygdavgift og pensjon."

parents:
  - role: "[710380] Note 7-38 Antall ansatte og lønnskostnader"
    parent: regnskap-no:Lonnskostnad
    weight: +1
    order: 5
---

## Verbatim text (regnskapsloven § 7-38)

> Sosiale ytelser
