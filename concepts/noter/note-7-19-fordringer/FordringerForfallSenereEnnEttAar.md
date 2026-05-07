---
concept_id: regnskap-no:FordringerForfallSenereEnnEttAar
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
    text: "Fordringer med forfall senere enn ett år"
  - lang: en
    role: standardLabel
    text: "Receivables due after more than one year"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-19"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "For hver post under eiendeler skal det opplyses om fordringer som forfaller senere enn ett år etter regnskapsårets slutt."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-19"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:NoncurrentReceivables
    relation: skos:closeMatch
    quality: approximate
---
