---
concept_id: regnskap-no:PantsatteEiendelerBeskrivelse
namespace: regnskap-no
period_type: instant
balance: null
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Beskrivelse av pantsatte eiendeler"
  - lang: en
    role: standardLabel
    text: "Description of pledged assets"

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
  - to: ifrs-full:DescriptionOfNatureAndCarryingAmountOfAssetsPledgedAsCollateralForLiabilities
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept er beskrivelse av pantsatte eiendeler; IFRS-Full har lignende men er gruppert under sikkerhetsstillelse."

---

## Verbatim text (regnskapsloven § 7-40)

> Beskrivelse av pantsatte eiendeler
