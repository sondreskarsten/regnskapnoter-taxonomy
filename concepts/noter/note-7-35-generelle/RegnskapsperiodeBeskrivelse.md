---
concept_id: regnskap-no:RegnskapsperiodeBeskrivelse
namespace: regnskap-no
period_type: duration
balance: null
data_type: stringItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Beskrivelse av regnskapsperioden"
  - lang: en
    role: standardLabel
    text: "Reporting period description"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-35"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:DescriptionOfReportingPeriod
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk og IFRS bruker samme prinsipp om beskrivelse av rapporteringsperiode; ikke alltid eksakt sammenfallende fordi norsk regnskapsår ofte sammenfaller med kalenderår mens IFRS er nøytralt."

---

## Verbatim text (regnskapsloven § 7-35)

> Beskrivelse av regnskapsperioden
