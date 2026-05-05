---
concept_id: regnskap-no:EgenkapitalRollforwardBelop
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Beløp i egenkapital-rollforward"
  - lang: en
    role: standardLabel
    text: "Equity rollforward amount"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:Equity
    relation: skos:closeMatch
    quality: approximate
    note: "Equity-rollforward fact dimensionalized by component (E) and movement (M); IFRS uses StatementOfChangesInEquity."
axes:
  - axis: regnskap-no:EgenkapitalKomponentAxis
    closed: true
  - axis: regnskap-no:EgenkapitalEndringAxis
    closed: true
---

## Verbatim text (regnskapsloven § 7-46)

> Beløp i egenkapital-rollforward
