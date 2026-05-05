---
concept_id: regnskap-no:AnleggsmiddelOpptattAvskrivningBeskrivelse
namespace: regnskap-no
period_type: duration
balance: null
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Beskrivelse av avskrivningsplan"
  - lang: en
    role: standardLabel
    text: "Description of depreciation plan"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-12"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Anleggsmidler (1) For hver post under varige driftsmidler og immaterielle eiendeler skal det opplyses om: 1. anskaffelseskost med spesifikasjon av balanseførte finansieringsutgifter knyttet til egentilvirkede anleggsmidler. 2. tilgang og avgang i løpet av regnskapsåret, 3. samlede avskrivninger, nedskrivninger og reverseringer av nedskrivninger, og 4. avskrivninger, nedskrivninger og reverseringer av nedskrivninger i regnskapsåret. (2) Det skal opplyses om endring i avskrivningsplan."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-12"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DescriptionOfDepreciationMethodPropertyPlantAndEquipment
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-12)

> Beskrivelse av avskrivningsplan
