---
concept_id: regnskap-no:EndringUtsattSkattefordel
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
    text: "Endring i utsatt skattefordel"
  - lang: en
    role: standardLabel
    text: "Change in deferred tax asset"

references:
  - publisher: NRS
    document: Resultatskatt
    paragraph: "kap. 5"
    applicable_from_fiscal_year: 2014
mappings:
  - to: ifrs-full:DeferredTaxIncomeExpense
    relation: skos:closeMatch
    quality: approximate
    note: "Period change in deferred tax asset; IFRS reports as deferred tax expense or income."
---

## Verbatim text (NRS(F) Resultatskatt kap. 5)

> Endring i utsatt skattefordel
