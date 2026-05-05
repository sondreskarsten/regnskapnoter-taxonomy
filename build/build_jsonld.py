"""Emit JSON-LD serialization of the taxonomy from the Turtle graph."""

from __future__ import annotations

import argparse
import contextlib
import json
import os
from pathlib import Path

from build.build_turtle import build_graph
from build.parse_concepts import REPO_ROOT

CONTEXT = {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rno": "https://regnskapnoter-taxonomy/regnskap-no/",
    "ifrs-full": "https://xbrl.ifrs.org/taxonomy/2024-03-27/ifrs-full/",
    "us-gaap": "http://fasb.org/us-gaap/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Build JSON-LD artifact.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path(os.environ.get("RNT_OUT_DIR") or REPO_ROOT / "artifacts"),
    )
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    g = build_graph()
    out_path = args.out_dir / "taxonomy.jsonld"
    raw = g.serialize(format="json-ld", indent=2)
    data = json.loads(raw)
    graph_list = data if isinstance(data, list) else data.get("@graph", [data])

    def sort_lists(obj):
        if isinstance(obj, list):
            sorted_list = [sort_lists(x) for x in obj]
            with contextlib.suppress(TypeError):
                sorted_list.sort(key=lambda x: json.dumps(x, sort_keys=True, ensure_ascii=False))
            return sorted_list
        if isinstance(obj, dict):
            return {k: sort_lists(v) for k, v in obj.items()}
        return obj

    graph_list = sort_lists(graph_list)
    graph_list.sort(key=lambda d: (d.get("@id", ""), json.dumps(d, sort_keys=True, ensure_ascii=False)))
    wrapped = {"@context": CONTEXT, "@graph": graph_list}
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(wrapped, f, indent=2, ensure_ascii=False, sort_keys=True)
    print(f"  taxonomy.jsonld  {len(g)} triples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
