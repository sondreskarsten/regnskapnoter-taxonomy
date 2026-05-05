---
concept_id: regnskap-no:FordringerForfallEttFemAr
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
    text: "Fordringer med forfall mellom ett og fem år"
  - lang: en
    role: standardLabel
    text: "Receivables falling due between 1 and 5 years"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:LongtermTradeReceivables
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk presentasjon krever 1-5 år bucket; IFRS-Full grupperer som non-current trade receivables uten 1-5 år splitt."

---

## Verbatim text (regnskapsloven § 7-40)

> Fordringer med forfall mellom ett og fem år
