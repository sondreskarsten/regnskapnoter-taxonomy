---
concept_id: regnskap-no:InvesteringerOmlopsmidler
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Investeringer"
  - lang: en
    role: standardLabel
    text: "Investments (current)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 B III"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "B. Omløpsmidler — III. Investeringer"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 B III"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:CurrentInvestments
    relation: skos:closeMatch
    quality: approximate
    note: "Short-term financial investments."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Omlopsmidler
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-2 B III)

> Investeringer
