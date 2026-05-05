---
axis_id: regnskap-no:EgenkapitalEndringAxis
namespace: regnskap-no
axis_kind: explicit
status: standard
introduced_version: 0.1.0
default_member: null

labels:
  - lang: nb
    role: standardLabel
    text: "Endringer i egenkapital"
  - lang: en
    role: standardLabel
    text: "Changes in equity"

mappings:
  - to: ifrs-full:ChangesInEquityAxis
    relation: skos:closeMatch

members:
  - id: regnskap-no:InngaendeBalanseMember
    parent: null
    order: 1
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Inngående balanse"
      - lang: en
        role: standardLabel
        text: "Opening balance"
    mapping:
      to: ifrs-full:PreviouslyStatedMember
      relation: skos:closeMatch
  - id: regnskap-no:KapitalforhoyelseMember
    parent: null
    order: 2
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Kapitalforhøyelse"
      - lang: en
        role: standardLabel
        text: "Capital increase"
    mapping:
      to: ifrs-full:IncreaseDecreaseThroughIssueOfEquityMember
      relation: skos:closeMatch
  - id: regnskap-no:KapitalnedsettelseMember
    parent: null
    order: 3
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Kapitalnedsettelse"
      - lang: en
        role: standardLabel
        text: "Capital reduction"
    mapping:
      to: null
      relation: null
      note: "IFRS aggregates this with treasury share movements."
  - id: regnskap-no:UtbytteUtdeltMember
    parent: null
    order: 4
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Utbytte utdelt"
      - lang: en
        role: standardLabel
        text: "Dividends paid"
    mapping:
      to: ifrs-full:IncreaseDecreaseThroughDividendsRecognisedAsDistributionsToOwnersMember
      relation: skos:exactMatch
  - id: regnskap-no:AarsresultatAndelMember
    parent: null
    order: 5
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Årsresultat"
      - lang: en
        role: standardLabel
        text: "Profit (loss) for the period"
    mapping:
      to: ifrs-full:IncreaseDecreaseThroughComprehensiveIncomeMember
      relation: skos:closeMatch
  - id: regnskap-no:KonserninternOverforingMember
    parent: null
    order: 6
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Konsernintern overføring"
      - lang: en
        role: standardLabel
        text: "Group internal transfer"
    mapping:
      to: null
      relation: null
      note: "Norwegian-specific intra-group equity transfer."
  - id: regnskap-no:AndreEndringerMember
    parent: null
    order: 7
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Andre endringer"
      - lang: en
        role: standardLabel
        text: "Other changes"
    mapping:
      to: ifrs-full:OtherChangesInEquityMember
      relation: skos:closeMatch
  - id: regnskap-no:UtgaendeBalanseMember
    parent: null
    order: 99
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Utgående balanse"
      - lang: en
        role: standardLabel
        text: "Closing balance"
    mapping:
      to: null
      relation: null
---

## Editorial notes

The EgenkapitalEndringAxis decomposes the equity rollforward into the standard set of movements observed in regnskap noter under § 7-46 and the more detailed disclosures under § 7-26. Combined with EgenkapitalKomponentAxis, the two axes form the hypercube that represents the complete statement of changes in equity.
