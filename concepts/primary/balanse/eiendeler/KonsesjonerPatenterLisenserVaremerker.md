---
concept_id: regnskap-no:KonsesjonerPatenterLisenserVaremerker
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
    text: "Konsesjoner, patenter, lisenser, varemerker og lignende rettigheter"
  - lang: en
    role: standardLabel
    text: "Concessions, patents, licences, trademarks and similar rights"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A I 2"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "A. Anleggsmidler — I. Immaterielle eiendeler — 2. Konsesjoner, patenter, lisenser, varemerker og lignende rettigheter"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 A I 2"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:LicencesAndFranchises
    relation: skos:closeMatch
    quality: approximate
    note: "IFRS-Full splits these across multiple line items; regnskap-no aggregates per regnskapsloven."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:ImmaterielleEiendeler
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 6-2 A I 2)

> Konsesjoner, patenter, lisenser, varemerker og lignende rettigheter
