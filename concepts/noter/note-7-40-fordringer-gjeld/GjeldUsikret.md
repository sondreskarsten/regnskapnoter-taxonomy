---
concept_id: regnskap-no:GjeldUsikret
namespace: regnskap-no
period_type: instant
balance: credit
data_type: monetaryItemType
substitution_group: item
abstract: false
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "Gjeld uten sikkerhet"
  - lang: en
    role: standardLabel
    text: "Unsecured debt"

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
  - to: ifrs-full:UnsecuredBankLoansReceived
    relation: skos:closeMatch
    quality: approximate
    note: "Norsk konsept dekker all usikret gjeld; ifrs-full splitter etter motpartstype."

---

## Verbatim text (regnskapsloven § 7-40)

> Gjeld uten sikkerhet
