---
concept_id: regnskap-no:BetingetUtfallEstimertBelop
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Estimert beløp betinget utfall"
  - lang: en
    role: standardLabel
    text: "Estimated amount of contingency"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-33"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Betingede utfall Det skal opplyses om forhold ved regnskapsårets slutt med betinget utfall."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-33"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:EstimateOfFinancialEffectOfContingentLiabilities
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-33)

> Estimert beløp betinget utfall
