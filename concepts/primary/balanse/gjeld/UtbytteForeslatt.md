---
concept_id: regnskap-no:UtbytteForeslatt
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: deprecated
deprecated_date: "2021-01-01"
deprecated_replacement: regnskap-no:UtbytteForeslattBelop
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Utbytte"
  - lang: en
    role: standardLabel
    text: "Proposed dividend"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D III 7"
    applicable_from_fiscal_year: 1999
    applicable_to_fiscal_year: 2020

definitions:
  - lang: nb
    role: definition
    text: "D. Gjeld — III. Kortsiktig gjeld"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 D III 7"
    applicable_from_fiscal_year: 1999
    applicable_to_fiscal_year: 2020
    applicable_to_fiscal_year: 2020
    authoritative: true

mappings:
  - to: ifrs-full:DividendsPayable
    relation: skos:closeMatch
    quality: approximate
    note: "Proposed dividend before AGM approval; under NGAAP recognized as liability per styrebehandling, IFRS recognizes only when declared."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:KortsiktigGjeld
    weight: +1
    order: 7
---

## Verbatim text (regnskapsloven § 6-2 D III 7)

> Utbytte
