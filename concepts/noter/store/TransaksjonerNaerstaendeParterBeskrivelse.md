---
concept_id: regnskap-no:TransaksjonerNaerstaendeParterBeskrivelse
namespace: regnskap-no
period_type: duration
balance: null
data_type: textBlockItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Beskrivelse av transaksjoner med nærstående parter"
  - lang: en
    role: standardLabel
    text: "Description of related party transactions"

references:
  - publisher: Stortinget
    document: regnskapsloven
    paragraph: "§ 7-30b"
    applicable_from_fiscal_year: 1999

mappings:
  - to: ifrs-full:DisclosureOfTransactionsBetweenRelatedPartiesExplanatory
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk § 7-30b og IFRS IAS 24 er begrepsmessig like; norsk har snevrere definisjon av nærstående."
---

## Verbatim text (regnskapsloven § 7-30b)

> Beskrivelse av transaksjoner med nærstående parter
