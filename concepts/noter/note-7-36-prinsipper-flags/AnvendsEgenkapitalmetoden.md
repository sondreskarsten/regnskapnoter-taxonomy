---
concept_id: regnskap-no:AnvendsEgenkapitalmetoden
namespace: regnskap-no
period_type: duration
data_type: booleanItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Anvender egenkapitalmetoden"
  - lang: en
    role: standardLabel
    text: "Uses equity method"

references:
  - publisher: NRS
    document: NRS 17
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2018
definitions:
  - lang: nb
    role: definition
    text: "4. Former for konserndannelse Et konsernforhold kan oppstå ved at morselskapet kjøper en kontrollerende eierandel i et selskap, ved nydannelse, eller ved rettet emisjon, kapitalnedsettelse eller fisjon i et eksisterende selskap, eller ved tilbakekjøp av egne aksjer som øker morselskapets eierandel. Konsernforhold kan i tillegg oppstå ved inngåelse av avtale eller ved andre forhold som gir morselskapet kontroll."
    source_publisher: NRS
    source_document: NRS 17
    source_paragraph: "kap. 4"
    applicable_from_fiscal_year: 2018
    authoritative: true

mappings:
  - to: ifrs-full:DescriptionOfWhetherEntityHasInterestsInUnconsolidatedStructuredEntities
    relation: skos:closeMatch
    quality: approximate
    note: "Equity method election; IFRS via IAS 28."
---

## Verbatim text (NRS 17 kap. 4)

> Anvender egenkapitalmetoden
