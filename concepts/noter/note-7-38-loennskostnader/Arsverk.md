---
concept_id: regnskap-no:Arsverk
namespace: regnskap-no
period_type: duration
data_type: decimalItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Antall årsverk"
  - lang: en
    role: standardLabel
    text: "Number of full-time equivalents"

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
  - to: ifrs-full:AverageNumberOfEmployees
    relation: skos:closeMatch
    quality: approximate
    note: "regnskapsloven uses årsverk (FTE); IFRS uses average number of employees."
---

## Verbatim text (regnskapsloven § 7-38)

> Antall årsverk
