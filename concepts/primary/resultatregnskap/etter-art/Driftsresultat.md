---
concept_id: regnskap-no:Driftsresultat
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
    text: "Driftsresultat"
  - lang: en
    role: standardLabel
    text: "Operating profit (loss)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 10"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:ProfitLossFromOperatingActivities
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk driftsresultat er definert som sum post 1-9; ifrs-full:ProfitLossFromOperatingActivities har samme rolle men IFRS' Operating-tema er ikke standardisert."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:ResultatForSkattekostnad
    weight: +1
    order: 10
---

## Verbatim text (regnskapsloven § 6-1 (1) post 10)

> 10. Driftsresultat
