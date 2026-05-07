---
concept_id: regnskap-no:AksjebasertBetalingKostnadsfort
namespace: regnskap-no
period_type: duration
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Kostnadsført aksjeverdibasert betaling"
  - lang: en
    role: standardLabel
    text: "Share-based payment expense"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-11a"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Kostnadsført aksjeverdibasert betaling i regnskapsåret."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-11a"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ExpenseFromSharebasedPaymentTransactionsWithEmployees
    relation: skos:closeMatch
    quality: approximate
---
