---
concept_id: regnskap-no:TilknyttetSelskapBokfortVerdi
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Bokført verdi av investering i tilknyttet selskap"
  - lang: en
    role: standardLabel
    text: "Carrying amount of investment in associate"

references:
  - publisher: NRS
    document: Investering i tilknyttet selskap og deltakelse i FKV
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2007
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999
    applicable_to_fiscal_year: 2020

definitions:
  - lang: nb
    role: definition
    text: "(Opphevet)"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999
    applicable_to_fiscal_year: 2020
    authoritative: true

mappings:
  - to: ifrs-full:InvestmentsInAssociates
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-44)

> Bokført verdi av investering i tilknyttet selskap
