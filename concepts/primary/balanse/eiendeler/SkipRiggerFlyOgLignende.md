---
concept_id: regnskap-no:SkipRiggerFlyOgLignende
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
    text: "Skip, rigger, fly o.l."
  - lang: en
    role: standardLabel
    text: "Ships, rigs, aircraft and similar"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A II 3"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "A. Anleggsmidler / II."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 A II 3"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Industry-specific aggregation (shipping, offshore, aviation); no exact IFRS-Full equivalent."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:VarigeDriftsmidler
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-2 A II 3)

> Skip, rigger, fly o.l.
