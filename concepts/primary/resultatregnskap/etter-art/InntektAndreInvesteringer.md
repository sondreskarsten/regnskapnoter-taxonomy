---
concept_id: regnskap-no:InntektAndreInvesteringer
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
    text: "Inntekt på andre investeringer"
  - lang: en
    role: standardLabel
    text: "Income from other investments"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1 (1) post 12"
    applicable_from_fiscal_year: 1999

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Aggregert kategori for utbytte og gevinst på finansielle anleggsmidler utenfor konsern/tilknyttet; ingen direkte ifrs-full-ekvivalent."

parents:
  - role: "[610000] Resultatregnskap etter art"
    parent: regnskap-no:ResultatForSkattekostnad
    weight: +1
    order: 12
---

## Verbatim text (regnskapsloven § 6-1 (1) post 12)

> 12. Inntekt på andre investeringer
