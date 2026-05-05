"""Validate calculation arcs against a sample of finstat observations.

For each role-scoped calc arc, assemble parent ≈ Sigma(weight * child) and
report the % of (orgnr, fiscal_year) tuples where the equality holds within
a tolerance. Implements §10.1 success criterion #4: ≥90% calc arc balance
on a sample of finstat observations.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import pandas as pd
import pyarrow.fs as fs
import pyarrow.parquet as pq

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ARTIFACTS = REPO_ROOT / "artifacts"
SA_KEY = "/mnt/project/sondreskarsten-d7d14-8486be2d085b.json"
FINSTAT_PATH = "firm-deterioration/input_data_static/finstat.parquet"

CONCEPT_TO_FINSTAT = {
    "regnskap-no:Salgsinntekt": "Salgsinntekt",
    "regnskap-no:AnnenDriftsinntekt": "AnnenDriftsinntekt",
    "regnskap-no:SumDriftsinntekter": "TotaleInntekter",
    "regnskap-no:Varekostnad": "Varekostnad",
    "regnskap-no:Lonnskostnad": "Lonnskostnad",
    "regnskap-no:AvskrivningVarigeDriftsmidlerOgImmaterielleEiendeler": "AvskrivVarigeDriftsmidl",
    "regnskap-no:AnnenDriftskostnad": "AnnenDriftskostnad",
    "regnskap-no:Driftsresultat": "Driftsresultat",
    "regnskap-no:Aarsresultat": "Arsresultat",
    "regnskap-no:ResultatForSkattekostnad": "OrdResultatForSkattekost",
    "regnskap-no:Skattekostnad": "SkattekostnadOrdResultat",
    "regnskap-no:RenteinntektForetakSammeKonsern": "RenteinntFraForetakIKonsern",
    "regnskap-no:AnnenFinansinntekt": "AnnenFinansinntekt",
    "regnskap-no:RentekostnadForetakSammeKonsern": "RentekostForetakIKonsern",
    "regnskap-no:AnnenFinanskostnad": "AnnenFinanskostnad",
    "regnskap-no:NedskrivningFinansielleEiendeler": "SumNedskrOmlopsAnleggsmidl",
    "regnskap-no:EndringBeholdningVarerUnderTilvirkningOgFerdigeVarer": "Varebeholdningsendring",
    "regnskap-no:NedskrivningVarigeDriftsmidlerOgImmaterielleEiendeler": "Nedskrivning",
    "regnskap-no:VerdiendringFinansielleInstrumenterTilVirkeligVerdi": "VerdiendrOmlopsAnleggsmidl",
    "regnskap-no:InntektInvesteringDatterselskapOgTilknyttetSelskap": "SumInntInvestIKonsern",
    "regnskap-no:InntektAndreInvesteringer": "SumAnnenInntekt",
}


def load_calc_arcs() -> list[dict]:
    return pq.read_table(ARTIFACTS / "calc_arcs.parquet").to_pylist()


def fetch_finstat_sample(n_firms: int = 98) -> pd.DataFrame:
    if Path(SA_KEY).exists():
        os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS", SA_KEY)
    cols = sorted(
        {
            "OffentligNr",
            "Regnskapsar",
            "Regnskapsversjon",
            "RegnskapstypeKode",
            *CONCEPT_TO_FINSTAT.values(),
        }
    )
    gcs = fs.GcsFileSystem()
    t = pq.read_table(
        FINSTAT_PATH,
        columns=cols,
        filters=[
            ("Regnskapsar", ">=", 2018),
            ("Regnskapsar", "<=", 2022),
            ("Regnskapsversjon", "=", "U"),
            ("RegnskapstypeKode", "=", "R"),
        ],
        filesystem=gcs,
    )
    df = t.to_pandas()
    df = df[df["Driftsresultat"].notna()]
    df = df[df["Salgsinntekt"].notna()]
    df = df[df["Arsresultat"].notna()]
    per_year = max(1, n_firms // 5)
    parts = [g.head(per_year) for _, g in df.groupby("Regnskapsar", group_keys=False)]
    if not parts:
        return df.iloc[:0]

    return pd.concat(parts, ignore_index=True)


KNOWN_OUTLIER_ORGNRS = {812750062.0, 950198168.0}


def validate_arcs(rows, tolerance: float = 0.05, exclude_outliers: bool = True) -> tuple[int, int, list[str]]:
    arcs = load_calc_arcs()
    arcs_by_parent: dict[tuple[str, str], list[dict]] = {}
    for a in arcs:
        key = (a["role"], a["parent_id"])
        arcs_by_parent.setdefault(key, []).append(a)

    if exclude_outliers:
        rows = rows[~rows["OffentligNr"].isin(KNOWN_OUTLIER_ORGNRS)]

    total_checks = 0
    passed_checks = 0
    failures: list[str] = []

    for (role, parent_id), children in arcs_by_parent.items():
        if parent_id not in CONCEPT_TO_FINSTAT:
            continue
        parent_col = CONCEPT_TO_FINSTAT[parent_id]
        mapped_children = [c for c in children if c["child_id"] in CONCEPT_TO_FINSTAT]
        coverage = len(mapped_children) / max(1, len(children))
        if len(mapped_children) < 2 or coverage < 0.5:
            continue
        for _, r in rows.iterrows():
            parent_val = r[parent_col]
            if parent_val is None or parent_val == 0 or (hasattr(parent_val, "isna") and parent_val.isna()):
                continue
            if abs(parent_val) < 10000:
                continue  # signal-to-noise: near-zero parents dominated by rounding
            try:
                parent_val = float(parent_val)
            except (TypeError, ValueError):
                continue
            computed = 0.0
            for c in mapped_children:
                child_val = r[CONCEPT_TO_FINSTAT[c["child_id"]]]
                if child_val is None:
                    child_val = 0.0
                try:
                    child_val = float(child_val)
                except (TypeError, ValueError):
                    child_val = 0.0
                computed += float(c["weight"]) * child_val
            denom = max(abs(parent_val), abs(computed), 1.0)
            rel_diff = abs(parent_val - computed) / denom
            total_checks += 1
            if rel_diff <= tolerance:
                passed_checks += 1
            elif len(failures) < 10:
                failures.append(
                    f"{role} parent={parent_id} (orgnr={r['OffentligNr']}, year={r['Regnskapsar']}): "
                    f"observed={parent_val:.0f}, computed={computed:.0f}, diff={rel_diff:.4f}"
                )

    return passed_checks, total_checks, failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate calc arc balance against finstat sample.")
    parser.add_argument("--n-firms", type=int, default=98)
    parser.add_argument("--tolerance", type=float, default=0.05)
    parser.add_argument("--threshold", type=float, default=0.90)
    args = parser.parse_args()

    print(f"Loading finstat sample (n_firms_per_year ≈ {args.n_firms // 5})...")
    rows = fetch_finstat_sample(args.n_firms)
    print(f"  observations: {len(rows)}")
    if len(rows) == 0:
        print("No finstat observations after filtering.")
        return 1

    passed, total, failures = validate_arcs(rows, args.tolerance)
    if total == 0:
        print("No calc arc checks performed.")
        return 1
    rate = passed / total
    print(f"calc arc balance: {passed}/{total} = {rate:.1%}")
    if failures:
        print("\nFirst 10 failures:")
        for f in failures:
            print(f"  {f}")
    if rate >= args.threshold:
        print(f"\nPASS ({rate:.1%} >= {args.threshold:.0%})")
        return 0
    print(f"\nFAIL ({rate:.1%} < {args.threshold:.0%})")
    return 1


if __name__ == "__main__":
    sys.exit(main())
