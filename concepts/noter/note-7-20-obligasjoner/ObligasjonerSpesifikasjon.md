---
concept_id: regnskap-no:ObligasjonerSpesifikasjon
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
    text: "Obligasjoner – spesifikasjon"
  - lang: en
    role: standardLabel
    text: "Bonds specification"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-20"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "(1) Obligasjoner skal spesifiseres etter debitorkategori og pålydende valuta. Det skal opplyses om balanseført verdi og markedsverdi. (2) Foretak av allmenn interesse skal gi en oversikt over rentereguleringstidspunkter og gjennomsnittlig rente."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-20"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfDebtSecuritiesExplanatory
    relation: skos:broadMatch
    quality: approximate
---
