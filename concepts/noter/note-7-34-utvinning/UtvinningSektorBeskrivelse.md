---
concept_id: regnskap-no:UtvinningSektorBeskrivelse
namespace: regnskap-no
period_type: duration
balance: null
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 1.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Utvinning av petroleum, kraftproduksjon, gruvedrift – beskrivelse"
  - lang: en
    role: standardLabel
    text: "Extraction sector disclosures"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-34"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Regnskapspliktig som har betydelig virksomhet innen utvinning av petroleum, kraftproduksjon eller gruvedrift, skal gi opplysning om antatte reserver og gjenværende utvinnings- eller utnyttelsesperiode, konsesjonsperiode og andre økonomiske betingelser. Det skal opplyses særskilt om framtidige utgifter til disponering og opprydding."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-34"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfExplorationAndEvaluationAssetsExplanatory
    relation: skos:broadMatch
    quality: approximate
---
