---
concept_id: regnskap-no:RenteinntektForetakSammeKonsernFunksjon
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Renteinntekt fra foretak i samme konsern"
  - lang: en
    role: standardLabel
    text: "Interest income from group entities"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 9"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "9. Renteinntekt fra foretak i samme konsern"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1a (1) post 9"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:InterestIncomeOnLoansAndReceivables
    relation: skos:closeMatch
    quality: approximate
    note: "Samme begrep som § 6-1 post 13."

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:ResultatForSkattekostnadFunksjon
    weight: +1
    order: 9
---

## Verbatim text (regnskapsloven § 6-1a (1) post 9)

> 9. Renteinntekt fra foretak i samme konsern
