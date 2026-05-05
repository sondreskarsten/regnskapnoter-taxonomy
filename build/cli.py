"""rnt-build entry point — runs the full build pipeline."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from build import (
    build_jsonld,
    build_parquet,
    build_turtle,
    check_parquet_rdf_parity,
    validate_jsonschema,
    validate_referential,
    validate_shacl,
)
from build.parse_concepts import REPO_ROOT


def _run_module(module_main, args: list[str]) -> int:
    saved = sys.argv
    sys.argv = [saved[0], *args]
    try:
        return module_main()
    finally:
        sys.argv = saved


def main() -> int:
    parser = argparse.ArgumentParser(prog="rnt-build", description="Build regnskapnoter-taxonomy artifacts.")
    parser.add_argument(
        "--out-dir", type=Path, default=Path(os.environ.get("RNT_OUT_DIR") or REPO_ROOT / "artifacts")
    )
    parser.add_argument("--version", default="0.1.0")
    parser.add_argument("--skip-shacl", action="store_true")
    args = parser.parse_args()

    os.environ["RNT_OUT_DIR"] = str(args.out_dir)

    print("[1/6] JSON Schema validation")
    if validate_jsonschema.main() != 0:
        return 1

    print("[2/6] Referential integrity validation")
    if validate_referential.main() != 0:
        return 1

    print("[3/6] Build Parquet artifacts")
    counts = build_parquet.build_all(args.out_dir)
    for name, n in sorted(counts.items()):
        print(f"        {name}.parquet  {n:>6d} rows")

    print("[4/6] Build Turtle and JSON-LD")
    g = build_turtle.build_graph(args.version)
    g.serialize(destination=str(args.out_dir / "taxonomy.ttl"), format="turtle")
    g.serialize(destination=str(args.out_dir / "taxonomy.jsonld"), format="json-ld", indent=2)
    print(f"        taxonomy.ttl / taxonomy.jsonld  {len(g):>6d} triples")
    _ = build_jsonld

    if not args.skip_shacl:
        print("[5/6] SHACL validation")
        if _run_module(validate_shacl.main, ["--out-dir", str(args.out_dir)]) != 0:
            return 1
    else:
        print("[5/6] SHACL validation (skipped)")

    print("[6/6] Parquet/RDF parity check")
    if _run_module(check_parquet_rdf_parity.main, ["--out-dir", str(args.out_dir)]) != 0:
        return 1

    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
