---
concept_id: regnskap-no:EndringMidlertidigeForskjeller
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
    text: "Endring i midlertidige forskjeller"
  - lang: en
    role: standardLabel
    text: "Change in temporary differences"

references:
  - publisher: NRS
    document: Resultatskatt
    paragraph: "kap. 5"
    applicable_from_fiscal_year: 2014
mappings:
  - to: ifrs-full:DeferredTaxExpenseIncomeRelatingToOriginationAndReversalOfTemporaryDifferences
    relation: skos:closeMatch
    quality: approximate
    note: "Period change in book-tax differences; IFRS reports as deferred tax expense."
---

## Verbatim text (NRS(F) Resultatskatt kap. 5)

> Endring i midlertidige forskjeller
