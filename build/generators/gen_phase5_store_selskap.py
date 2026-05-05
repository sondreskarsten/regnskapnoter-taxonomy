"""Generator script for Phase 5 store_selskap noter concepts.

Maps to build_tables column structure for: skatt_aaret, skatt_midlertidige_forskjeller,
pensjon_otp, bankinnskudd_bundne, intern_transaksjoner, anleggskontrakter,
kontingente_forpliktelser, skattefunn, regnskapsprinsipper_flags, styre_signatures.

Runs idempotently. Re-running overwrites existing files in the target folders.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent / "concepts/noter"


def write(
    folder,
    cid,
    label_nb,
    label_en,
    period_type,
    data_type,
    publisher,
    document,
    paragraph,
    applicable_from,
    balance=None,
    parent=None,
    weight=None,
    order=0,
    ifrs_to=None,
    ifrs_relation=None,
    ifrs_quality=None,
    ifrs_note=None,
    abstract=False,
    axes=None,
    role=None,
):
    role = role or f"[800000] Note {folder}"
    parents_block = ""
    if parent and weight is not None:
        parents_block = f'''
parents:
  - role: "{role}"
    parent: {parent}
    weight: {weight:+d}
    order: {order}'''
    mapping_block = ""
    if ifrs_quality == "norwegian_specific":
        mapping_block = f'''
mappings:
  - to: null
    relation: null
    quality: norwegian_specific
    note: "{ifrs_note or "Norwegian-specific concept; no IFRS-Full equivalent."}"'''
    elif ifrs_to:
        note_line = f'\n    note: "{ifrs_note}"' if ifrs_note else ""
        mapping_block = f"""
mappings:
  - to: {ifrs_to}
    relation: {ifrs_relation}
    quality: {ifrs_quality}{note_line}"""
    axes_block = ""
    if axes:
        axes_lines = "\n".join([f"  - axis: {a}\n    closed: true" for a in axes])
        axes_block = f"\naxes:\n{axes_lines}"
    balance_line = f"\nbalance: {balance}" if balance else ""
    content = f"""---
concept_id: regnskap-no:{cid}
namespace: regnskap-no
period_type: {period_type}{balance_line}
data_type: {data_type}
substitution_group: item
abstract: {str(abstract).lower()}
status: standard
introduced_version: 0.1.0

labels:
  - lang: nb
    role: standardLabel
    text: "{label_nb}"
  - lang: en
    role: standardLabel
    text: "{label_en}"

references:
  - publisher: {publisher}
    document: {document}
    paragraph: "{paragraph}"
    applicable_from_fiscal_year: {applicable_from}{mapping_block}{parents_block}{axes_block}
---

## Verbatim text ({document} {paragraph})

> {label_nb}
"""
    out = ROOT / folder / f"{cid}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
