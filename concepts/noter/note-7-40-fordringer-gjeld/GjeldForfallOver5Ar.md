---
concept_id: regnskap-no:GjeldForfallOver5Ar
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
    text: "Gjeld med forfall etter mer enn fem år"
  - lang: en
    role: standardLabel
    text: "Debt falling due after more than 5 years"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NoncurrentLiabilities
    relation: skos:closeMatch
    quality: approximate
    note: "Långsiktig gjeld over 5 år er en delmengde av ifrs-full:NoncurrentLiabilities."

---

## Verbatim text (regnskapsloven § 7-40)

> Gjeld med forfall etter mer enn fem år
