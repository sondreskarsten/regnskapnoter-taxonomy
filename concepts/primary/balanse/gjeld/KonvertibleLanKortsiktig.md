---
concept_id: regnskap-no:KonvertibleLanKortsiktig
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
    text: "Konvertible lån (kortsiktig)"
  - lang: en
    role: standardLabel
    text: "Convertible loans (current)"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D III 1"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:CurrentConvertibleNotesPayable
    relation: skos:closeMatch
    quality: approximate
    note: "Short-term convertibles."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:KortsiktigGjeld
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 D III 1)

> Konvertible lån (kortsiktig)
