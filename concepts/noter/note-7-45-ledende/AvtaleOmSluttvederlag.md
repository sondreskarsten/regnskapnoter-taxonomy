---
concept_id: regnskap-no:AvtaleOmSluttvederlag
namespace: regnskap-no
period_type: duration
balance: null
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Avtale om sluttvederlag"
  - lang: en
    role: standardLabel
    text: "Severance agreement"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-45"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:KeyManagementPersonnelCompensationTerminationBenefits
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept er avtale-tekst om sluttvederlag; ifrs-full er kvantitative termination benefits."

---

## Verbatim text (regnskapsloven § 7-45)

> Avtale om sluttvederlag
