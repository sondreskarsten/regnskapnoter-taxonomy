---
concept_id: regnskap-no:GodtgjorelseRevisorSkatterad
namespace: regnskap-no
period_type: duration
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Godtgjørelse revisor skatterådgivning"
  - lang: en
    role: standardLabel
    text: "Audit fees — tax advisory"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-31a"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Godtgjørelse til revisor Det skal opplyses om godtgjørelse til revisor og hvordan godtgjørelsen er fordelt på lovpålagt revisjon, andre attestasjonstjenester, skatterådgivning og andre tjenester utenfor revisjonen. Honorarer for andre tjenester utenfor revisjonen skal spesifiseres for vesentlig forskjellige tjenester. Opplysningene skal også omfatte godtgjørelse til foretak som revisor har et særskilt samarbeid med."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-31a"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:FeesPaidToAuditorTaxServices
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-31a)

> Godtgjørelse revisor skatterådgivning
