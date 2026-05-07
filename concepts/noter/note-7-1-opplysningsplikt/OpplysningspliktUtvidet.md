---
concept_id: regnskap-no:OpplysningspliktUtvidet
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
    text: "Utvidet noteinformasjon"
  - lang: en
    role: standardLabel
    text: "Extended note disclosures"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-1"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "I noter til årsregnskapet skal det gis opplysninger som nevnt i §§ 7-2 til 7-34 . Små foretak kan i stedet gi opplysninger som nevnt i §§ 7-35 til 7-46. (2) I tillegg til opplysninger som nevnt i første ledd skal det gis opplysninger som er nødvendige for å bedømme den regnskapspliktiges eller konsernets stilling og resultat og som ikke fremgår av årsregnskapet for øvrig. Små foretak som ikke utarbeider konsernregnskap kan unnlate å gi slike tilleggsopplysninger om forhold knyttet til konsernets…"
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-1"
    source_version: v2024
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:DisclosureOfNotesAndOtherExplanatoryInformationExplanatory
    relation: skos:broadMatch
    quality: approximate
    note: "IFRS IAS 1 har bredere opplysningsplikt; § 7-1 er NGAAP-spesifikk."
---
