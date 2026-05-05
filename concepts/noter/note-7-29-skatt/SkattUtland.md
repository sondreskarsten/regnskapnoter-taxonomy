---
concept_id: regnskap-no:SkattUtland
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
    text: "Skatt utland"
  - lang: en
    role: standardLabel
    text: "Foreign tax"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-29"
    applicable_from_fiscal_year: 1999
definitions:
  - lang: nb
    role: definition
    text: "Andre forpliktelser Det skal opplyses om andre forpliktelser enn nevnt i § 7-28 som ikke er regnskapsført. Det skal opplyses særskilt dersom slike forpliktelser er sikret ved pant."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-29"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ForeignTaxExpenseIncome
    relation: skos:closeMatch
    quality: approximate
    note: "Tax paid to foreign jurisdictions."
---

## Verbatim text (regnskapsloven § 7-29)

> Skatt utland
