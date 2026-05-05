---
concept_id: regnskap-no:OpptjentIkkeFakturert
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
    text: "Opptjent ikke fakturert produksjon"
  - lang: en
    role: standardLabel
    text: "Recognized but uninvoiced production"

references:
  - publisher: NRS
    document: NRS 2
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2003
mappings:
  - to: ifrs-full:ContractAssets
    relation: skos:closeMatch
    quality: approximate
    note: "Work performed but not yet invoiced; IFRS uses contract assets per IFRS 15."
---

## Verbatim text (NRS 2 kap. 4)

> Opptjent ikke fakturert produksjon
