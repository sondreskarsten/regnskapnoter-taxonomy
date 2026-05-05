---
concept_id: regnskap-no:AksjekapitalAntallAksjerKlasse
namespace: regnskap-no
period_type: instant
balance: null
data_type: sharesItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Antall aksjer per klasse"
  - lang: en
    role: standardLabel
    text: "Number of shares by class"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-26"
    applicable_from_fiscal_year: 1999

definitions:
  - lang: nb
    role: definition
    text: "Antall aksjer, aksjeeiere m.v. (1) Aksjeselskap og allmennaksjeselskap skal opplyse om aksjekapitalen og aksjenes pålydende fordelt på hver aksjeklasse. Det skal opplyses om vedtektsbestemmelser om stemmerett. Det skal opplyses om alle rettigheter som kan medføre at det blir utstedt nye aksjer med angivelse av hovedtrekkene i de vilkår som gjelder for retten. (2) Aksjeselskap og allmennaksjeselskap skal opplyse om selskapets 20 største aksjeeiere og deres eierandeler. Opplysning om aksjeeiere som eier under 1 prosent av aksjene kan utelates. (3) Det skal opplyses om aksjer eller andeler i selskapet samt rettigheter til slike, som eies av henholdsvis daglig leder og medlemmer av styret og bedriftsforsamlingen. (4) Foretak av allmenn interesse skal gi opplysninger som nevnt i tredje ledd spesifisert på de enkelte medlemmer av styret og deres personlig nærstående samt de enkelte ledende ansatte og deres personlig nærstående. Som personlig nærstående regnes: 1. ektefelle og en person som vedkommende bor sammen med i ekteskapslignende forhold, 2. mindreårige barn til vedkommende selv, samt mindreårige barn til en person som nevnt i nr. 1 som vedkommende bor sammen med, og 3. foretak der vedkommende selv eller noen som er nevnt i nr. 1 og 2 har slik bestemmende innflytelse som nevnt i § 1-3 annet ledd. (5) Regnskapspliktige som er utstedere med Norge som hjemstat etter verdipapirhandelloven § 5-4 , skal opplyse om vesentlige indirekte aksjebesittelser i selskapet. Aksjebesittelser ..."
    source_publisher: Stortinget
    source_document: regnskapsloven
    source_paragraph: "§ 7-26"
    applicable_from_fiscal_year: 1999
    authoritative: true

mappings:
  - to: ifrs-full:NumberOfSharesIssued
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk § 7-26 krever fordeling per aksjeklasse; ifrs-full har bare aggregert antall."
---

## Verbatim text (regnskapsloven § 7-26)

> Antall aksjer per klasse
