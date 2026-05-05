---
concept_id: regnskap-no:InvesteringerIAnnetForetakSammeKonsern
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
    text: "Investeringer i annet foretak i samme konsern"
  - lang: en
    role: standardLabel
    text: "Investments in other group enterprises"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A III 2"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "A. Anleggsmidler — III. Finansielle anleggsmidler — 2. Investeringer i annet foretak i samme konsern"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 A III 2"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Sister-company investments in same group; IFRS does not segregate this category."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:FinansielleAnleggsmidler
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 6-2 A III 2)

> Investeringer i annet foretak i samme konsern
