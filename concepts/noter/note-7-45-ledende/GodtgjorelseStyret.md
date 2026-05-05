---
concept_id: regnskap-no:GodtgjorelseStyret
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
    text: "Godtgjørelse til styret"
  - lang: en
    role: standardLabel
    text: "Compensation - board of directors"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-45"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:KeyManagementPersonnelCompensation
    relation: skos:closeMatch
    quality: approximate
    note: "Total compensation to board members; IFRS aggregates with key-management-personnel disclosure."
---

## Verbatim text (regnskapsloven § 7-45)

> Godtgjørelse til styret
