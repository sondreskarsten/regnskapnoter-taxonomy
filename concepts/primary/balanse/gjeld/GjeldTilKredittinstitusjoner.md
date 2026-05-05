---
concept_id: regnskap-no:GjeldTilKredittinstitusjoner
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
    text: "Gjeld til kredittinstitusjoner"
  - lang: en
    role: standardLabel
    text: "Debt to credit institutions"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D II 3"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "D. Gjeld — II. Annen langsiktig gjeld — 3. Gjeld til kredittinstitusjoner"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 D II 3"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:NoncurrentBorrowings
    relation: skos:closeMatch
    quality: approximate
    note: "Bank loans and similar."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:AnnenLangsiktigGjeld
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-2 D II 3)

> Gjeld til kredittinstitusjoner
