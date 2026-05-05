---
concept_id: regnskap-no:VarerNedskrivningBelop
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
    text: "Nedskrivning av varer"
  - lang: en
    role: standardLabel
    text: "Inventory write-down"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-10"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Varer Varer skal spesifiseres på råvarer, varer under tilvirkning og ferdigvarer. § 6-6 om sammenligningstall gjelder tilsvarende."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-10"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:WritedownsReversalsOfInventories
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konseptet er bare nedskrivning; ifrs-full inkluderer både nedskrivning og reverseringer."
---

## Verbatim text (regnskapsloven § 7-10)

> Nedskrivning av varer
