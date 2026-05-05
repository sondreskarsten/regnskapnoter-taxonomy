---
concept_id: regnskap-no:FordringerKundefordringerInkluderendeAvsetning
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
    text: "Kundefordringer inkl. avsetning"
  - lang: en
    role: standardLabel
    text: "Trade receivables incl. provision"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:TradeAndOtherCurrentReceivables
    relation: skos:closeMatch
    quality: approximate
    note: "Trade receivables including loss allowance; IFRS aggregates trade and other current receivables."
---

## Verbatim text (regnskapsloven § 7-40)

> Kundefordringer inkl. avsetning
