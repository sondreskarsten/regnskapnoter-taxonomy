---
concept_id: regnskap-no:SumMidlertidigeForskjeller
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
    text: "Sum midlertidige forskjeller"
  - lang: en
    role: standardLabel
    text: "Total temporary differences"

references:
  - publisher: NRS
    document: Resultatskatt
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2014
mappings:
  - to: ifrs-full:DeferredTaxExpenseIncomeRelatingToOriginationAndReversalOfTemporaryDifferences
    relation: skos:closeMatch
    quality: approximate
    note: "Total of temporary book-tax differences before considering carry-forward losses."
---

## Verbatim text (NRS(F) Resultatskatt kap. 4)

> Sum midlertidige forskjeller
