---
concept_id: regnskap-no:AksjekapitalPalydendeVerdi
namespace: regnskap-no
period_type: instant
data_type: decimalItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Pålydende verdi per aksje"
  - lang: en
    role: standardLabel
    text: "Par value per share"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-42"
    applicable_from_fiscal_year: 1999
definitions:
  - lang: nb
    role: definition
    text: "Antall aksjer, aksjeeiere m.v. (1) Har selskapet en beholdning av egne aksjer etter aksjeloven kapittel 9 , skal det opplyses om antallet, aksjenes pålydende verdi og den andel aksjene utgjør av aksjekapitalen. (2) Det skal opplyses om endringer i beholdning av egne aksjer og datterselskapenes beholdning av aksjer i morselskapet i løpet av regnskapsåret. Det skal minst opplyses om: 1. bakgrunnen for erverv som har funnet sted, 2. antall aksjer som er ervervet, vederlag for disse og den andel de utgjør av aksjekapitalen, 3. antall aksjer som er avhendet, vederlag for disse og den andel de utgjør av aksjekapitalen. (3) Samvirkeforetak som har medlemskapitalkonti i samsvar med lov om samvirkeforetak § 29 , skal gi opplysninger om årets utbetaling og avsetning. Det skal også opplyses om eventuelle vedtektsbestemmelser og årsmøtevedtak eller forslag til vedtak knyttet til medlemskapitalkonti."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-42"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ParValuePerShare
    relation: skos:exactMatch
    quality: exact
---

## Verbatim text (regnskapsloven § 7-42)

> Pålydende verdi per aksje
