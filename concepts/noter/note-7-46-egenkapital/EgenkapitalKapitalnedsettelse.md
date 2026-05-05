---
concept_id: regnskap-no:EgenkapitalKapitalnedsettelse
namespace: regnskap-no
period_type: duration
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Kapitalnedsettelse"
  - lang: en
    role: standardLabel
    text: "Capital decrease"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:DecreaseInEquityFromCapitalReduction
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept dekker både formell nedsettelse og udekket tap-utligning; ifrs-full er begrenset til formell capital reduction."

---

## Verbatim text (regnskapsloven § 7-46)

> Kapitalnedsettelse
