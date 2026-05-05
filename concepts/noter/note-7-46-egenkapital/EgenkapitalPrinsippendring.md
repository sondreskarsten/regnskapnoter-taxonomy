---
concept_id: regnskap-no:EgenkapitalPrinsippendring
namespace: regnskap-no
period_type: duration
balance: null
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Prinsippendring innregnet i egenkapital"
  - lang: en
    role: standardLabel
    text: "Change in accounting policy recognised in equity"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:IncreaseDecreaseDueToChangesInAccountingPolicyAndCorrectionsOfPriorPeriodErrorsRetainedEarnings
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept inkluderer både prinsippendring og feil-korrigering; ifrs-full splitter."

---

## Verbatim text (regnskapsloven § 7-46)

> Prinsippendring innregnet i egenkapital
