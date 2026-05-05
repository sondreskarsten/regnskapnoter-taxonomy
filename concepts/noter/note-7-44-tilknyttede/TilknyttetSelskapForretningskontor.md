---
concept_id: regnskap-no:TilknyttetSelskapForretningskontor
namespace: regnskap-no
period_type: instant
balance: null
data_type: stringItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Forretningskontor tilknyttet selskap"
  - lang: en
    role: standardLabel
    text: "Registered office of associate"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-44"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:PrincipalPlaceOfBusinessOfAssociate
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept er forretningskontor; ifrs-full bruker principal place of business."

---

## Verbatim text (regnskapsloven § 7-44)

> Forretningskontor tilknyttet selskap
