"""Emit WADM-conformant annotations.parquet from per-document extraction outputs.

Each row is one annotation linking a (concept_id, value) pair to its evidence in a
source PDF, expressed as a W3C Web Annotation Data Model record. The producer side
of the contract documented in `docs/consumer-guide.md`.

Input: a directory of extraction JSON files of the form:
    {
      "orgnr": "123456789",
      "fiscal_year": 2023,
      "source_pdf_uri": "gs://brreg-regnskap/raw/123456789/2023.pdf",
      "annotations": [
        {
          "concept_id": "regnskap-no:Aksjekapital",
          "value_numeric": 100000,
          "value_text": null,
          "page": 14,
          "text_quote": "Aksjekapital 100 000",
          "text_quote_prefix": "Egenkapital ",
          "text_quote_suffix": " Annen egenkapital",
          "text_position_start": 24512,
          "text_position_end": 24528,
          "media_fragment": "xywh=120,840,310,42",
          "extraction_method": "gemini-2.5-flash",
          "extraction_confidence": 0.94
        }
      ]
    }

Output: artifacts/annotations.parquet with columns:
    annotation_id, orgnr, fiscal_year, concept_id, value_numeric, value_text,
    source_pdf_uri, page, text_quote, text_quote_prefix, text_quote_suffix,
    text_position_start, text_position_end, media_fragment,
    motivation, target_iri, extraction_method, extraction_confidence, created
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ARTIFACTS = REPO_ROOT / "artifacts"


def _annotation_id(orgnr: str, year: int, concept_id: str, page: int, text_quote: str) -> str:
    h = hashlib.sha256(f"{orgnr}|{year}|{concept_id}|{page}|{text_quote}".encode()).hexdigest()
    return f"ann:{h[:16]}"


def _target_iri(source_pdf_uri: str, page: int) -> str:
    return f"{source_pdf_uri}#page={page}"


def _wadm_record(orgnr: str, year: int, source_pdf_uri: str, ann: dict) -> dict:
    page = ann["page"]
    text_quote = ann["text_quote"]
    return {
        "annotation_id": _annotation_id(orgnr, year, ann["concept_id"], page, text_quote),
        "orgnr": orgnr,
        "fiscal_year": year,
        "concept_id": ann["concept_id"],
        "value_numeric": ann.get("value_numeric"),
        "value_text": ann.get("value_text"),
        "source_pdf_uri": source_pdf_uri,
        "page": page,
        "text_quote": text_quote,
        "text_quote_prefix": ann.get("text_quote_prefix"),
        "text_quote_suffix": ann.get("text_quote_suffix"),
        "text_position_start": ann.get("text_position_start"),
        "text_position_end": ann.get("text_position_end"),
        "media_fragment": ann.get("media_fragment"),
        "motivation": "describing",
        "target_iri": _target_iri(source_pdf_uri, page),
        "extraction_method": ann.get("extraction_method"),
        "extraction_confidence": ann.get("extraction_confidence"),
        "created": ann.get("created"),
    }


def emit(input_dir: Path, output: Path) -> int:
    rows: list[dict] = []
    for json_file in sorted(input_dir.glob("*.json")):
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"  SKIP {json_file.name}: {e}", file=sys.stderr)
            continue
        orgnr = str(data["orgnr"])
        year = int(data["fiscal_year"])
        pdf_uri = data["source_pdf_uri"]
        for ann in data.get("annotations", []):
            rows.append(_wadm_record(orgnr, year, pdf_uri, ann))

    schema = pa.schema([
        ("annotation_id", pa.string()),
        ("orgnr", pa.string()),
        ("fiscal_year", pa.int32()),
        ("concept_id", pa.string()),
        ("value_numeric", pa.float64()),
        ("value_text", pa.string()),
        ("source_pdf_uri", pa.string()),
        ("page", pa.int32()),
        ("text_quote", pa.string()),
        ("text_quote_prefix", pa.string()),
        ("text_quote_suffix", pa.string()),
        ("text_position_start", pa.int64()),
        ("text_position_end", pa.int64()),
        ("media_fragment", pa.string()),
        ("motivation", pa.string()),
        ("target_iri", pa.string()),
        ("extraction_method", pa.string()),
        ("extraction_confidence", pa.float64()),
        ("created", pa.string()),
    ])
    if not rows:
        empty = {f.name: [] for f in schema}
        table = pa.table(empty, schema=schema)
    else:
        table = pa.Table.from_pylist(rows, schema=schema)

    output.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(table, output, compression="zstd")
    print(f"  annotations: {len(rows)} rows -> {output}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Emit WADM annotations parquet.")
    parser.add_argument("--input-dir", type=Path, required=True,
                        help="Directory of per-document extraction JSON files")
    parser.add_argument("--output", type=Path,
                        default=ARTIFACTS / "annotations.parquet")
    args = parser.parse_args()
    if not args.input_dir.exists():
        print(f"MISSING input-dir: {args.input_dir}", file=sys.stderr)
        return 1
    return emit(args.input_dir, args.output)


if __name__ == "__main__":
    sys.exit(main())
