---
concept_id: regnskap-no:EgenkapitalKapitalforhoyelse
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
    text: "Kapitalforhøyelse"
  - lang: en
    role: standardLabel
    text: "Capital increase"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:IncreaseDecreaseThroughIssueOfShareCapital
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept dekker både kontant og naturalia; ifrs-full er begrenset til share-capital issue."

---

## Verbatim text (regnskapsloven § 7-46)

> Kapitalforhøyelse
