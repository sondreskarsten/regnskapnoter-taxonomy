---
concept_id: regnskap-no:RevisorhonorarLovpalagt
namespace: regnskap-no
period_type: duration
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Revisjonshonorar - lovpålagt revisjon"
  - lang: en
    role: standardLabel
    text: "Audit fee - statutory audit"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-45"
    applicable_from_fiscal_year: 1999
mappings:
  - to: ifrs-full:FeesForAuditServices
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-45)

> Revisjonshonorar - lovpålagt revisjon
