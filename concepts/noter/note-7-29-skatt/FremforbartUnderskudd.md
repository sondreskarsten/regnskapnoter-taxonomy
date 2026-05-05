---
concept_id: regnskap-no:FremforbartUnderskudd
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
    text: "Fremførbart underskudd"
  - lang: en
    role: standardLabel
    text: "Carry-forward losses"

references:
  - publisher: Stortinget
    document: skatteloven
    paragraph: "§ 14-6"
    applicable_from_fiscal_year: 1999
definitions:
  - lang: nb
    role: definition
    text: "Skatteloven § 14-6 — Underskudd: Underskudd ved virksomhet kan kreves fradratt i skattyterens inntekt i senere år. Underskuddet skal fradras så langt det er skattepliktig inntekt, og skal anvendes uten unødig opphold. Underskudd faller ikke bort etter en bestemt tidsfrist."
    source_publisher: Stortinget
    source_document: skatteloven
    source_paragraph: "§ 14-6"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:UnusedTaxLossesForWhichNoDeferredTaxAssetRecognised
    relation: skos:closeMatch
    quality: approximate
    note: "Norwegian unused tax losses; IFRS reports recognized vs unrecognized split."
---

## Verbatim text (skatteloven § 14-6)

> Fremførbart underskudd
