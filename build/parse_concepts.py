"""Parse Markdown source files into in-memory dictionaries.

Each concept is one Markdown file with YAML front-matter delimited by ``---``.
The body of the Markdown file is the human-readable content (verbatim source
quotations and editorial notes); the YAML front-matter carries all structured
metadata that drives the build artifacts.

This module exposes three loaders: :func:`load_concepts`, :func:`load_axes`,
and :func:`load_all`. All three return plain Python dicts suitable for further
processing by the Parquet, Turtle, and JSON-LD builders.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONCEPTS_DIR = REPO_ROOT / "concepts"
AXES_DIR = REPO_ROOT / "axes"
REFERENCES_DIR = REPO_ROOT / "references"

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)


@dataclass
class ConceptFile:
    path: Path
    front_matter: dict[str, Any]
    body: str


@dataclass
class AxisFile:
    path: Path
    front_matter: dict[str, Any]
    body: str


@dataclass
class ParseResult:
    concepts: list[ConceptFile] = field(default_factory=list)
    axes: list[AxisFile] = field(default_factory=list)
    references: dict[str, dict[str, Any]] = field(default_factory=dict)


def parse_markdown_file(path: Path) -> tuple[dict[str, Any], str]:
    """Split a Markdown file into YAML front-matter and body.

    Raises :class:`ValueError` if the file does not begin with a front-matter
    block or if the YAML cannot be parsed.
    """
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if match is None:
        raise ValueError(f"{path}: missing YAML front-matter delimited by '---'")
    fm_text, body = match.groups()
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as exc:
        raise ValueError(f"{path}: YAML parse error: {exc}") from exc
    if not isinstance(fm, dict):
        raise ValueError(f"{path}: front-matter is not a mapping")
    return fm, body


def load_concepts(root: Path | None = None) -> list[ConceptFile]:
    root = root or CONCEPTS_DIR
    out: list[ConceptFile] = []
    if not root.exists():
        return out
    for md_path in sorted(root.rglob("*.md")):
        fm, body = parse_markdown_file(md_path)
        out.append(ConceptFile(path=md_path, front_matter=fm, body=body))
    return out


def load_axes(root: Path | None = None) -> list[AxisFile]:
    root = root or AXES_DIR
    out: list[AxisFile] = []
    if not root.exists():
        return out
    for md_path in sorted(root.rglob("*.md")):
        fm, body = parse_markdown_file(md_path)
        out.append(AxisFile(path=md_path, front_matter=fm, body=body))
    return out


def load_references(root: Path | None = None) -> dict[str, dict[str, Any]]:
    root = root or REFERENCES_DIR
    out: dict[str, dict[str, Any]] = {}
    if not root.exists():
        return out
    for yaml_path in sorted(root.glob("*.yaml")):
        with yaml_path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        out[yaml_path.stem] = data
    return out


def load_all() -> ParseResult:
    return ParseResult(
        concepts=load_concepts(),
        axes=load_axes(),
        references=load_references(),
    )


def iter_concept_ids(concepts: Iterable[ConceptFile]) -> list[str]:
    return [c.front_matter["concept_id"] for c in concepts]


def iter_axis_ids(axes: Iterable[AxisFile]) -> list[str]:
    return [a.front_matter["axis_id"] for a in axes]


if __name__ == "__main__":
    result = load_all()
    print(f"concepts: {len(result.concepts)}")
    print(f"axes: {len(result.axes)}")
    print(f"reference registries: {sorted(result.references.keys())}")
