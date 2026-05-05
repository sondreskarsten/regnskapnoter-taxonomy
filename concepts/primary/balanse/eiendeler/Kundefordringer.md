---
concept_id: regnskap-no:Kundefordringer
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
    text: "Kundefordringer"
  - lang: en
    role: standardLabel
    text: "Trade receivables"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 B II 1"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "B. Omløpsmidler / II."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 B II 1"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:TradeAndOtherCurrentReceivables
    relation: skos:closeMatch
    quality: approximate
    note: "regnskap-no separates customer receivables; IFRS aggregates trade and other."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Fordringer
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 B II 1)

> Kundefordringer
