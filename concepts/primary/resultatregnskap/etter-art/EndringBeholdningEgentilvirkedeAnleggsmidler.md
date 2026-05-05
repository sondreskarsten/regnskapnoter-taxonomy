---
concept_id: regnskap-no:EndringBeholdningEgentilvirkedeAnleggsmidler
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
    text: "Endring i beholdning av egentilvirkede anleggsmidler"
  - lang: en
    role: standardLabel
    text: "Work performed by entity and capitalised"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 4"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "4. Endring i beholdning av egentilvirkede anleggsmidler"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1 (1) post 4"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:WorkPerformedByEntityAndCapitalised
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konseptet er en inntektsføring; IFRS-Full er en aktivering. Logisk sett er beløpene speilbilde av hverandre."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:Driftsresultat
    weight: +1
    order: 4
---

## Verbatim text (regnskapsloven § 6-1 (1) post 4)

> 4. Endring i beholdning av egentilvirkede anleggsmidler
