---
concept_id: regnskap-no:AvsetningForForpliktelser
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
    text: "Avsetning for forpliktelser"
  - lang: en
    role: standardLabel
    text: "Provisions for liabilities"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D I"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:Provisions
    relation: skos:closeMatch
    quality: approximate
    note: "Provisions per NRS 13; IFRS uses IAS 37 with similar definitions but different recognition tests."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Gjeld
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 D I)

> Avsetning for forpliktelser
