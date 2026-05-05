---
concept_id: regnskap-no:AnnenKortsiktigGjeld
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
    text: "Annen kortsiktig gjeld"
  - lang: en
    role: standardLabel
    text: "Other current liabilities"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D III 8"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:OtherCurrentPayables
    relation: skos:closeMatch
    quality: approximate
    note: "Other accrued and short-term liabilities."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:KortsiktigGjeld
    weight: +1
    order: 8
---

## Verbatim text (regnskapsloven § 6-2 D III 8)

> Annen kortsiktig gjeld
