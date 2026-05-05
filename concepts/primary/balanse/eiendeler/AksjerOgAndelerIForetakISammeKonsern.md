---
concept_id: regnskap-no:AksjerOgAndelerIForetakISammeKonsern
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
    text: "Aksjer og andeler i foretak i samme konsern"
  - lang: en
    role: standardLabel
    text: "Shares and units in group enterprises"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 B III 1"
    applicable_from_fiscal_year: 1999

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Short-term holdings in group companies; Norwegian-specific separation."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:InvesteringerOmlopsmidler
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 B III 1)

> Aksjer og andeler i foretak i samme konsern
