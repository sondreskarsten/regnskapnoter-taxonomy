"""Check Parquet artifacts and RDF Turtle have consistent counts."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pyarrow.parquet as pq
from rdflib import RDF, SKOS

from build.build_turtle import build_graph
from build.parse_concepts import REPO_ROOT


def main() -> int:
    out_dir = Path(os.environ.get("RNT_OUT_DIR") or REPO_ROOT / "artifacts")
    concepts_pq = out_dir / "concepts.parquet"
    if not concepts_pq.exists():
        print(f"Parquet artifacts missing in {out_dir}; run build_parquet first", file=sys.stderr)
        return 1
    n_concepts_pq = pq.read_table(concepts_pq).num_rows
    n_axes_pq = pq.read_table(out_dir / "axes.parquet").num_rows

    g = build_graph()
    n_concepts_rdf = sum(1 for _ in g.subjects(RDF.type, SKOS.Concept))
    expected = (
        n_concepts_pq
        + n_axes_pq
        + sum(pq.read_table(out_dir / "axis_members.parquet").num_rows for _ in [None])
    )
    if n_concepts_rdf != expected:
        print(
            f"Parity mismatch: Parquet has {expected} concept-like entities "
            f"({n_concepts_pq} concepts + {n_axes_pq} axes + members), "
            f"RDF has {n_concepts_rdf}",
            file=sys.stderr,
        )
        return 1
    print(f"  parity: {n_concepts_rdf} concept-like entities in both Parquet and RDF")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
