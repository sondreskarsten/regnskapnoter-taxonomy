---
concept_id: regnskap-no:HendelserEtterBalansedagenOkonomiskVirkning
namespace: regnskap-no
period_type: duration
balance: null
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Økonomisk virkning av hendelser etter balansedagen"
  - lang: en
    role: standardLabel
    text: "Financial effect of events after balance sheet date"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-7 b"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Den økonomiske virkningen av vesentlige hendelser som har inntruffet etter balansedagen."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-7 b"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:AdjustmentsForEventsAfterReportingPeriod
    relation: skos:broadMatch
    quality: approximate
---
