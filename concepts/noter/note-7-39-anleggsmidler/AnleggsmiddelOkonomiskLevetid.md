---
concept_id: regnskap-no:AnleggsmiddelOkonomiskLevetid
namespace: regnskap-no
period_type: duration
data_type: decimalItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Økonomisk levetid"
  - lang: en
    role: standardLabel
    text: "Economic useful life"

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
  - to: ifrs-full:UsefulLifeMeasuredAsPeriodOfTimePropertyPlantAndEquipment
    relation: skos:closeMatch
    quality: approximate
    note: "Economic useful life used for depreciation; IFRS records as useful-life period (IAS 16.50)."
axes:
  - axis: regnskap-no:KlassifiseringAvAnleggsmidlerAxis
    closed: true
---

## Verbatim text (regnskapsloven § 7-39)

> Økonomisk levetid
