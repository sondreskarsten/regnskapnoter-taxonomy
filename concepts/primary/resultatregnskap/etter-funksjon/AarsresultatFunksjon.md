---
concept_id: regnskap-no:AarsresultatFunksjon
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
    text: "Årsresultat"
  - lang: en
    role: standardLabel
    text: "Profit (loss)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-1a (1) post 16"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "16. Årsresultat"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-1a (1) post 16"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ProfitLoss
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 6-1a (1) post 16)

> 16. Årsresultat
