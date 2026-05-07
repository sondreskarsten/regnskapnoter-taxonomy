---
concept_id: regnskap-no:EgneAksjerBeholdning
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
    text: "Egne aksjer – beholdning og transaksjoner"
  - lang: en
    role: standardLabel
    text: "Treasury shares – holdings and transactions"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-27"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Dersom egne aksjer ikke vises på egen linje under selskapskapital i balansen, må spesifikasjon gis i note eller i oppstillingen av endringer i egenkapitalen. (1) Dersom egne aksjer ikke vises på egen linje under selskapskapital i balansen, må spesifikasjon gis i note eller i oppstillingen av endringer i egenkapitalen. (2) Aksjeselskap og allmennaksjeselskap som har en beholdning av egne aksjer etter aksjeloven og allmennaksjeloven kapittel 9 , skal opplyse om antallet, aksjenes pålydende verdi o…"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-27"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfTreasurySharesExplanatory
    relation: skos:closeMatch
    quality: approximate
---
