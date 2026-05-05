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

definitions:
  - lang: nb
    role: definition
    text: "Regnskapsprinsipper m.v. (1) Det skal gis opplysninger om anvendte regnskapsprinsipper. (2) Det skal opplyses om sammenligningstallene er omarbeidet. Dersom de omarbeides skal omarbeidingen forklares, jf. § 6-6 ."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-35"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DescriptionOfReportingPeriod
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk og IFRS bruker samme prinsipp om beskrivelse av rapporteringsperiode; ikke alltid eksakt sammenfallende fordi norsk regnskapsår ofte sammenfaller med kalenderår mens IFRS er nøytralt."

---

## Verbatim text (regnskapsloven § 7-35)

> Beskrivelse av regnskapsperioden
