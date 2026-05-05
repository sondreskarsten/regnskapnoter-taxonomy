---
concept_id: regnskap-no:Resultatregnskap
namespace: regnskap-no
period_type: duration
balance: null
data_type: stringItemType
substitution_group: item
abstract: true
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Resultatregnskap"
  - lang: en
    role: standardLabel
    text: "Income statement"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:IncomeStatementAbstract
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk resultatregnskap i § 6-1 / § 6-1a følger en oppstillingsplan; IFRS-Full ifrs-full:IncomeStatementAbstract er et abstrakt grupperingskonsept uten en obligatorisk oppstillingsplan."
---

## Verbatim text (regnskapsloven § 6-1)

> Oppstillingsplan for resultatregnskap.
