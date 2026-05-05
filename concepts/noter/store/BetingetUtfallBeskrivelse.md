---
concept_id: regnskap-no:BetingetUtfallBeskrivelse
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
    text: "Beskrivelse av betinget utfall"
  - lang: en
    role: standardLabel
    text: "Description of contingency"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-33"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Betingede utfall Det skal opplyses om forhold ved regnskapsårets slutt med betinget utfall."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-33"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DescriptionOfNatureOfContingentLiabilities
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk § 7-33 omfatter både betingede forpliktelser og betingede eiendeler; ifrs-full splitter."
---

## Verbatim text (regnskapsloven § 7-33)

> Beskrivelse av betinget utfall
