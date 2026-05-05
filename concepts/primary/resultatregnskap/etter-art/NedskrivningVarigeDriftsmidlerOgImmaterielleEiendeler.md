---
concept_id: regnskap-no:NedskrivningVarigeDriftsmidlerOgImmaterielleEiendeler
namespace: regnskap-no
period_type: duration
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Nedskrivning av varige driftsmidler og immaterielle eiendeler"
  - lang: en
    role: standardLabel
    text: "Impairment loss on property, plant, equipment and intangibles"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 8"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "8. Nedskrivning av varige driftsmidler og immaterielle eiendeler"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1 (1) post 8"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ImpairmentLossRecognisedInProfitOrLoss
    relation: skos:closeMatch
    quality: approximate
    note: "ifrs-full:ImpairmentLossRecognisedInProfitOrLoss er bredere; § 6-1 post 8 er begrenset til varige driftsmidler og immaterielle eiendeler."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:Driftsresultat
    weight: -1
    order: 8
---

## Verbatim text (regnskapsloven § 6-1 (1) post 8)

> 8. Nedskrivning av varige driftsmidler og immaterielle eiendeler
