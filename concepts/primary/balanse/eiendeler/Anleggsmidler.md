---
concept_id: regnskap-no:Anleggsmidler
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
    text: "Anleggsmidler"
  - lang: en
    role: standardLabel
    text: "Non-current assets"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NoncurrentAssets
    relation: skos:closeMatch
    quality: approximate
    note: "Norwegian 'anleggsmidler' is defined per regnskapsloven § 5-1 as 'eiendeler bestemt til varig eie eller bruk'; IFRS uses a 12-month operating-cycle test under IAS 1.66."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Eiendeler
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 A)

> Anleggsmidler
