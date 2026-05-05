---
concept_id: regnskap-no:AnnenLangsiktigGjeld
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
    text: "Annen langsiktig gjeld"
  - lang: en
    role: standardLabel
    text: "Other non-current liabilities"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D II"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NoncurrentLiabilities
    relation: skos:closeMatch
    quality: approximate
    note: "Non-current liabilities other than provisions; aggregation differs from IFRS classification."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Gjeld
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 6-2 D II)

> Annen langsiktig gjeld
