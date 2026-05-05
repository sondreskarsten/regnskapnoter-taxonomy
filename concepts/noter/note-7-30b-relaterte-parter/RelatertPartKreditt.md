---
concept_id: regnskap-no:RelatertPartKreditt
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
    text: "Kreditt til relatert part"
  - lang: en
    role: standardLabel
    text: "Credit to related party"

references:
  - publisher: NRS
    document: NRS 21
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2009
mappings:
  - to: ifrs-full:LoansAndAdvancesToRelatedParties
    relation: skos:closeMatch
    quality: approximate
    note: "Loans and advances to related parties; aksjeloven § 8-7 and IAS 24."
---

## Verbatim text (NRS 21 kap. 4)

> Kreditt til relatert part
