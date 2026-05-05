---
concept_id: regnskap-no:Pensjonsforpliktelser
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
    text: "Pensjonsforpliktelser"
  - lang: en
    role: standardLabel
    text: "Pension obligations"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D I 1"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NetDefinedBenefitLiability
    relation: skos:closeMatch
    quality: approximate
    note: "NRS 6 pension liability; IFRS IAS 19 uses different actuarial framework."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:AvsetningForForpliktelser
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 D I 1)

> Pensjonsforpliktelser
