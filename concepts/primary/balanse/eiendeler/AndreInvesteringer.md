---
concept_id: regnskap-no:AndreInvesteringer
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
    text: "Andre investeringer"
  - lang: en
    role: standardLabel
    text: "Other investments"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 B III 3"
    applicable_from_fiscal_year: 1999

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Other short-term investments."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:InvesteringerOmlopsmidler
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 6-2 B III 3)

> Andre investeringer
