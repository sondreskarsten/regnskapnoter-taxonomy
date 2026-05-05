---
concept_id: regnskap-no:RentekostnadForetakSammeKonsernFunksjon
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
    text: "Rentekostnad til foretak i samme konsern"
  - lang: en
    role: standardLabel
    text: "Interest expense to group entities"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 10"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:InterestExpense
    relation: skos:closeMatch
    quality: approximate
    note: "Samme begrep som § 6-1 post 17."

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:ResultatForSkattekostnadFunksjon
    weight: -1
    order: 10
---

## Verbatim text (regnskapsloven § 6-1a (1) post 10)

> 10. Rentekostnad til foretak i samme konsern
