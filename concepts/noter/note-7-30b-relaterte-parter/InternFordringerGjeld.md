---
concept_id: regnskap-no:InternFordringerGjeld
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Interne fordringer og gjeld"
  - lang: en
    role: standardLabel
    text: "Inter-company receivables and payables"

references:
  - publisher: NRS
    document: NRS 21
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2009
mappings:
  - to: ifrs-full:RelatedPartyTransactionsAxis
    relation: skos:closeMatch
    quality: approximate
    note: "Inter-company balances disclosed under § 7-30b; IFRS uses IAS 24 related parties."
---

## Verbatim text (NRS 21 kap. 4)

> Interne fordringer og gjeld
