---
concept_id: regnskap-no:AnnenInnskuttEgenkapital
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Annen innskutt egenkapital"
  - lang: en
    role: standardLabel
    text: "Other contributed equity"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 C I 3"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "C. Egenkapital — I. Innskutt egenkapital — 3. Annen innskutt egenkapital"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 C I 3"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Norwegian-specific equity component without IFRS-Full equivalent."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:InnskuttEgenkapital
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-2 C I 3)

> Annen innskutt egenkapital
