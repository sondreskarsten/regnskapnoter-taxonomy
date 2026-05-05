---
concept_id: regnskap-no:LanTilTilknyttetSelskapOgFelleskontrollertVirksomhet
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
    text: "Lån til tilknyttet selskap og felleskontrollert virksomhet"
  - lang: en
    role: standardLabel
    text: "Loans to associates and joint ventures"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A III 5"
    applicable_from_fiscal_year: 1999

mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "Loans to associates/JVs separately disclosed; IFRS aggregates."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:FinansielleAnleggsmidler
    weight: +1
    order: 5
---

## Verbatim text (regnskapsloven § 6-2 A III 5)

> Lån til tilknyttet selskap og felleskontrollert virksomhet
