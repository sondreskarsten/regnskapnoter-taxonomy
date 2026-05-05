---
concept_id: regnskap-no:GodtgjorelseDagligLederPensjon
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
    text: "Pensjonskostnad daglig leder"
  - lang: en
    role: standardLabel
    text: "CEO pension cost"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-45"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:KeyManagementPersonnelCompensationPostemploymentBenefits
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept er pensjonskostnad; ifrs-full er postemployment benefits bredere definert."

---

## Verbatim text (regnskapsloven § 7-45)

> Pensjonskostnad daglig leder
