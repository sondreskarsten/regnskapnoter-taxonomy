---
concept_id: regnskap-no:DatterselskapEgenkapitalverdi
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
    text: "Datterselskaps egenkapitalverdi"
  - lang: en
    role: standardLabel
    text: "Subsidiary equity value"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-15"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:Equity
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept er datterselskaps EK fra et morselskaps perspektiv; ifrs-full Equity er konsoliderte totaler."
---

## Verbatim text (regnskapsloven § 7-15)

> Datterselskaps egenkapitalverdi
