---
axis_id: regnskap-no:KlassifiseringAvAnleggsmidlerAxis
namespace: regnskap-no
axis_kind: explicit
status: standard
introduced_version: 0.1.0
default_member: regnskap-no:SumAnleggsmidlerMember

labels:
  - lang: nb
    role: standardLabel
    text: "Klassifisering av anleggsmidler"
  - lang: en
    role: standardLabel
    text: "Classification of non-current assets"

mappings:
  - to: ifrs-full:ClassesOfPropertyPlantAndEquipmentAxis
    relation: skos:broadMatch
    note: "regnskap-no axis covers all anleggsmidler classes (intangible, tangible, financial); IFRS axis is PPE-specific."

members:
  - id: regnskap-no:SumAnleggsmidlerMember
    parent: null
    order: 1
    usable: false
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Sum anleggsmidler"
      - lang: en
        role: standardLabel
        text: "Total non-current assets"
  - id: regnskap-no:ImmaterielleEiendelerMember
    parent: null
    order: 2
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Immaterielle eiendeler"
      - lang: en
        role: standardLabel
        text: "Intangible assets"
  - id: regnskap-no:GoodwillMember
    parent: regnskap-no:ImmaterielleEiendelerMember
    order: 3
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Goodwill"
      - lang: en
        role: standardLabel
        text: "Goodwill"
    mapping:
      to: ifrs-full:GoodwillMember
      relation: skos:exactMatch
  - id: regnskap-no:VarigeDriftsmidlerMember
    parent: null
    order: 4
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Varige driftsmidler"
      - lang: en
        role: standardLabel
        text: "Property, plant and equipment"
  - id: regnskap-no:TomterBygningerOgAnnenFastEiendomMember
    parent: regnskap-no:VarigeDriftsmidlerMember
    order: 5
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Tomter, bygninger og annen fast eiendom"
      - lang: en
        role: standardLabel
        text: "Land, buildings and other real property"
  - id: regnskap-no:MaskinerOgAnleggMember
    parent: regnskap-no:VarigeDriftsmidlerMember
    order: 6
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Maskiner og anlegg"
      - lang: en
        role: standardLabel
        text: "Machinery and plant"
  - id: regnskap-no:DriftslosoreMember
    parent: regnskap-no:VarigeDriftsmidlerMember
    order: 7
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Driftsløsøre"
      - lang: en
        role: standardLabel
        text: "Operating equipment"
  - id: regnskap-no:FinansielleAnleggsmidlerMember
    parent: null
    order: 8
    usable: true
    status: standard
    labels:
      - lang: nb
        role: standardLabel
        text: "Finansielle anleggsmidler"
      - lang: en
        role: standardLabel
        text: "Non-current financial assets"
---

## Editorial notes

The KlassifiseringAvAnleggsmidlerAxis classifies non-current assets along the structural categories defined in regnskapsloven § 6-2 A. The hierarchy uses two levels: the top-level categories (Immaterielle, Varige Driftsmidler, Finansielle) match the I/II/III subdivisions of § 6-2 A; sub-members capture the specific line items within Varige Driftsmidler used in the § 7-39 anleggsmidler-rollforward note.
