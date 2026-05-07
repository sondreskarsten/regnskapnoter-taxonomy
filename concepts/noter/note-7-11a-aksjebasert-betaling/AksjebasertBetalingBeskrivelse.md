---
concept_id: regnskap-no:AksjebasertBetalingBeskrivelse
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
    text: "Aksjeverdibasert betaling – beskrivelse"
  - lang: en
    role: standardLabel
    text: "Share-based payment description"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-11a"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Det skal redegjøres for bruken av aksjeverdibasert betaling. Det skal opplyses om kostnadsført aksjeverdibasert betaling minst spesifisert på de aktuelle postene i resultatregnskapet. Det skal opplyses hvordan kostnadene er beregnet, herunder de forutsetningene som er lagt til grunn for beregningen."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-11a"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfSharebasedPaymentArrangementsExplanatory
    relation: skos:closeMatch
    quality: approximate
---
