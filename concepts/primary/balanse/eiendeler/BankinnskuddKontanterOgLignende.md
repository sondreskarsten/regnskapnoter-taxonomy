---
concept_id: regnskap-no:BankinnskuddKontanterOgLignende
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
    text: "Bankinnskudd, kontanter o.l."
  - lang: en
    role: standardLabel
    text: "Cash and cash equivalents"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 B IV"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "B. Omløpsmidler"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 6-2 B IV"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:CashAndCashEquivalents
    relation: skos:closeMatch
    quality: approximate
    note: "Substantially identical; minor scope differences in 'kontanter o.l.' vs IAS 7.6."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:Omlopsmidler
    weight: +1
    order: 4
---

## Verbatim text (regnskapsloven § 6-2 B IV)

> Bankinnskudd, kontanter o.l.
