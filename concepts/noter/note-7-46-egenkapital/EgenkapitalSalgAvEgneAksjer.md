---
concept_id: regnskap-no:EgenkapitalSalgAvEgneAksjer
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Salg av egne aksjer"
  - lang: en
    role: standardLabel
    text: "Treasury share sale"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Fortsatt drift Dersom det er usikkerhet om fortsatt drift, skal det opplyses om usikkerheten. Kapittel 8. Offentlighet, innsendelse av regnskap, straff"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:SaleOfTreasuryShares
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-46)

> Salg av egne aksjer
