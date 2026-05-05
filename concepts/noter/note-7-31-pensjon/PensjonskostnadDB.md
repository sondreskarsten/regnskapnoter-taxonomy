---
concept_id: regnskap-no:PensjonskostnadDB
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
    text: "Pensjonskostnad ytelsesordning"
  - lang: en
    role: standardLabel
    text: "Pension cost - defined benefit"

references:
  - publisher: NRS
    document: NRS 6
    paragraph: "kap. 5"
    applicable_from_fiscal_year: 2007
mappings:
  - to: ifrs-full:PostemploymentBenefitExpenseDefinedBenefitPlans
    relation: skos:closeMatch
    quality: approximate
    note: "NRS 6 defined-benefit pension cost; IFRS IAS 19 uses different actuarial framework."
---

## Verbatim text (NRS 6 kap. 5)

> Pensjonskostnad ytelsesordning
