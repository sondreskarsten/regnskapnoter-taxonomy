---
concept_id: regnskap-no:AnnenDriftskostnad
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
    text: "Annen driftskostnad"
  - lang: en
    role: standardLabel
    text: "Other operating expenses"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 9"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:OtherExpenseByNature
    relation: skos:closeMatch
    quality: approximate
    note: "ifrs-full:OtherExpenseByNature er klassifisering etter art; § 6-1 post 9 er restposten i artsoppstillingen."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:Driftsresultat
    weight: -1
    order: 9
---

## Verbatim text (regnskapsloven § 6-1 (1) post 9)

> 9. Annen driftskostnad
