---
concept_id: regnskap-no:DriftskostnaderEtterArtSpesifikasjon
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
    text: "Spesifisering av driftskostnader etter art"
  - lang: en
    role: standardLabel
    text: "Operating expenses by nature"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-8b"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "(1) Dersom driftskostnadene ikke er spesifisert etter sin art i resultatregnskapet, skal spesifikasjon foretas etter følgende oppstilling: - - Endring i beholdning av varer under tilvirkning og ferdig tilvirkede varer - - Endring i beholdning av egentilvirkede anleggsmidler - - Varekostnad - - Lønnskostnad - - Avskrivning på varige driftsmidler og immaterielle eiendeler - - Nedskrivning på varige driftsmidler og immaterielle eiendeler - - Annen driftskostnad. (2) § 6-6 om sammenligningstall gjel…"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-8b"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfExpensesByNatureExplanatory
    relation: skos:closeMatch
    quality: approximate
---
