---
concept_id: regnskap-no:DriftsinntektVirksomhetsomraade
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
    text: "Driftsinntekter fordelt på virksomhetsområde"
  - lang: en
    role: standardLabel
    text: "Operating revenue by business segment"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-7"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Sammenslåing av poster i oppstillingsplanen (1) Poster i oppstillingsplanen som er slått sammen etter § 6-3 annet ledd, skal spesifiseres. (2) § 6-6 om sammenligningstall gjelder tilsvarende."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-7"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:RevenueFromContractsWithCustomers
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk § 7-7 krever fordeling per virksomhetsområde og geografi; ifrs-full har separate IFRS 8 segmentkonsepter."
---

## Verbatim text (regnskapsloven § 7-7)

> Driftsinntekter fordelt på virksomhetsområde
