---
concept_id: regnskap-no:DriftsresultatFunksjon
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
    paragraph: "§ 6-1a (1) post 6"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:ProfitLossFromOperatingActivities
    relation: skos:closeMatch
    quality: approximate
    note: "Samme begrep som § 6-1 post 10, men summert i funksjonsoppstillingen."

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:ResultatForSkattekostnadFunksjon
    weight: +1
    order: 6
---

## Verbatim text (regnskapsloven § 6-1a (1) post 6)

> 6. Driftsresultat
