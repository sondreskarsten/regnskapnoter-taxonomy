---
concept_id: regnskap-no:LonnskostnadPensjon
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
    text: "Pensjonskostnader"
  - lang: en
    role: standardLabel
    text: "Pension costs"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-38"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:PostemploymentBenefitExpenseDefinedBenefitPlans
    relation: skos:closeMatch
    quality: approximate
    note: "NRS 6 pensjonskostnad covers both DB and DC; IFRS-Full splits."
parents:
  - role: "[710000] Note 7-38 Lønnskostnader"
    parent: regnskap-no:Lonnskostnad
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 7-38)

> Pensjonskostnader
