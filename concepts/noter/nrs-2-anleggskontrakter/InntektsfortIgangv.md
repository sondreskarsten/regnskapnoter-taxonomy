---
concept_id: regnskap-no:InntektsfortIgangv
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
    text: "Inntektsført løpende (igangv. kontrakter)"
  - lang: en
    role: standardLabel
    text: "Recognized revenue (ongoing contracts)"

references:
  - publisher: NRS
    document: NRS 2
    paragraph: "kap. 3"
    applicable_from_fiscal_year: 2003
definitions:
  - lang: nb
    role: definition
    text: "3. Standarden omhandler regnskapsføring av anleggskontrakt. Anleggskontrakt brukes som samlebetegnelse på kontraktsfestet tilvirkning av én enkelt eiendel eller flere eiendeler som sammen utgjør en helhet. Standarden gjelder alle regn- skapspliktige. Det gjelder egne regler for små foretak, jf. pkt. 53."
    source_publisher: NRS
    source_document: NRS 2
    source_paragraph: "kap. 3"
    applicable_from_fiscal_year: 2003
    authoritative: true

mappings:
  - to: ifrs-full:RevenueFromConstructionContracts
    relation: skos:closeMatch
    quality: approximate
    note: "NRS 2 percentage-of-completion revenue; IFRS 15 over-time revenue recognition."
---

## Verbatim text (NRS 2 kap. 3)

> Inntektsført løpende (igangv. kontrakter)
