---
concept_id: regnskap-no:ImmaterielleEiendeler
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
    text: "Immaterielle eiendeler"
  - lang: en
    role: standardLabel
    text: "Intangible assets"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A I"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "A. Anleggsmidler — I. Immaterielle eiendeler"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 A I"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:IntangibleAssetsOtherThanGoodwill
    relation: skos:closeMatch
    quality: approximate
    note: "Includes goodwill in regnskap-no decomposition; IFRS separates goodwill."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Anleggsmidler
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 A I)

> Immaterielle eiendeler
