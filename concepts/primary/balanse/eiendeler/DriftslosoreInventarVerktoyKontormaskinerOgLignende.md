---
concept_id: regnskap-no:DriftslosoreInventarVerktoyKontormaskinerOgLignende
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
    text: "Driftsløsøre, inventar, verktøy, kontormaskiner og lignende"
  - lang: en
    role: standardLabel
    text: "Operating equipment, fixtures, tools, office machinery and similar"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A II 4"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "A. Anleggsmidler — II. Varige driftsmidler — 4. Driftsløsøre, inventar, verktøy, kontormaskiner og lignende"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 A II 4"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:OfficeEquipmentNetOfAccumulatedDepreciationAndAmortisationAndImpairment
    relation: skos:closeMatch
    quality: approximate
    note: "Aggregation of moveable operating assets."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:VarigeDriftsmidler
    weight: +1
    order: 4
---

## Verbatim text (regnskapsloven § 6-2 A II 4)

> Driftsløsøre, inventar, verktøy, kontormaskiner og lignende
