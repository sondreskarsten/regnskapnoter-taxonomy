---
concept_id: regnskap-no:PensjonskostnadDC
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
    text: "Pensjonskostnad innskuddsordning"
  - lang: en
    role: standardLabel
    text: "Pension cost - defined contribution"

references:
  - publisher: NRS
    document: NRS 6
    paragraph: "kap. 5"
    applicable_from_fiscal_year: 2007
mappings:
  - to: ifrs-full:PostemploymentBenefitExpenseDefinedContributionPlans
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (NRS 6 kap. 5)

> Pensjonskostnad innskuddsordning
