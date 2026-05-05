---
concept_id: regnskap-no:FelleskontrollertVirksomhetNavn
namespace: regnskap-no
period_type: instant
balance: null
data_type: stringItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Navn på felleskontrollert virksomhet"
  - lang: en
    role: standardLabel
    text: "Name of joint venture"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "(Opphevet)"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:NameOfJointVenture
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-44)

> Navn på felleskontrollert virksomhet
