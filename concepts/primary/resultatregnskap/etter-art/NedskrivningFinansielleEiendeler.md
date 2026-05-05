---
concept_id: regnskap-no:NedskrivningFinansielleEiendeler
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
    text: "Nedskrivning av finansielle eiendeler"
  - lang: en
    role: standardLabel
    text: "Impairment of financial assets"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 16"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:ImpairmentLossOnFinancialAssets
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:ResultatForSkattekostnad
    weight: -1
    order: 16
---

## Verbatim text (regnskapsloven § 6-1 (1) post 16)

> 16. Nedskrivning av finansielle eiendeler
