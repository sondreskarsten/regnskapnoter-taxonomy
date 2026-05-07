---
concept_id: regnskap-no:OpptjentEgenkapitalSpesifikasjon
namespace: regnskap-no
period_type: duration
balance: null
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Opptjent egenkapital – spesifikasjon"
  - lang: en
    role: standardLabel
    text: "Retained earnings specification"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-25"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Opptjent egenkapital skal spesifiseres. Det skal opplyses om endringer i egenkapitalen i løpet av regnskapsåret."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-25"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:RetainedEarnings
    relation: skos:broadMatch
    quality: approximate
---
