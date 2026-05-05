---
concept_id: regnskap-no:AnnenFinansinntekt
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
    text: "Annen finansinntekt"
  - lang: en
    role: standardLabel
    text: "Other finance income"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 14"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:FinanceIncome
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konseptet er post 14 (residual finansinntekt etter konserninterne renter, datter/tilknyttet utbytte, og andre investeringsinntekter)."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:ResultatForSkattekostnad
    weight: +1
    order: 14
---

## Verbatim text (regnskapsloven § 6-1 (1) post 14)

> 14. Annen finansinntekt
