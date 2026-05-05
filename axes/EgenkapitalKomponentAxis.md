---
axis_id: regnskap-no:EgenkapitalKomponentAxis
namespace: regnskap-no
axis_kind: explicit
status: standard
introduced_version: 0.1.0
default_member: regnskap-no:SumEgenkapitalMember

labels:
  - lang: nb
    role: standardLabel
    text: "Egenkapitalkomponenter"
  - lang: en
    role: standardLabel
    text: "Components of equity"

mappings:
  - to: ifrs-full:ComponentsOfEquityAxis
    relation: skos:closeMatch

members:
  - id: regnskap-no:SumEgenkapitalMember
    parent: null
    order: 1
    usable: false
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Sum egenkapital"
      - lang: en
        role: standardLabel
        text: "Total equity"
  - id: regnskap-no:AksjekapitalMember
    parent: null
    order: 2
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Aksjekapital"
      - lang: en
        role: standardLabel
        text: "Share capital"
    mapping:
      to: ifrs-full:IssuedCapitalMember
      relation: skos:exactMatch
    references:
      - publisher: Stortinget
        document: regnskapsloven
        paragraph: "§ 6-2 C I 1"
  - id: regnskap-no:OvkursMember
    parent: null
    order: 3
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Overkurs"
      - lang: en
        role: standardLabel
        text: "Share premium"
    mapping:
      to: ifrs-full:SharePremiumMember
      relation: skos:exactMatch
  - id: regnskap-no:AnnenInnskuttEgenkapitalMember
    parent: null
    order: 4
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Annen innskutt egenkapital"
      - lang: en
        role: standardLabel
        text: "Other contributed equity"
    mapping:
      to: null
      relation: null
      note: "No direct IFRS-Full equivalent; Norwegian-specific equity component."
  - id: regnskap-no:AnnenEgenkapitalMember
    parent: null
    order: 5
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Annen egenkapital"
      - lang: en
        role: standardLabel
        text: "Retained earnings / other equity"
    mapping:
      to: ifrs-full:RetainedEarningsMember
      relation: skos:closeMatch
      note: "Norwegian 'annen egenkapital' includes retained earnings and other unspecified equity."
  - id: regnskap-no:UdekketTapMember
    parent: null
    order: 6
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Udekket tap"
      - lang: en
        role: standardLabel
        text: "Uncovered loss"
    mapping:
      to: ifrs-full:RetainedEarningsMember
      relation: skos:closeMatch
      note: "Negative retained earnings disclosed separately under regnskapsloven § 6-2 C II."
---

## Verbatim text (regnskapsloven § 6-2 C)

> C. Egenkapital
>   I. Innskutt egenkapital
>     1. Aksjekapital
>     2. Overkurs
>     3. Annen innskutt egenkapital
>   II. Opptjent egenkapital
>     1. Annen egenkapital
>     2. Udekket tap

## Editorial notes

This axis composes the equity-rollforward note (§ 7-46) by allowing each line item in the rollforward (incoming balance, capital increase, dividend, profit allocation, outgoing balance) to be reported per equity component. When combined with EgenkapitalEndringAxis (the changes-in-equity axis), the dimensional structure mirrors ifrs-full:StatementOfChangesInEquity.
