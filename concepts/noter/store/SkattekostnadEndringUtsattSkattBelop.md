---
concept_id: regnskap-no:SkattekostnadEndringUtsattSkattBelop
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
    text: "Endring i utsatt skatt (skattekostnad)"
  - lang: en
    role: standardLabel
    text: "Change in deferred tax (tax expense)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-23"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Skattekostnad Det skal opplyses om beregning av skattekostnad og utsatt skatt eller utsatt skattefordel."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-23"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DeferredTaxExpenseIncome
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-23)

> Endring i utsatt skatt (skattekostnad)
