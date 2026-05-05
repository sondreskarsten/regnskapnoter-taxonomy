---
concept_id: regnskap-no:Kassekreditt
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
    text: "Kassekreditt"
  - lang: en
    role: standardLabel
    text: "Bank overdraft (current account credit line)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-21"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:BankBalancesAtCentralBanksOtherThanMandatoryReserveDeposits
    relation: skos:closeMatch
    quality: approximate
    note: "Available overdraft facility; IFRS treats as financing activity in cash flow."
---

## Verbatim text (regnskapsloven § 7-21)

> Kassekreditt
