---
concept_id: regnskap-no:SumDriftsinntekter
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Sum driftsinntekter"
  - lang: en
    role: standardLabel
    text: "Total operating income"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1)"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "(1) Resultatregnskapet etter art skal ha følgende oppstillingsplan."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1 (1)"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:Revenue
    relation: skos:closeMatch
    quality: approximate
    note: "Sum av § 6-1 post 1 og post 2; ifrs-full:Revenue dekker primært post 1 men er ofte brukt for samlet driftsinntekt i konsolidert IFRS-rapportering."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:Driftsresultat
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-1 (1))

> Sum driftsinntekter
