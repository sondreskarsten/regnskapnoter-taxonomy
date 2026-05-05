---
concept_id: regnskap-no:GodtgjorelseDagligLeder
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
    text: "Godtgjørelse til daglig leder"
  - lang: en
    role: standardLabel
    text: "Compensation - CEO"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-45"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:KeyManagementPersonnelCompensationShorttermEmployeeBenefits
    relation: skos:closeMatch
    quality: approximate
    note: "Total compensation to CEO; IFRS uses key-management-personnel disclosure with similar grain."
---

## Verbatim text (regnskapsloven § 7-45)

> Godtgjørelse til daglig leder
