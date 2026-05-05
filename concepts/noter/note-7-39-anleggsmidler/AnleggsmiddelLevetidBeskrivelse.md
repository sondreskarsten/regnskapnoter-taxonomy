---
concept_id: regnskap-no:AnleggsmiddelLevetidBeskrivelse
namespace: regnskap-no
period_type: duration
balance: null
data_type: stringItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Beskrivelse av forventet levetid"
  - lang: en
    role: standardLabel
    text: "Description of useful life"

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
  - to: ifrs-full:UsefulLivesOrDepreciationRatesPropertyPlantAndEquipment
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept inkluderer immaterielle eiendeler og varige driftsmidler; IFRS-Full er begrenset til PP&E."

---

## Verbatim text (regnskapsloven § 7-39)

> Beskrivelse av forventet levetid
