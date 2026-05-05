---
concept_id: regnskap-no:EstimertGjenvarendeTap
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
    text: "Estimert gjenvarende tap"
  - lang: en
    role: standardLabel
    text: "Estimated remaining loss"

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
  - to: ifrs-full:OnerousContractsProvision
    relation: skos:closeMatch
    quality: approximate
    note: "Estimated future loss on ongoing contract; IFRS uses onerous-contract provision."
---

## Verbatim text (NRS 2 kap. 3)

> Estimert gjenvarende tap
