---
concept_id: regnskap-no:KontingentForpliktelseBelop
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
    text: "Kontingent forpliktelse - beløp"
  - lang: en
    role: standardLabel
    text: "Contingent liability - amount"

references:
  - publisher: NRS
    document: NRS 13
    paragraph: "kap. 5"
    applicable_from_fiscal_year: 2003
mappings:
  - to: ifrs-full:ContingentLiabilitiesContingentLiabilityAtMeasurement
    relation: skos:closeMatch
    quality: approximate
    note: "Best estimate of contingent liability; IFRS uses IAS 37 with similar definition."
---

## Verbatim text (NRS 13 kap. 5)

> Kontingent forpliktelse - beløp
