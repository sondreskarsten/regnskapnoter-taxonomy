---
concept_id: regnskap-no:SkattekostnadBetalbarBelop
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
    text: "Betalbar skatt"
  - lang: en
    role: standardLabel
    text: "Current tax expense"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-23"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:CurrentTaxExpenseIncome
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-23)

> Betalbar skatt
