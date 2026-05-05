---
concept_id: regnskap-no:TomterBygningerOgAnnenFastEiendom
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
    text: "Tomter, bygninger og annen fast eiendom"
  - lang: en
    role: standardLabel
    text: "Land, buildings and other real property"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A II 1"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "A. Anleggsmidler / II."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 A II 1"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:LandAndBuildings
    relation: skos:closeMatch
    quality: approximate
    note: "regnskap-no aggregates land + buildings + other real property; IFRS-Full splits land vs buildings."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:VarigeDriftsmidler
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 A II 1)

> Tomter, bygninger og annen fast eiendom
