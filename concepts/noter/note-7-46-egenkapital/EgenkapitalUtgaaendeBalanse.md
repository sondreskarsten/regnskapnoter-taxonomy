---
concept_id: regnskap-no:EgenkapitalUtgaaendeBalanse
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
    text: "Utgående balanse egenkapital"
  - lang: en
    role: standardLabel
    text: "Equity at end of period"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:Equity
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-46)

> Utgående balanse egenkapital
