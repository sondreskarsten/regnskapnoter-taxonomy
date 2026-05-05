---
concept_id: regnskap-no:ResultatForSkattekostnadFunksjon
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
    text: "Resultat før skattekostnad"
  - lang: en
    role: standardLabel
    text: "Profit (loss) before tax"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 14"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "14. Resultat før skattekostnad"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1a (1) post 14"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ProfitLossBeforeTax
    relation: skos:exactMatch
    quality: exact

parents:
  - role: "[610100] Resultatregnskap etter funksjon"
    parent: regnskap-no:AarsresultatFunksjon
    weight: +1
    order: 14
---

## Verbatim text (regnskapsloven § 6-1a (1) post 14)

> 14. Resultat før skattekostnad
