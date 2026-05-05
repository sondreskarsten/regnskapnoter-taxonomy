---
concept_id: regnskap-no:EffektivSkattesats
namespace: regnskap-no
period_type: duration
balance: null
data_type: percentItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Effektiv skattesats"
  - lang: en
    role: standardLabel
    text: "Effective tax rate"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-23"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:AverageEffectiveTaxRate
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-23)

> Effektiv skattesats
