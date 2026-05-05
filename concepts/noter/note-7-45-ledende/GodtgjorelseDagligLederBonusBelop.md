---
concept_id: regnskap-no:GodtgjorelseDagligLederBonusBelop
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
    text: "Bonus til daglig leder"
  - lang: en
    role: standardLabel
    text: "Bonus to CEO"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-45"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:KeyManagementPersonnelCompensationShorttermEmployeeBenefits
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept er bonus-delen av kompensasjon; ifrs-full er kortidsytelser bredt definert."

---

## Verbatim text (regnskapsloven § 7-45)

> Bonus til daglig leder
