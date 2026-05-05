---
concept_id: regnskap-no:PensjonsforpliktelserNetto
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
    text: "Pensjonsforpliktelser netto"
  - lang: en
    role: standardLabel
    text: "Net pension obligation"

references:
  - publisher: NRS
    document: NRS 6
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2007
mappings:
  - to: ifrs-full:NetDefinedBenefitLiabilityAsset
    relation: skos:closeMatch
    quality: approximate
    note: "NRS 6 net pension liability; IFRS IAS 19 uses different actuarial framework."
---

## Verbatim text (NRS 6 kap. 4)

> Pensjonsforpliktelser netto
