---
concept_id: regnskap-no:InternSalgsinntekterVarekostnad
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
    text: "Interne salgsinntekter og varekostnad"
  - lang: en
    role: standardLabel
    text: "Inter-company sales and COGS"

references:
  - publisher: NRS
    document: NRS 21
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2009
mappings:
  - to: ifrs-full:RelatedPartyTransactionsAxis
    relation: skos:closeMatch
    quality: approximate
    note: "Inter-company P&L flows; IFRS uses IAS 24 related-party transaction disclosures."
---

## Verbatim text (NRS 21 kap. 4)

> Interne salgsinntekter og varekostnad
