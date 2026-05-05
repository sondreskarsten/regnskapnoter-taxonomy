---
concept_id: regnskap-no:FremforbartUnderskudd
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
    text: "Fremførbart underskudd"
  - lang: en
    role: standardLabel
    text: "Carry-forward losses"

references:
  - publisher: Stortinget
    document: skatteloven
    paragraph: "§ 14-6"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:UnusedTaxLossesForWhichNoDeferredTaxAssetRecognised
    relation: skos:closeMatch
    quality: approximate
    note: "Norwegian unused tax losses; IFRS reports recognized vs unrecognized split."
---

## Verbatim text (skatteloven § 14-6)

> Fremførbart underskudd
