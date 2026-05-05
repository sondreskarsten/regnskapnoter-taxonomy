---
concept_id: regnskap-no:OverordnetMorselskapNavn
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
    text: "Navn på overordnet morselskap"
  - lang: en
    role: standardLabel
    text: "Name of ultimate parent"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-5"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Finansiell markedsrisiko (1) Det skal gis opplysninger om egenskaper ved og omfang av finansielle derivater fordelt på klasser av derivater. Opplysningene skal omfatte vesentlige betingelser og forhold som kan påvirke beløpsstørrelse, tidfesting og usikkerhet ved fremtidige kontantstrømmer. (2) Foretak av allmenn interesse skal gi opplysninger om finansiell markedsrisiko fordelt på arter av risiko."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-5"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:NameOfUltimateParentOfGroup
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-5)

> Navn på overordnet morselskap
