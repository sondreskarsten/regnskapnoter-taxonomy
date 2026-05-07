---
concept_id: regnskap-no:KonsernMellomvaerendeGjeld
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Mellomværende konsern – gjeld"
  - lang: en
    role: standardLabel
    text: "Intercompany payables"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-22"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Samlet beløp som gjelder foretak i samme konsern under annen langsiktig gjeld og kortsiktig gjeld."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-22"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:AmountsPayableToRelatedParties
    relation: skos:closeMatch
    quality: approximate
---
