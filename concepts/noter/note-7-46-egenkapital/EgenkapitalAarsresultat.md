---
concept_id: regnskap-no:EgenkapitalAarsresultat
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
    text: "Årsresultat (egenkapital)"
  - lang: en
    role: standardLabel
    text: "Profit (loss) recognised in equity"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:ProfitLoss
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-46)

> Årsresultat (egenkapital)
