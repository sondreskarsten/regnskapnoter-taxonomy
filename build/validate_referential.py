"""Cross-file referential integrity checks.

Enforces invariants that span multiple source files and cannot be expressed
in JSON Schema:

* Every ``parents[*].parent`` references an existing concept.
* Every ``axes[*].axis`` references an existing axis.
* Every ``mappings[*].to`` is a well-formed external concept ID.
* Every NRS reference cites a ``(document, version)`` listed in
  ``references/nrs-standards.yaml``.
* Every regnskapsloven reference cites a paragraph listed in
  ``references/regnskapsloven-paragraphs.yaml``.
* Calculation arcs do not form cycles.
* No two concepts share the same ``concept_id``.
* No two axes share the same ``axis_id``.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from collections.abc import Iterable
from typing import Any

from build.parse_concepts import REPO_ROOT, load_all


def _violations() -> list[str]:
    parsed = load_all()
    errors: list[str] = []

    concept_ids = {c.front_matter["concept_id"]: c.path for c in parsed.concepts}
    axis_ids = {a.front_matter["axis_id"]: a.path for a in parsed.axes}

    seen_concepts: dict[str, list[str]] = defaultdict(list)
    for c in parsed.concepts:
        seen_concepts[c.front_matter["concept_id"]].append(str(c.path.relative_to(REPO_ROOT)))
    for cid, paths in seen_concepts.items():
        if len(paths) > 1:
            errors.append(f"DUP_CONCEPT: {cid} appears in {paths}")

    seen_axes: dict[str, list[str]] = defaultdict(list)
    for a in parsed.axes:
        seen_axes[a.front_matter["axis_id"]].append(str(a.path.relative_to(REPO_ROOT)))
    for aid, paths in seen_axes.items():
        if len(paths) > 1:
            errors.append(f"DUP_AXIS: {aid} appears in {paths}")

    nrs_versions: dict[str, set[str]] = {}
    nrs_data = parsed.references.get("nrs-standards", {}) or {}
    for std_key, std_info in nrs_data.items():
        std_doc = std_info.get("title", std_key)
        versions = {v["version"] for v in std_info.get("versions", [])}
        nrs_versions.setdefault(std_key.upper(), set()).update(versions)
        nrs_versions.setdefault(std_doc.upper(), set()).update(versions)

    rl_paragraphs: set[str] = set()
    rl_data = parsed.references.get("regnskapsloven-paragraphs", {}) or {}
    for _chap_key, chap_info in rl_data.items():
        for para in chap_info.get("paragraphs", []) if isinstance(chap_info, dict) else []:
            rl_paragraphs.add(_normalize_paragraph(para.get("paragraph", "")))

    fk_paragraphs: set[str] = set()
    fk_data = parsed.references.get("forskrift-paragraphs", {}) or {}
    for _chap_key, chap_info in fk_data.items():
        for para in chap_info.get("paragraphs", []) if isinstance(chap_info, dict) else []:
            fk_paragraphs.add(_normalize_paragraph(para.get("paragraph", "")))

    parent_arcs: list[tuple[str, str]] = []

    for c in parsed.concepts:
        fm = c.front_matter
        cid = fm["concept_id"]
        rel = c.path.relative_to(REPO_ROOT)

        for parent_arc in fm.get("parents") or []:
            parent_id = parent_arc["parent"]
            if parent_id not in concept_ids:
                errors.append(f"REF_PARENT: {rel}: '{cid}' has parent '{parent_id}' which is not declared")
            parent_arcs.append((cid, parent_id))

        for axis_use in fm.get("axes") or []:
            axis = axis_use["axis"]
            if axis not in axis_ids:
                errors.append(f"REF_AXIS: {rel}: '{cid}' uses axis '{axis}' which is not declared")

        for ref in fm.get("references") or []:
            errors.extend(_check_reference(cid, rel, ref, nrs_versions, rl_paragraphs, fk_paragraphs))

        for definition in fm.get("definitions") or []:
            errors.extend(_check_definition(cid, rel, definition, nrs_versions, rl_paragraphs, fk_paragraphs))

        for mapping in fm.get("mappings") or []:
            errors.extend(_check_mapping(cid, rel, mapping))

    cycle = _find_cycle(parent_arcs)
    if cycle:
        errors.append(f"CYCLE: calculation arcs form a cycle: {' -> '.join(cycle)}")

    return errors


def _normalize_paragraph(p: str) -> str:
    return " ".join(p.replace("\u00a0", " ").strip().split())


def _base_paragraph(p: str) -> str:
    """Extract base paragraph form '§ N-N' from a more specific citation like '§ 6-1 (1) post 1'."""
    m = re.match(r"§\s*\d+-\d+[a-z]?", p)
    return m.group(0).replace("  ", " ").strip() if m else p


def _check_reference(
    cid: str,
    rel: Any,
    ref: dict[str, Any],
    nrs_versions: dict[str, set[str]],
    rl_paragraphs: set[str],
    fk_paragraphs: set[str],
) -> Iterable[str]:
    publisher = ref.get("publisher", "")
    document = ref.get("document", "")
    paragraph = _normalize_paragraph(ref.get("paragraph", ""))
    version = ref.get("version")

    if publisher == "Stortinget":
        if document == "regnskapsloven":
            base_para = _base_paragraph(paragraph)
            if rl_paragraphs and paragraph not in rl_paragraphs and base_para not in rl_paragraphs:
                yield f"REF_RL: {rel}: '{cid}' cites regnskapsloven '{paragraph}' (base '{base_para}') which is not in registry"
        elif document.startswith("forskrift"):
            base_para = _base_paragraph(paragraph)
            if fk_paragraphs and paragraph not in fk_paragraphs and base_para not in fk_paragraphs:
                yield f"REF_FK: {rel}: '{cid}' cites forskrift '{paragraph}' (base '{base_para}') which is not in registry"
    elif publisher == "NRS":
        candidates = (document.upper(), document.upper().replace(" ", "-"))
        version_set: set[str] = set()
        for cand in candidates:
            if cand in nrs_versions:
                version_set = nrs_versions[cand]
                break
        if not version_set:
            yield f"REF_NRS: {rel}: '{cid}' cites NRS document '{document}' not listed in nrs-standards.yaml"
        elif version is not None and version not in version_set:
            yield (
                f"REF_NRS_VERSION: {rel}: '{cid}' cites NRS '{document}' version '{version}' "
                f"not listed in nrs-standards.yaml (have: {sorted(version_set)})"
            )


def _check_definition(
    cid: str,
    rel: Any,
    definition: dict[str, Any],
    nrs_versions: dict[str, set[str]],
    rl_paragraphs: set[str],
    fk_paragraphs: set[str],
) -> Iterable[str]:
    pseudo_ref = {
        "publisher": definition.get("source_publisher", ""),
        "document": definition.get("source_document", ""),
        "paragraph": definition.get("source_paragraph", ""),
        "version": definition.get("source_version"),
    }
    yield from _check_reference(cid, rel, pseudo_ref, nrs_versions, rl_paragraphs, fk_paragraphs)


def _check_mapping(cid: str, rel: Any, mapping: dict[str, Any]) -> Iterable[str]:
    target = mapping.get("to")
    relation = mapping.get("relation")
    quality = mapping.get("quality")
    note = mapping.get("note")

    if quality == "norwegian_specific":
        if target is not None or relation is not None:
            yield f"MAP_NORSPEC: {rel}: '{cid}' marked norwegian_specific but has target/relation"
        return

    if target is None or relation is None:
        yield f"MAP_INCOMPLETE: {rel}: '{cid}' mapping missing target or relation"
        return

    if not target.startswith(("ifrs-full:", "us-gaap:")):
        yield f"MAP_NS: {rel}: '{cid}' mapping target '{target}' uses unknown namespace"

    if quality == "approximate" and not (note and note.strip()):
        yield f"MAP_APPROX_NOTE: {rel}: '{cid}' mapping is approximate but has no explanatory note"


def _find_cycle(arcs: list[tuple[str, str]]) -> list[str]:
    graph: dict[str, list[str]] = defaultdict(list)
    for child, parent in arcs:
        graph[child].append(parent)
    visited: set[str] = set()
    on_stack: set[str] = set()
    path: list[str] = []

    def dfs(node: str) -> list[str] | None:
        if node in on_stack:
            idx = path.index(node)
            return [*path[idx:], node]
        if node in visited:
            return None
        visited.add(node)
        on_stack.add(node)
        path.append(node)
        for nxt in graph.get(node, []):
            cyc = dfs(nxt)
            if cyc:
                return cyc
        on_stack.remove(node)
        path.pop()
        return None

    for node in list(graph):
        cyc = dfs(node)
        if cyc:
            return cyc
    return []


def main() -> int:
    errors = _violations()
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"{len(errors)} referential violation(s)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
