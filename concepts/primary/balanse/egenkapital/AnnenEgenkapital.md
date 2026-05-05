---
concept_id: regnskap-no:AnnenEgenkapital
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Annen egenkapital"
  - lang: en
    role: standardLabel
    text: "Other equity"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 C II 1"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:RetainedEarnings
    relation: skos:closeMatch
    quality: approximate
    note: "regnskap-no 'annen egenkapital' broadly equivalent to retained earnings; IFRS distinguishes reserves."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:OpptjentEgenkapital
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 C II 1)

> Annen egenkapital
