---
concept_id: regnskap-no:EgenkapitalAvsattUtbytte
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
    text: "Avsatt utbytte (egenkapital)"
  - lang: en
    role: standardLabel
    text: "Dividends declared (equity movement)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:DividendsRecognisedAsDistributionsToOwners
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-46)

> Avsatt utbytte (egenkapital)
