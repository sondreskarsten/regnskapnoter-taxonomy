---
concept_id: regnskap-no:KortsiktigGjeld
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
    text: "Kortsiktig gjeld"
  - lang: en
    role: standardLabel
    text: "Current liabilities"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D III"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "D. Gjeld — III. Kortsiktig gjeld"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 D III"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:CurrentLiabilities
    relation: skos:closeMatch
    quality: approximate
    note: "Aggregation of current liabilities."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Gjeld
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-2 D III)

> Kortsiktig gjeld
