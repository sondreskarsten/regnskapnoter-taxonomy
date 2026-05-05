---
concept_id: regnskap-no:BankinnskuddTotal
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Bankinnskudd totalt"
  - lang: en
    role: standardLabel
    text: "Total bank deposits"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-21"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:CashAndCashEquivalents
    relation: skos:closeMatch
    quality: approximate
    note: "Aggregate bank deposit balance; substantially equivalent to IFRS cash and equivalents."
---

## Verbatim text (regnskapsloven § 7-21)

> Bankinnskudd totalt
