---
concept_id: regnskap-no:InvesteringerIDatterselskap
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
    text: "Investeringer i datterselskap"
  - lang: en
    role: standardLabel
    text: "Investments in subsidiaries"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 6-2 A III 1"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:InvestmentsInSubsidiariesAccountedForUsingEquityMethod
    relation: skos:closeMatch
    quality: approximate
    note: "regnskap-no shows in separate financial statements at cost or equity; IFRS depends on consolidation status."
parents:
  - role: "[620000] Balanse"
    parent: regnskap-no:FinansielleAnleggsmidler
    weight: +1
    order: 1
---

## Verbatim text (regnskapsloven § 6-2 A III 1)

> Investeringer i datterselskap
