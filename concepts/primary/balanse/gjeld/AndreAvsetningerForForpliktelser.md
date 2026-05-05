---
concept_id: regnskap-no:AndreAvsetningerForForpliktelser
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
    text: "Andre avsetninger for forpliktelser"
  - lang: en
    role: standardLabel
    text: "Other provisions for liabilities"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D I 3"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:OtherProvisions
    relation: skos:closeMatch
    quality: approximate
    note: "Other provisions; aggregation under NRS 13."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:AvsetningForForpliktelser
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-2 D I 3)

> Andre avsetninger for forpliktelser
