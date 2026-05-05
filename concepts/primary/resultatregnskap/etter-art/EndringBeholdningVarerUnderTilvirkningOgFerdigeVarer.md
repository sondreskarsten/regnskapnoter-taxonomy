---
concept_id: regnskap-no:EndringBeholdningVarerUnderTilvirkningOgFerdigeVarer
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
    text: "Endring i beholdning av varer under tilvirkning og ferdig tilvirkede varer"
  - lang: en
    role: standardLabel
    text: "Changes in inventories of finished goods and work in progress"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 3"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "3. Endring i beholdning av varer under tilvirkning og ferdig tilvirkede varer"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1 (1) post 3"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ChangesInInventoriesOfFinishedGoodsAndWorkInProgress
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:Driftsresultat
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-1 (1) post 3)

> 3. Endring i beholdning av varer under tilvirkning og ferdig tilvirkede varer
