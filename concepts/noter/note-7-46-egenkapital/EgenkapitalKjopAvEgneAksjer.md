---
concept_id: regnskap-no:EgenkapitalKjopAvEgneAksjer
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
    text: "Kjøp av egne aksjer"
  - lang: en
    role: standardLabel
    text: "Treasury share purchase"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:PurchaseOfTreasuryShares
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-46)

> Kjøp av egne aksjer
