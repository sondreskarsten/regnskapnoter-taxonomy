---
concept_id: regnskap-no:HendelserEtterBalansedagenBeskrivelse
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
    text: "Hendelser etter balansedagen"
  - lang: en
    role: standardLabel
    text: "Events after the balance sheet date"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-7 b"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Det skal opplyses om arten og den økonomiske virkningen av vesentlige hendelser som har inntruffet etter balansedagen, og som ikke er regnskapsført i resultatregnskap eller balanse."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-7 b"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfEventsAfterReportingPeriodExplanatory
    relation: skos:closeMatch
    quality: approximate
---
