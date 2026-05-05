---
concept_id: regnskap-no:EgenkapitalInngaaendeBalanse
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Inngående balanse egenkapital"
  - lang: en
    role: standardLabel
    text: "Equity at start of period"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Fortsatt drift Dersom det er usikkerhet om fortsatt drift, skal det opplyses om usikkerheten. Kapittel 8. Offentlighet, innsendelse av regnskap, straff"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-46"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:Equity
    relation: skos:exactMatch
    quality: exact
    note: "Samme konsept som ifrs-full:Equity, men i rollforward-kontekst som åpningsbalanse."

---

## Verbatim text (regnskapsloven § 7-46)

> Inngående balanse egenkapital
