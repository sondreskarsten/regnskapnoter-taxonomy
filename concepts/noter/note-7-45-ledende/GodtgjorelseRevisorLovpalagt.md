---
concept_id: regnskap-no:GodtgjorelseRevisorLovpalagt
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
    text: "Godtgjørelse revisor lovpålagt revisjon"
  - lang: en
    role: standardLabel
    text: "Audit fees — statutory audit"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-45"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:FeesPaidToAuditorAuditOfFinancialStatements
    relation: skos:exactMatch
    quality: exact

---

## Verbatim text (regnskapsloven § 7-45)

> Godtgjørelse revisor lovpålagt revisjon
