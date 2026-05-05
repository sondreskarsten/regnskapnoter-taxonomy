---
concept_id: regnskap-no:AntallAnsatteSnitt
namespace: regnskap-no
period_type: duration
balance: null
data_type: decimalItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Gjennomsnittlig antall ansatte"
  - lang: en
    role: standardLabel
    text: "Average number of employees"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-30"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Antall ansatte Det skal opplyses om antall årsverk som den regnskapspliktige har sysselsatt i regnskapsåret."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-30"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:AverageNumberOfEmployees
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-30)

> Gjennomsnittlig antall ansatte
