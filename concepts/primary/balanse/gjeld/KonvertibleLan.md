---
concept_id: regnskap-no:KonvertibleLan
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Konvertible lån"
  - lang: en
    role: standardLabel
    text: "Convertible loans"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D II 1"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NoncurrentConvertibleNotesPayable
    relation: skos:closeMatch
    quality: approximate
    note: "Convertible debt; IFRS may bifurcate equity component (IAS 32)."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:AnnenLangsiktigGjeld
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 D II 1)

> Konvertible lån
