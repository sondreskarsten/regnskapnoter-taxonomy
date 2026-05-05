---
concept_id: regnskap-no:AnleggsmiddelAkkumulerteAvskrivninger
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
    text: "Akkumulerte avskrivninger"
  - lang: en
    role: standardLabel
    text: "Accumulated depreciation"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-39"
    applicable_from_fiscal_year: 1999
definitions:
  - lang: nb
    role: definition
    text: "Anleggsmidler (1) For varige driftsmidler og immaterielle eiendeler skal det opplyses om: 1. anskaffelseskost med spesifikasjon av balanseførte lånekostnader knyttet til egentilvirkede anleggsmidler, 2. tilgang og avgang i løpet av regnskapsåret, 3. samlede avskrivninger, nedskrivninger og reverseringer av nedskrivninger, og 4. avskrivninger, nedskrivninger og reverseringer av nedskrivninger i regnskapsåret. (2) Det skal opplyses om økonomisk levetid og valg av avskrivningsplan for immaterielle eiendeler. (3) Goodwill skal spesifiseres for hvert enkelt virksomhetskjøp. Avskrivningsplan for goodwill som er lenger enn fem år, skal begrunnes."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-39"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:PropertyPlantAndEquipmentAccumulatedDepreciationAndImpairment
    relation: skos:closeMatch
    quality: approximate
    note: "Norwegian disclosure separates accumulated depreciation per anleggsmiddel class; IFRS aggregates depreciation and impairment."
axes:
  - axis: regnskap-no:KlassifiseringAvAnleggsmidlerAxis
    closed: true
---

## Verbatim text (regnskapsloven § 7-39)

> Akkumulerte avskrivninger
