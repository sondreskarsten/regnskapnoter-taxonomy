---
concept_id: regnskap-no:DatterselskapResultatandel
namespace: regnskap-no
period_type: duration
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Datterselskaps resultatandel"
  - lang: en
    role: standardLabel
    text: "Subsidiary share of profit"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-15"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Datterselskap, tilknyttet selskap m.v. (1) Det skal opplyses om foretaksnavn, forretningskontor, eierandel og stemmeandel for datterselskap, tilknyttet selskap og felles kontrollert virksomhet. (2) For datterselskap og tilknyttet selskap skal det gis opplysninger om egenkapitalen og resultatet ifølge siste årsregnskap. Dette gjelder likevel ikke datterselskap som er konsolidert eller er regnskapsført etter egenkapitalmetoden i selskapsregnskapet, eller tilknyttet selskap som er regnskapsført etter egenkapitalmetoden. (3) Regnskapspliktig som er datterselskap, skal opplyse om foretaksnavn og forretningskontor for morselskap som utarbeider konsernregnskap der den regnskapspliktige inngår i konsolideringen. Det skal opplyses hvor en kan få utlevert konsernregnskapene. (4) Dersom datterselskap er utelatt fra konsolideringen etter § 3-8 , skal dette opplyses og begrunnes. (5) I konsernregnskapet skal det opplyses om navnet på foretak der den regnskapspliktige selv eller gjennom datterselskaper eier så mange aksjer eller andeler at de representerer flertallet av stemmene i foretaket, men som ikke er datterselskap fordi det klart kan påvises at slikt eierskap likevel ikke gir bestemmende innflytelse, jf. § 1-3 annet ledd nr. 1. Det skal opplyses om de forhold som påviser at slikt eierskap likevel ikke gir bestemmende innflytelse."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-15"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:ProfitLossFromContinuingOperations
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk EK-metode resultatandel; mappes løst til IFRS profit/loss-konsept."
---

## Verbatim text (regnskapsloven § 7-15)

> Datterselskaps resultatandel
