---
concept_id: regnskap-no:SkattepliktigInntekt
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Skattepliktig inntekt"
  - lang: en
    role: standardLabel
    text: "Taxable income"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-29"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:CurrentTaxExpenseIncome
    relation: skos:closeMatch
    quality: approximate
    note: "Taxable profit basis; IFRS reports current tax expense."
---

## Verbatim text (regnskapsloven § 7-29)

> Skattepliktig inntekt
