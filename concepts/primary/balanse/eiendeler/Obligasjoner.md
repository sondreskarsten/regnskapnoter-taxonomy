---
concept_id: regnskap-no:Obligasjoner
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
    text: "Obligasjoner"
  - lang: en
    role: standardLabel
    text: "Bonds"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A III 6"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "A. Anleggsmidler — III. Finansielle anleggsmidler — 6. Investeringer i aksjer og andeler"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 A III 6"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:NoncurrentInvestmentsInBonds
    relation: skos:closeMatch
    quality: approximate
    note: "Long-term bond investments classified as anleggsmiddel."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:FinansielleAnleggsmidler
    weight: +1
    order: 6
---

## Verbatim text (regnskapsloven § 6-2 A III 6)

> Obligasjoner
