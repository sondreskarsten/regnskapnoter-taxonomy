---
concept_id: regnskap-no:ForskuddsfakturertProduksjon
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
    text: "Forskuddsfakturert produksjon"
  - lang: en
    role: standardLabel
    text: "Pre-invoiced production"

references:
  - publisher: NRS
    document: NRS 2
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2003
definitions:
  - lang: nb
    role: definition
    text: "4. Begrepet anleggskontrakt gjelder ikke utelukkende det som i dagligtale omtales som anleggsvirksomhet (for eksempel bygging av vei eller tunnel), men også andre byggeoppdrag, skipsbygging og tilvirkning av store og komplekse produk- ter eller leveranser. Kontraktsfestet tjenesteyting knyttet til anleggsvirksomhet, eksempelvis byggeledelse, teknisk assistanse eller arkitektoppdrag, omfattes også."
    source_publisher: NRS
    source_document: NRS 2
    source_paragraph: "kap. 4"
    applicable_from_fiscal_year: 2003
    authoritative: true

mappings:
  - to: ifrs-full:ContractLiabilities
    relation: skos:closeMatch
    quality: approximate
    note: "Invoiced amounts in excess of work performed; IFRS uses contract liabilities per IFRS 15."
---

## Verbatim text (NRS 2 kap. 4)

> Forskuddsfakturert produksjon
