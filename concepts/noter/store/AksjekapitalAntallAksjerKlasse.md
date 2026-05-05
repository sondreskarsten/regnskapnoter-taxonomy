---
concept_id: regnskap-no:AksjekapitalAntallAksjerKlasse
namespace: regnskap-no
period_type: instant
balance: null
data_type: sharesItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Antall aksjer per klasse"
  - lang: en
    role: standardLabel
    text: "Number of shares by class"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-26"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NumberOfSharesIssued
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk § 7-26 krever fordeling per aksjeklasse; ifrs-full har bare aggregert antall."
---

## Verbatim text (regnskapsloven § 7-26)

> Antall aksjer per klasse
