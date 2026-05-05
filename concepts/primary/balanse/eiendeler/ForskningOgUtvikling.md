---
concept_id: regnskap-no:ForskningOgUtvikling
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
    text: "Forskning og utvikling"
  - lang: en
    role: standardLabel
    text: "Research and development"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A I 1"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:IntangibleAssetsAndGoodwill
    relation: skos:relatedMatch
    quality: approximate
    note: "Norwegian 'forskning og utvikling' line aggregates capitalized R&D; IFRS distinguishes development phase (IAS 38.57)."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:ImmaterielleEiendeler
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 A I 1)

> Forskning og utvikling
