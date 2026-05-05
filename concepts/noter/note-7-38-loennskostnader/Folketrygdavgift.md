---
concept_id: regnskap-no:Folketrygdavgift
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
    text: "Folketrygdavgift"
  - lang: en
    role: standardLabel
    text: "Social security contributions"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-38"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:SocialSecurityContributions
    relation: skos:exactMatch
    quality: exact
parents:
  - role: "[710000] Note 7-38 Lønnskostnader"
    parent: regnskap-no:Lonnskostnad
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 7-38)

> Folketrygdavgift
