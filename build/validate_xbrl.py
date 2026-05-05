"""Validate the XBRL XSD package using arelle.

Loads `artifacts/xbrl/regnskap-no.xsd` and reports XBRL conformance errors.
Exits non-zero on any errors.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
XSD_PATH = REPO_ROOT / "artifacts" / "xbrl" / "regnskap-no.xsd"


def main() -> int:
    if not XSD_PATH.exists():
        print(f"MISSING: {XSD_PATH}; run `python -m build.build_xbrl` first", file=sys.stderr)
        return 1

    try:
        from arelle import Cntlr
    except ImportError:
        print("arelle not installed; install with: pip install arelle-release", file=sys.stderr)
        return 1

    ctrl = Cntlr.Cntlr(logFileName="logToBuffer")
    ctrl.webCache.workOffline = False
    model = ctrl.modelManager.load(str(XSD_PATH.resolve()))

    errors: list[str] = []
    warnings_count = 0
    for log in ctrl.logHandler.logRecordBuffer:
        msg = log.getMessage() if hasattr(log, "getMessage") else str(log)
        if log.levelname in ("ERROR", "CRITICAL"):
            errors.append(msg)
        elif log.levelname == "WARNING":
            warnings_count += 1

    n_concepts = len(model.qnameConcepts) if model else 0
    print(f"  XBRL: {n_concepts} concepts loaded, {len(errors)} errors, {warnings_count} warnings")

    for e in errors[:10]:
        print(f"  ERROR: {e}", file=sys.stderr)

    ctrl.close()
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
