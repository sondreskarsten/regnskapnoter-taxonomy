---
concept_id: regnskap-no:GarantiansvarTotaltBelop
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
    text: "Garantiansvar - totalt beløp"
  - lang: en
    role: standardLabel
    text: "Guarantees - total amount"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40 (3)"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:ContingentLiabilitiesContingentLiabilityAtMeasurement
    relation: skos:closeMatch
    quality: approximate
    note: "NRS 13 financial guarantees; IFRS uses IAS 37 contingent liabilities."
---

## Verbatim text (regnskapsloven § 7-40 (3))

> Garantiansvar - totalt beløp
