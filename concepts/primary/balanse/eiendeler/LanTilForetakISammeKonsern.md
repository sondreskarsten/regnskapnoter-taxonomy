---
concept_id: regnskap-no:LanTilForetakISammeKonsern
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
    text: "Lån til foretak i samme konsern"
  - lang: en
    role: standardLabel
    text: "Loans to group enterprises"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A III 3"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "A. Anleggsmidler / III."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 A III 3"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Inter-company loans (same group); IFRS aggregates under financial assets."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:FinansielleAnleggsmidler
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-2 A III 3)

> Lån til foretak i samme konsern
