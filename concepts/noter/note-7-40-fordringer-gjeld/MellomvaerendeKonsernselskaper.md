---
concept_id: regnskap-no:MellomvaerendeKonsernselskaper
namespace: regnskap-no
period_type: instant
balance: null
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Mellomværende med konsernselskaper"
  - lang: en
    role: standardLabel
    text: "Intra-group balances"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:DueFromRelatedParties
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept inkluderer både fordringer og gjeld; ifrs-full splitter i to."

---

## Verbatim text (regnskapsloven § 7-40)

> Mellomværende med konsernselskaper
