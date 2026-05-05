---
concept_id: regnskap-no:AndreFordringerKortsiktig
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
    text: "Andre fordringer"
  - lang: en
    role: standardLabel
    text: "Other receivables (current)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 B II 2"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "B. Omløpsmidler / II."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 B II 2"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:OtherCurrentReceivables
    relation: skos:closeMatch
    quality: approximate
    note: "Other current receivables."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Fordringer
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 6-2 B II 2)

> Andre fordringer
