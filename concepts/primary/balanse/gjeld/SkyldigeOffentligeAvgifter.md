---
concept_id: regnskap-no:SkyldigeOffentligeAvgifter
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
    text: "Skyldige offentlige avgifter"
  - lang: en
    role: standardLabel
    text: "Public duties payable"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 D III 6"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "D. Gjeld / III."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 D III 6"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "VAT, employer's NI contribution, withholding tax aggregated; Norwegian-specific."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:KortsiktigGjeld
    weight: +1
    order: 6
---

## Verbatim text (regnskapsloven § 6-2 D III 6)

> Skyldige offentlige avgifter
