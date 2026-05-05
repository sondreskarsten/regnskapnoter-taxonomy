"""Pre-commit hook: forbid concept_id renames.

A concept's ``concept_id`` is forever. Once published, a rename is forbidden.
This hook compares the front-matter of staged files against the version in
``HEAD`` and refuses commits that change ``concept_id`` or ``axis_id``.

Skipped during the initial commit (when ``HEAD`` does not yet exist).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml


def _git_show(rev: str, path: str) -> str | None:
    """Return file contents at given rev, or None if file does not exist there."""
    result = subprocess.run(
        ["git", "show", f"{rev}:{path}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def _front_matter_id(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None
    return fm.get("concept_id") or fm.get("axis_id")


def _staged_files() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=AM"],
        capture_output=True,
        text=True,
        check=False,
    )
    return [
        line.strip()
        for line in result.stdout.splitlines()
        if (line.startswith("concepts/") or line.startswith("axes/")) and line.endswith(".md")
    ]


def main() -> int:
    head_check = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    if head_check.returncode != 0:
        return 0  # initial commit, nothing to compare against

    violations: list[str] = []
    for path in _staged_files():
        new_text = Path(path).read_text(encoding="utf-8") if Path(path).exists() else ""
        old_text = _git_show("HEAD", path) or ""
        new_id = _front_matter_id(new_text)
        old_id = _front_matter_id(old_text)
        if old_id and new_id and old_id != new_id:
            violations.append(f"{path}: concept/axis ID changed from '{old_id}' to '{new_id}'")
    if violations:
        for v in violations:
            print(f"RENAME: {v}", file=sys.stderr)
        print("Concept/axis IDs are immutable. Deprecate the old ID and add a new concept.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
