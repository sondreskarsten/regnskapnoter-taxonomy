---
concept_id: regnskap-no:GodtgjorelseRevisorSkatterad
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
    text: "Godtgjørelse revisor skatterådgivning"
  - lang: en
    role: standardLabel
    text: "Audit fees — tax advisory"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-31a"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:FeesPaidToAuditorTaxServices
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-31a)

> Godtgjørelse revisor skatterådgivning
