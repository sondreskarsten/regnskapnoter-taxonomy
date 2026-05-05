---
concept_id: regnskap-no:EstimertGjenvarendeTap
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
    text: "Estimert gjenvarende tap"
  - lang: en
    role: standardLabel
    text: "Estimated remaining loss"

references:
  - publisher: NRS
    document: NRS 2
    paragraph: "kap. 3"
    applicable_from_fiscal_year: 2003
mappings:
  - to: ifrs-full:OnerousContractsProvision
    relation: skos:closeMatch
    quality: approximate
    note: "Estimated future loss on ongoing contract; IFRS uses onerous-contract provision."
---

## Verbatim text (NRS 2 kap. 3)

> Estimert gjenvarende tap
