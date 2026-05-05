---
concept_id: regnskap-no:AvskrivningVarigeDriftsmidlerOgImmaterielleEiendeler
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
    text: "Avskrivning på varige driftsmidler og immaterielle eiendeler"
  - lang: en
    role: standardLabel
    text: "Depreciation and amortisation expense"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 7"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:DepreciationAndAmortisationExpense
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:Driftsresultat
    weight: -1
    order: 7
---

## Verbatim text (regnskapsloven § 6-1 (1) post 7)

> 7. Avskrivning på varige driftsmidler og immaterielle eiendeler
