---
concept_id: regnskap-no:AntallAksjerEgneAksjer
namespace: regnskap-no
period_type: instant
balance: null
data_type: sharesItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Antall egne aksjer"
  - lang: en
    role: standardLabel
    text: "Number of treasury shares"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-42"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NumberOfSharesIssuedAndOutstandingTreasuryShares
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept er antall egne aksjer på balansedagen; ifrs-full er issued and outstanding treasury shares."

---

## Verbatim text (regnskapsloven § 7-42)

> Antall egne aksjer
