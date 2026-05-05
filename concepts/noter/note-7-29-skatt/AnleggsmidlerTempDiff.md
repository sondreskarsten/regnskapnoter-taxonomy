---
concept_id: regnskap-no:AnleggsmidlerTempDiff
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
    text: "Anleggsmidler - midlertidig forskjell"
  - lang: en
    role: standardLabel
    text: "PPE - temporary difference"

references:
  - publisher: NRS
    document: Resultatskatt
    paragraph: "kap. 4"
    applicable_from_fiscal_year: 2014
mappings:
  - to: ifrs-full:TemporaryDifferenceMember
    relation: skos:closeMatch
    quality: approximate
    note: "Book-tax temporary difference on non-current assets."
---

## Verbatim text (NRS(F) Resultatskatt kap. 4)

> Anleggsmidler - midlertidig forskjell
