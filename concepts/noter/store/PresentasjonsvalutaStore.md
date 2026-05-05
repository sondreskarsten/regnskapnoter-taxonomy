---
concept_id: regnskap-no:PresentasjonsvalutaStore
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
    text: "Presentasjonsvaluta"
  - lang: en
    role: standardLabel
    text: "Presentation currency"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-2"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Regnskapsprinsipper Det skal gis opplysninger om anvendte regnskapsprinsipper, herunder prinsipper for inntektsføring og omregning av utenlandsk valuta. Endringer i hvilke prinsipper som anvendes skal begrunnes. Forskjellig prinsippanvendelse i selskapsregnskap og konsernregnskap skal opplyses og begrunnes i konsernregnskapet. Det skal gis opplysninger om og begrunnelse for sikringsvurdering, jf. § 4-1 nr. 5. Tilsvarende gjelder eventuell porteføljevurdering. Kontinuitet ved regnskapsføring av konserndannelse eller fusjon skal opplyses og begrunnes."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-2"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DescriptionOfPresentationCurrency
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-2)

> Presentasjonsvaluta
