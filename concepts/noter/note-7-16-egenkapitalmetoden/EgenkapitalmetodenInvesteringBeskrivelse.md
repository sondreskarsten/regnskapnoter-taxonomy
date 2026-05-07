---
concept_id: regnskap-no:EgenkapitalmetodenInvesteringBeskrivelse
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
    text: "Investering etter egenkapitalmetoden – beskrivelse"
  - lang: en
    role: standardLabel
    text: "Equity method investment disclosures"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-16"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "For investering som regnskapsføres etter egenkapitalmetoden, skal det opplyses om anskaffelseskost og balanseført egenkapital på anskaffelsestidspunktet. For hver investering skal det opplyses om inngående balanse, inntektsført resultat, andre endringer i løpet av året og utgående balanse. Det skal opplyses om merverdier og goodwill samt avskrivning av merverdier og goodwill."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-16"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfInvestmentsAccountedForUsingEquityMethodExplanatory
    relation: skos:closeMatch
    quality: approximate
---
