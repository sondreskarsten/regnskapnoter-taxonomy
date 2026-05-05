---
concept_id: regnskap-no:Pensjonsmidler
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
    text: "Pensjonsmidler"
  - lang: en
    role: standardLabel
    text: "Pension assets"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A III 8"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:NetDefinedBenefitAsset
    relation: skos:closeMatch
    quality: approximate
    note: "NRS 6 net pension asset; IFRS IAS 19 uses different actuarial assumptions."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:FinansielleAnleggsmidler
    weight: +1
    order: 8
---

## Verbatim text (regnskapsloven § 6-2 A III 8)

> Pensjonsmidler
