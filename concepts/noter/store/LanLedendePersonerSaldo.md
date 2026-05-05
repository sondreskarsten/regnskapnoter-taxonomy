---
concept_id: regnskap-no:LanLedendePersonerSaldo
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
    text: "Saldo lån til ledende personer"
  - lang: en
    role: standardLabel
    text: "Loans to key management personnel"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-32"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:KeyManagementPersonnelCompensation
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konseptet er lånsaldo; ifrs-full er bredere kompensasjonsbegrep — konteksten ligner men måling er ulik."
---

## Verbatim text (regnskapsloven § 7-32)

> Saldo lån til ledende personer
