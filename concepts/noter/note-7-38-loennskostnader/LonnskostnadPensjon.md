---
concept_id: regnskap-no:LonnskostnadPensjon
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
    text: "Pensjonskostnader"
  - lang: en
    role: standardLabel
    text: "Pension costs"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-38"
    applicable_from_fiscal_year: 1999
definitions:
  - lang: nb
    role: definition
    text: "Spesifisering av resultatregnskapet (1) Poster i oppstillingsplanen for resultatregnskapet som er slått sammen etter § 6-3 annet ledd, skal spesifiseres. Lønnskostnader skal spesifiseres på lønninger, folketrygdavgift, pensjonskostnader og andre ytelser. § 6-6 annet ledd om sammenligningstall gjelder tilsvarende. (2) § 6-6 om sammenligningstall gjelder tilsvarende."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-38"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:PostemploymentBenefitExpenseDefinedBenefitPlans
    relation: skos:closeMatch
    quality: approximate
    note: "NRS 6 pensjonskostnad covers both DB and DC; IFRS-Full splits."
parents:
  - role: "[710000] Note 7-38 Lønnskostnader"
    parent: regnskap-no:Lonnskostnad
    weight: +1
    order: 3
---

## Verbatim text (regnskapsloven § 7-38)

> Pensjonskostnader
