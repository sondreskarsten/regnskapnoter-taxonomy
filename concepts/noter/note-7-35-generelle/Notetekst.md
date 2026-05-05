---
concept_id: regnskap-no:Notetekst
namespace: regnskap-no
period_type: duration
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Notetekst"
  - lang: en
    role: standardLabel
    text: "Notes (free text)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-35"
    applicable_from_fiscal_year: 1999
definitions:
  - lang: nb
    role: definition
    text: "Regnskapsprinsipper m.v. (1) Det skal gis opplysninger om anvendte regnskapsprinsipper. (2) Det skal opplyses om sammenligningstallene er omarbeidet. Dersom de omarbeides skal omarbeidingen forklares, jf. § 6-6 ."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-35"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfNotesAndOtherExplanatoryInformationExplanatory
    relation: skos:closeMatch
    quality: approximate
    note: "Free-text noter container; IFRS uses extensible disclosure framework."
---

## Verbatim text (regnskapsloven § 7-35)

> Notetekst
