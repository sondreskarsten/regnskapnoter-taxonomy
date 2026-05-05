---
concept_id: regnskap-no:AnnenDriftsinntekt
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
    text: "Annen driftsinntekt"
  - lang: en
    role: standardLabel
    text: "Other operating income"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 2"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:OtherIncome
    relation: skos:closeMatch
    quality: approximate
    note: "ifrs-full:OtherIncome har bredere scope; § 6-1 post 2 er driftsmessig 'annen' inntekt i tillegg til hovedsalg."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:SumDriftsinntekter
    weight: +1
    order: 2
---

## Verbatim text (regnskapsloven § 6-1 (1) post 2)

> 2. Annen driftsinntekt
