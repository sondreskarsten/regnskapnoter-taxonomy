---
concept_id: regnskap-no:AvtaleOmSluttvederlag
namespace: regnskap-no
period_type: duration
balance: null
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Avtale om sluttvederlag"
  - lang: en
    role: standardLabel
    text: "Severance agreement"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-45"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Lån og sikkerhetsstillelse til ledende personer, aksjeeiere m.v. Det skal opplyses om samlede lån til og samlet sikkerhetsstillelse til fordel for medlemmer av styret med angivelse av rentesats, hovedvilkår og eventuelle tilbakebetalte, avskrevne eller frafalte beløp. Det samme gjelder for medlemmer av annet administrasjons-, ledelses- eller kontrollorgan."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-45"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:KeyManagementPersonnelCompensationTerminationBenefits
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept er avtale-tekst om sluttvederlag; ifrs-full er kvantitative termination benefits."

---

## Verbatim text (regnskapsloven § 7-45)

> Avtale om sluttvederlag
