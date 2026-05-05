---
concept_id: regnskap-no:AnnenFinanskostnad
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
    text: "Annen finanskostnad"
  - lang: en
    role: standardLabel
    text: "Other finance costs"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 18"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "18. Annen finanskostnad"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1 (1) post 18"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:FinanceCosts
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konseptet er post 18 (residual finanskostnad etter konserninterne renter og nedskrivninger)."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:ResultatForSkattekostnad
    weight: -1
    order: 18
---

## Verbatim text (regnskapsloven § 6-1 (1) post 18)

> 18. Annen finanskostnad
