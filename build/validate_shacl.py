"""Validate the RDF projection against SHACL shapes."""

from __future__ import annotations

import sys

import pyshacl

from build.build_turtle import build_graph
from build.parse_concepts import REPO_ROOT

SHAPES_PATH = REPO_ROOT / "schemas" / "shapes.ttl"


def main() -> int:
    data_graph = build_graph()
    if not SHAPES_PATH.exists():
        print(f"SHACL shapes not found at {SHAPES_PATH}", file=sys.stderr)
        return 1
    shapes_text = SHAPES_PATH.read_text(encoding="utf-8")
    conforms, _, results_text = pyshacl.validate(
        data_graph,
        shacl_graph=shapes_text,
        shacl_graph_format="turtle",
        inference="rdfs",
        meta_shacl=False,
        debug=False,
    )
    if not conforms:
        print(results_text, file=sys.stderr)
        return 1
    print("  SHACL: 0 violations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
