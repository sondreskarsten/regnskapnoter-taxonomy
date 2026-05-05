---
concept_id: regnskap-no:MaskinerOgAnlegg
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Maskiner og anlegg"
  - lang: en
    role: standardLabel
    text: "Machinery and plant"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A II 2"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:MachineryNetOfAccumulatedDepreciationAndAmortisationAndImpairment
    relation: skos:closeMatch
    quality: approximate
    note: "Generic machinery aggregation."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:VarigeDriftsmidler
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 6-2 A II 2)

> Maskiner og anlegg
