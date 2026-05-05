---
concept_id: regnskap-no:AnnenFinanskostnadFunksjon
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
    paragraph: "§ 6-1a (1) post 12"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:FinanceCosts
    relation: skos:closeMatch
    quality: approximate
    note: "Samme begrep som § 6-1 post 18."

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:ResultatForSkattekostnadFunksjon
    weight: -1
    order: 12
---

## Verbatim text (regnskapsloven § 6-1a (1) post 12)

> 12. Annen finanskostnad
