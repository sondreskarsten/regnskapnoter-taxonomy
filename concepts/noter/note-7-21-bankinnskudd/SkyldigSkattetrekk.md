---
concept_id: regnskap-no:SkyldigSkattetrekk
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
    text: "Skyldig skattetrekk"
  - lang: en
    role: standardLabel
    text: "Withholding tax payable"

references:
  - publisher: Stortinget
    document: skattebetalingsloven
    paragraph: "§ 5-12"
    applicable_from_fiscal_year: 2009
definitions:
  - lang: nb
    role: definition
    text: "Bundne skattetrekksmidler etter skattebetalingsloven § 5-12: Den som gjør fradrag i lønn for forskuddstrekk, skal sette beløpet inn på særskilt bankkonto (skattetrekkskonto) hver gang det utbetales lønn. I stedet for innskudd på skattetrekkskonto kan det stilles bankgaranti for trekkbeløpet, eller midlene kan være sikret på annen måte godtatt av skatteoppkreveren."
    source_publisher: Stortinget
    source_document: skattebetalingsloven
    source_paragraph: "§ 5-12"
    applicable_from_fiscal_year: 2009
    authoritative: true

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Withheld but unpaid employee income tax; Norwegian-specific liability."
---

## Verbatim text (skattebetalingsloven § 5-12)

> Skyldig skattetrekk
