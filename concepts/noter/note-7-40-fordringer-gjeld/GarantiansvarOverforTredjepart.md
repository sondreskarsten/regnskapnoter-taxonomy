---
concept_id: regnskap-no:GarantiansvarOverforTredjepart
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
    text: "Garantiansvar overfor tredjepart"
  - lang: en
    role: standardLabel
    text: "Guarantee liabilities to third parties"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-40"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Fordringer, gjeld, garantiforpliktelser (1) Det skal opplyses hvor stor del av den regnskapspliktiges fordringer som forfaller senere enn ett år etter regnskapsårets slutt. (2) Det skal opplyses hvor stor del av den regnskapspliktiges gjeld som forfaller til betaling mer enn fem år etter regnskapsårets slutt, hvor stor del av den regnskapspliktiges gjeld som er sikret ved pant eller lignende sikkerhet i den regnskapspliktiges eiendeler, og balanseført verdi av de pantsatte eiendeler. (3) Det skal opplyses om summen av garantiforpliktelser som ikke er regnskapsført. Det skal opplyses særskilt dersom slike garantiforpliktelser er sikret ved pant."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-40"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ContingentLiabilitiesIncurredByVentureFromInterestsInJointVentures
    relation: skos:closeMatch
    quality: approximate
    note: "Garantiansvar er en betinget forpliktelse; ifrs-full har lignende konsept under JV-kontekst men ikke en direkte ekvivalent for tredjepartsgarantier."

---

## Verbatim text (regnskapsloven § 7-40)

> Garantiansvar overfor tredjepart
