---
concept_id: regnskap-no:PresentasjonsvalutaStore
namespace: regnskap-no
period_type: duration
balance: null
data_type: stringItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Presentasjonsvaluta"
  - lang: en
    role: standardLabel
    text: "Presentation currency"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-2"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:DescriptionOfPresentationCurrency
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-2)

> Presentasjonsvaluta
