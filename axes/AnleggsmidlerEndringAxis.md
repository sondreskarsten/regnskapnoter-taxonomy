---
axis_id: regnskap-no:AnleggsmidlerEndringAxis
namespace: regnskap-no
axis_kind: explicit
status: standard
introduced_version: 0.1.0
default_member: null

labels:
  - lang: nb
    role: standardLabel
    text: "Endringer i anleggsmidler"
  - lang: en
    role: standardLabel
    text: "Changes in non-current assets"

mappings:
  - to: ifrs-full:CarryingAmountAccumulatedDepreciationAmortisationAndImpairmentAndGrossCarryingAmountAxis
    relation: skos:closeMatch

members:
  - id: regnskap-no:AnskaffelseskostInngaendeMember
    parent: null
    order: 1
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Anskaffelseskost inngående"
      - lang: en
        role: standardLabel
        text: "Cost - opening balance"
    mapping:
      to: ifrs-full:GrossCarryingAmountMember
      relation: skos:closeMatch
  - id: regnskap-no:TilgangMember
    parent: null
    order: 2
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Tilgang"
      - lang: en
        role: standardLabel
        text: "Additions"
    mapping:
      to: ifrs-full:IncreaseDecreaseThroughAdditionsPropertyPlantAndEquipmentMember
      relation: skos:closeMatch
  - id: regnskap-no:AvgangMember
    parent: null
    order: 3
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Avgang"
      - lang: en
        role: standardLabel
        text: "Disposals"
    mapping:
      to: ifrs-full:DisposalsPropertyPlantAndEquipmentMember
      relation: skos:closeMatch
  - id: regnskap-no:AnskaffelseskostUtgaendeMember
    parent: null
    order: 4
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Anskaffelseskost utgående"
      - lang: en
        role: standardLabel
        text: "Cost - closing balance"
  - id: regnskap-no:AkkumulerteAvskrivningerInngaendeMember
    parent: null
    order: 5
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Akkumulerte avskrivninger inngående"
      - lang: en
        role: standardLabel
        text: "Accumulated depreciation - opening balance"
    mapping:
      to: ifrs-full:AccumulatedDepreciationAmortisationAndImpairmentMember
      relation: skos:closeMatch
  - id: regnskap-no:AretsAvskrivningMember
    parent: null
    order: 6
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Årets avskrivning"
      - lang: en
        role: standardLabel
        text: "Depreciation for the year"
  - id: regnskap-no:AretsNedskrivningMember
    parent: null
    order: 7
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Årets nedskrivning"
      - lang: en
        role: standardLabel
        text: "Impairment for the year"
  - id: regnskap-no:AretsReverseringNedskrivningMember
    parent: null
    order: 8
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Årets reversering av nedskrivning"
      - lang: en
        role: standardLabel
        text: "Reversal of impairment for the year"
  - id: regnskap-no:BalansefortVerdiUtgaendeMember
    parent: null
    order: 99
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Balanseført verdi utgående"
      - lang: en
        role: standardLabel
        text: "Carrying amount - closing balance"
    mapping:
      to: ifrs-full:CarryingAmountMember
      relation: skos:closeMatch
---

## Editorial notes

The AnleggsmidlerEndringAxis decomposes the anleggsmidler rollforward (§ 7-39) into cost-side movements (anskaffelseskost: opening, additions, disposals, closing) and accumulated-depreciation-side movements (akkumulerte avskrivninger: opening, year's depreciation, year's impairment, year's reversal of impairment, closing carrying amount). When combined with KlassifiseringAvAnleggsmidlerAxis, these axes form the hypercube that represents the complete anleggsmidler note.
