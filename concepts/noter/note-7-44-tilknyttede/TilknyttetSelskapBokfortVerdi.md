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
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:InvestmentsInAssociates
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-44)

> Bokført verdi av investering i tilknyttet selskap
