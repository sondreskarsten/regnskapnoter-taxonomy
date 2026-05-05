---
concept_id: regnskap-no:GjeldUsikret
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
    text: "Gjeld uten sikkerhet"
  - lang: en
    role: standardLabel
    text: "Unsecured debt"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:UnsecuredBankLoansReceived
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept dekker all usikret gjeld; ifrs-full splitter etter motpartstype."

---

## Verbatim text (regnskapsloven § 7-40)

> Gjeld uten sikkerhet
