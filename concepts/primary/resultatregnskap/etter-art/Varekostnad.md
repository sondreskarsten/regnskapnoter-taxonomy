---
concept_id: regnskap-no:Varekostnad
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
    text: "Varekostnad"
  - lang: en
    role: standardLabel
    text: "Cost of goods"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 5"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:RawMaterialsAndConsumablesUsed
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk varekostnad inkluderer både innkjøpte varer og rå- og hjelpestoffer; mappes til IFRS-Full RawMaterialsAndConsumablesUsed med mindre granularitet."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:Driftsresultat
    weight: -1
    order: 5
---

## Verbatim text (regnskapsloven § 6-1 (1) post 5)

> 5. Varekostnad
