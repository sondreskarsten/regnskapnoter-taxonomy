---
concept_id: regnskap-no:EndringRegnskapsprinsippEffektBelop
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Effekt av endring i regnskapsprinsipp"
  - lang: en
    role: standardLabel
    text: "Effect of change in accounting policy"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-3"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Virkning av endring av regnskapsprinsipp m.v. Det skal opplyses om virkningen av endring av regnskapsprinsipp. Det samme gjelder feil i tidligere årsregnskap og korrigering av slike feil, samt omklassifiseringer. Sammenligningstall og omarbeiding av disse skal forklares."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-3"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:IncreaseDecreaseDueToChangesInAccountingPolicyAndCorrectionsOfPriorPeriodErrorsRetainedEarnings
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konseptet er resultateffekt; ifrs-full er egenkapitaleffekt — verdien er den samme men konteksten er ulik."
---

## Verbatim text (regnskapsloven § 7-3)

> Effekt av endring i regnskapsprinsipp
