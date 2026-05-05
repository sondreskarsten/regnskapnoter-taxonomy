---
concept_id: regnskap-no:AndreFordringer
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
    text: "Other receivables"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A III 7"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NoncurrentReceivables
    relation: skos:closeMatch
    quality: approximate
    note: "Long-term other receivables; IFRS uses 12-month split."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:FinansielleAnleggsmidler
    weight: +1
    order: 7
---

## Verbatim text (regnskapsloven § 6-2 A III 7)

> Andre fordringer
