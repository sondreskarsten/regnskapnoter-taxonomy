---
concept_id: regnskap-no:TilknyttetSelskapNavn
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
    text: "Navn på tilknyttet selskap"
  - lang: en
    role: standardLabel
    text: "Name of associated company"

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
  - to: ifrs-full:NameOfAssociate
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-44)

> Navn på tilknyttet selskap
