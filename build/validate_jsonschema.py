"""Validate concept and axis Markdown front-matter against JSON Schemas.

Exits with status 0 on success, status 1 with a list of failures otherwise.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import jsonschema

from build.parse_concepts import REPO_ROOT, load_axes, load_concepts

CONCEPT_SCHEMA_PATH = REPO_ROOT / "schemas" / "concept-frontmatter.schema.json"
AXIS_SCHEMA_PATH = REPO_ROOT / "schemas" / "axis-frontmatter.schema.json"


def _load_schema(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_concepts() -> list[str]:
    schema = _load_schema(CONCEPT_SCHEMA_PATH)
    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
    for c in load_concepts():
        for err in sorted(validator.iter_errors(c.front_matter), key=lambda e: e.path):
            errors.append(
                f"{c.path.relative_to(REPO_ROOT)}: {err.message} (at {'/'.join(str(p) for p in err.path)})"
            )
    return errors


def validate_axes() -> list[str]:
    schema = _load_schema(AXIS_SCHEMA_PATH)
    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []
    for a in load_axes():
        for err in sorted(validator.iter_errors(a.front_matter), key=lambda e: e.path):
            errors.append(
                f"{a.path.relative_to(REPO_ROOT)}: {err.message} (at {'/'.join(str(p) for p in err.path)})"
            )
    return errors


def main() -> int:
    errors = validate_concepts() + validate_axes()
    if errors:
        for e in errors:
            print(f"SCHEMA: {e}", file=sys.stderr)
        print(f"{len(errors)} schema violation(s)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
