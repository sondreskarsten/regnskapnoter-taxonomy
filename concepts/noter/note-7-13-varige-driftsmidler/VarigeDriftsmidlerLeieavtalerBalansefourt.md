---
concept_id: regnskap-no:VarigeDriftsmidlerLeieavtalerBalansefourt
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Balanseførte leieavtaler varige driftsmidler"
  - lang: en
    role: standardLabel
    text: "Capitalised leases PPE"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-13"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Balanseført verdi av leieavtaler under varige driftsmidler."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-13"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:RightofuseAssets
    relation: skos:broadMatch
    quality: approximate
---
