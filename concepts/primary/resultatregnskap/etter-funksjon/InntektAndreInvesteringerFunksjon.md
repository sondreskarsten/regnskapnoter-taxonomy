---
concept_id: regnskap-no:InntektAndreInvesteringerFunksjon
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
    paragraph: "§ 6-1a (1) post 8"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "8. Inntekt på andre investeringer"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1a (1) post 8"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Samme begrep som § 6-1 post 12."

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:ResultatForSkattekostnadFunksjon
    weight: +1
    order: 8
---

## Verbatim text (regnskapsloven § 6-1a (1) post 8)

> 8. Inntekt på andre investeringer
