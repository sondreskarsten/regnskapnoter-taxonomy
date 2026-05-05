---
concept_id: regnskap-no:LonnskostnadAndreYtelser
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
    text: "Andre ytelser"
  - lang: en
    role: standardLabel
    text: "Other employee benefits"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-38"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:OtherEmployeeExpense
    relation: skos:closeMatch
    quality: approximate
    note: "'Andre ytelser' aggregates fringe benefits and other employee costs; IFRS uses OtherEmployeeExpense at similar grain."
parents:
  - role: "[710000] Note 7-38 Lønnskostnader"
    parent: regnskap-no:Lonnskostnad
    weight: +1
    order: 4
---

## Verbatim text (regnskapsloven § 7-38)

> Andre ytelser
