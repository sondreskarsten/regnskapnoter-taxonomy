"""Release orchestrator: build all artifacts, compute checksums, generate DCAT manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import UTC, datetime
from pathlib import Path

from build import (
    build_parquet,
    build_turtle,
    build_xbrl,
    check_parquet_rdf_parity,
    validate_jsonschema,
    validate_referential,
    validate_shacl,
)
from build.parse_concepts import REPO_ROOT


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument(
        "--out-dir", type=Path, default=Path(os.environ.get("RNT_OUT_DIR") or REPO_ROOT / "artifacts")
    )
    parser.add_argument("--gcs-bucket", default=None, help="optional GCS bucket; uploads if specified")
    args = parser.parse_args()

    os.environ["RNT_OUT_DIR"] = str(args.out_dir)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    if validate_jsonschema.main() != 0:
        return 1
    if validate_referential.main() != 0:
        return 1

    counts = build_parquet.build_all(args.out_dir)

    g = build_turtle.build_graph(args.version)
    g.serialize(destination=str(args.out_dir / "taxonomy.ttl"), format="turtle")
    g.serialize(destination=str(args.out_dir / "taxonomy.jsonld"), format="json-ld", indent=2)

    if validate_shacl.main() != 0:
        return 1
    if check_parquet_rdf_parity.main() != 0:
        return 1

    build_xbrl.main()

    manifest = {
        "name": "regnskapnoter-taxonomy",
        "version": args.version,
        "issued": datetime.now(UTC).isoformat(),
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "publisher": "Sondre Skarsten / DNB Corporate Banking",
        "counts": counts,
        "distributions": [],
    }
    for path in sorted(args.out_dir.glob("*.parquet")):
        manifest["distributions"].append(
            {
                "name": path.name,
                "format": "application/vnd.apache.parquet",
                "size": path.stat().st_size,
                "sha256": _sha256(path),
            }
        )
    for path in sorted(args.out_dir.glob("taxonomy.*")):
        fmt = "text/turtle" if path.suffix == ".ttl" else "application/ld+json"
        manifest["distributions"].append(
            {"name": path.name, "format": fmt, "size": path.stat().st_size, "sha256": _sha256(path)}
        )
    with (args.out_dir / "release-manifest.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    if args.gcs_bucket:
        from google.cloud import storage

        client = storage.Client()
        bkt = client.bucket(args.gcs_bucket)
        for path in args.out_dir.iterdir():
            if path.is_file():
                for prefix in (f"v{args.version}", "latest"):
                    blob = bkt.blob(f"{prefix}/{path.name}")
                    blob.upload_from_filename(str(path))
        print(f"  uploaded to gs://{args.gcs_bucket}/v{args.version}/ and gs://{args.gcs_bucket}/latest/")

    print(f"Release {args.version} built. {len(manifest['distributions'])} distributions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
