---
concept_id: regnskap-no:InntektsfortIgangv
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Inntektsført løpende (igangv. kontrakter)"
  - lang: en
    role: standardLabel
    text: "Recognized revenue (ongoing contracts)"

references:
  - publisher: NRS
    document: NRS 2
    paragraph: "kap. 3"
    applicable_from_fiscal_year: 2003
mappings:
  - to: ifrs-full:RevenueFromConstructionContracts
    relation: skos:closeMatch
    quality: approximate
    note: "NRS 2 percentage-of-completion revenue; IFRS 15 over-time revenue recognition."
---

## Verbatim text (NRS 2 kap. 3)

> Inntektsført løpende (igangv. kontrakter)
