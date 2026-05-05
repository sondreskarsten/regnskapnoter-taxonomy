---
concept_id: regnskap-no:DatterselskapResultatandel
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
    text: "Datterselskaps resultatandel"
  - lang: en
    role: standardLabel
    text: "Subsidiary share of profit"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-15"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:ProfitLossFromContinuingOperations
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk EK-metode resultatandel; mappes løst til IFRS profit/loss-konsept."
---

## Verbatim text (regnskapsloven § 7-15)

> Datterselskaps resultatandel
