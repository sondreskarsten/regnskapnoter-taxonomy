---
concept_id: regnskap-no:GarantiansvarOverforTredjepart
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
    text: "Garantiansvar overfor tredjepart"
  - lang: en
    role: standardLabel
    text: "Guarantee liabilities to third parties"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:ContingentLiabilitiesIncurredByVentureFromInterestsInJointVentures
    relation: skos:closeMatch
    quality: approximate
    note: "Garantiansvar er en betinget forpliktelse; ifrs-full har lignende konsept under JV-kontekst men ikke en direkte ekvivalent for tredjepartsgarantier."

---

## Verbatim text (regnskapsloven § 7-40)

> Garantiansvar overfor tredjepart
