---
concept_id: regnskap-no:InternFordringerGjeld
namespace: regnskap-no
period_type: instant
balance: debit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Interne fordringer og gjeld"
  - lang: en
    role: standardLabel
    text: "Inter-company receivables and payables"

references:
  - publisher: NRS
    document: NRS 21
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2009
definitions:
  - lang: nb
    role: definition
    text: "4. Årsregnskapet 4.1 Årsregnskapets innhold Årsregnskapet skal inneholde resultatregnskap, balanse og tilleggsopplysninger (noter). Den regnskapspliktige kan velge å benytte skjema RF-1368 Næringsoppgave 5 for foretak med begrenset regnskapsplikt og ikke-regnskapspliktige selskap med deltakerfastsetting som sitt årsregnskap eller å utarbeide et årsregnskap med sammendratte opplysninger fra næringsoppgave 5. Se punkt 6 om oppstillingsplaner for resultatregnskap og balanse og punkt 7 om tilleggsopplysninger (noter). 4.2 Regnskapsåret Regnskapsloven § 1-7 gjelder på samme måte for regnskapspliktige som utarbeider årsregnskapet etter regelen om begrenset regnskapsplikt som for øvrige regnskapspliktige: Regnskapsåret er kalenderåret. Avvikende regnskapsår kan benyttes dersom dette på grunn av sesongmessig virksomhet øker årsregnskapets informasjonsverdi. Regnskapspliktig som er filial eller datterselskap av utenlandsk foretak, kan benytte avvikende regnskapsår for å ha samme regnskapsår som det utenlandske foretaket. Departementet kan i særlige tilfeller ved forskrift eller enkeltvedtak gjøre unntak fra bestemmelsen i første punktum. Den regnskapspliktiges første regnskapsår, første avvikende regnskapsår eller siste avvikende regnskapsår kan være kortere eller lengre enn 12 måneder. Regnskapsåret kan likevel ikke i noe tilfelle være lengre enn 18 måneder. Ved oppløsning slutter regn..."
    source_publisher: NRS
    source_document: NRS 21
    source_paragraph: "kap. 4"
    applicable_from_fiscal_year: 2009
    authoritative: true

mappings:
  - to: ifrs-full:RelatedPartyTransactionsAxis
    relation: skos:closeMatch
    quality: approximate
    note: "Inter-company balances disclosed under § 7-30b; IFRS uses IAS 24 related parties."
---

## Verbatim text (NRS 21 kap. 4)

> Interne fordringer og gjeld
