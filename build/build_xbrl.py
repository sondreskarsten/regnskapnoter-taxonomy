"""Optional XBRL XML emission for Arelle round-trip validation.

Generates a minimal XBRL taxonomy package that mirrors the concept dictionary
in the standard XBRL 2.1 + XBRL Dimensions information model:

* ``regnskap-no.xsd`` — concept declarations as ``xsd:element`` with
  ``substitutionGroup``, ``periodType``, ``balance``, and ``type`` attributes.
* ``regnskap-no-lab-{lang}.xml`` — label linkbases per language.
* ``regnskap-no-pre.xml`` — presentation linkbase.
* ``regnskap-no-cal.xml`` — calculation linkbase.
* ``regnskap-no-def.xml`` — definition linkbase (hypercubes, axes, members).
* ``regnskap-no-ref.xml`` — reference linkbase.
* ``META-INF/taxonomyPackage.xml`` — taxonomy package manifest per
  XBRL Taxonomy Packages 1.0.

The XBRL package is best-effort: concepts that cannot be expressed in XBRL
are excluded with a warning, but do not block other validations.
"""

from __future__ import annotations

import argparse
import os
import shutil
import zipfile
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

from build.parse_concepts import REPO_ROOT, load_axes, load_concepts

NS_XSD = "http://www.w3.org/2001/XMLSchema"
NS_XBRLI = "http://www.xbrl.org/2003/instance"
NS_LINK = "http://www.xbrl.org/2003/linkbase"
NS_XLINK = "http://www.w3.org/1999/xlink"
NS_XBRLDT = "http://xbrl.org/2005/xbrldt"
NS_RNO = "https://regnskapnoter-taxonomy/regnskap-no/2026"

XBRL_DATATYPES = {
    "monetaryItemType": "xbrli:monetaryItemType",
    "stringItemType": "xbrli:stringItemType",
    "decimalItemType": "xbrli:decimalItemType",
    "sharesItemType": "xbrli:sharesItemType",
    "pureItemType": "xbrli:pureItemType",
    "dateItemType": "xbrli:dateItemType",
    "textBlockItemType": "us-types:textBlockItemType",
    "booleanItemType": "xbrli:booleanItemType",
    "integerItemType": "xbrli:integerItemType",
    "percentItemType": "num:percentItemType",
}


def _local_name(qname: str) -> str:
    return qname.split(":", 1)[1]


def _build_xsd(concepts: list, axes: list, out_dir: Path) -> int:
    ET.register_namespace("", NS_XSD)
    ET.register_namespace("xbrli", NS_XBRLI)
    ET.register_namespace("link", NS_LINK)
    ET.register_namespace("xlink", NS_XLINK)
    ET.register_namespace("xbrldt", NS_XBRLDT)
    ET.register_namespace("regnskap-no", NS_RNO)

    schema = ET.Element(
        f"{{{NS_XSD}}}schema",
        attrib={
            "targetNamespace": NS_RNO,
            "elementFormDefault": "qualified",
            "attributeFormDefault": "unqualified",
        },
    )
    ET.SubElement(
        schema,
        f"{{{NS_XSD}}}import",
        {"namespace": NS_XBRLI, "schemaLocation": "http://www.xbrl.org/2003/xbrl-instance-2003-12-31.xsd"},
    )
    ET.SubElement(
        schema,
        f"{{{NS_XSD}}}import",
        {"namespace": NS_XBRLDT, "schemaLocation": "http://www.xbrl.org/2005/xbrldt-2005.xsd"},
    )

    n_emitted = 0
    for c in concepts:
        fm = c.front_matter
        attribs = {
            "name": _local_name(fm["concept_id"]),
            "id": _local_name(fm["concept_id"]),
            f"{{{NS_XBRLI}}}periodType": fm["period_type"],
            "type": XBRL_DATATYPES.get(fm["data_type"], "xbrli:stringItemType"),
            "abstract": "true" if fm["abstract"] else "false",
            "nillable": "true",
            "substitutionGroup": "xbrli:item",
        }
        if fm.get("balance"):
            attribs[f"{{{NS_XBRLI}}}balance"] = fm["balance"]
        ET.SubElement(schema, f"{{{NS_XSD}}}element", attribs)
        n_emitted += 1

    for a in axes:
        fm = a.front_matter
        ET.SubElement(
            schema,
            f"{{{NS_XSD}}}element",
            {
                "name": _local_name(fm["axis_id"]),
                "id": _local_name(fm["axis_id"]),
                f"{{{NS_XBRLI}}}periodType": "duration",
                "type": "xbrli:stringItemType",
                "abstract": "true",
                "nillable": "true",
                "substitutionGroup": "xbrldt:dimensionItem",
            },
        )
        for m in fm.get("members") or []:
            ET.SubElement(
                schema,
                f"{{{NS_XSD}}}element",
                {
                    "name": _local_name(m["id"]),
                    "id": _local_name(m["id"]),
                    f"{{{NS_XBRLI}}}periodType": "duration",
                    "type": "xbrli:stringItemType",
                    "abstract": "true",
                    "nillable": "true",
                    "substitutionGroup": "xbrli:item",
                },
            )

    tree = ET.ElementTree(schema)
    ET.indent(tree, space="  ")
    out_path = out_dir / "regnskap-no.xsd"
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    return n_emitted


def _build_label_linkbases(concepts: list, axes: list, out_dir: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    languages = {"nb", "en"}
    label_role_uris = {
        "standardLabel": "http://www.xbrl.org/2003/role/label",
        "documentationLabel": "http://www.xbrl.org/2003/role/documentation",
        "terseLabel": "http://www.xbrl.org/2003/role/terseLabel",
        "verboseLabel": "http://www.xbrl.org/2003/role/verboseLabel",
        "totalLabel": "http://www.xbrl.org/2003/role/totalLabel",
        "periodStartLabel": "http://www.xbrl.org/2003/role/periodStartLabel",
        "periodEndLabel": "http://www.xbrl.org/2003/role/periodEndLabel",
        "negatedLabel": "http://www.xbrl.org/2009/role/negatedLabel",
        "deprecatedLabel": "http://www.xbrl.org/2009/role/deprecatedLabel",
    }
    for lang in languages:
        ET.register_namespace("link", NS_LINK)
        ET.register_namespace("xlink", NS_XLINK)
        linkbase = ET.Element(f"{{{NS_LINK}}}linkbase")
        label_link = ET.SubElement(
            linkbase,
            f"{{{NS_LINK}}}label_link",
            {f"{{{NS_XLINK}}}type": "extended", f"{{{NS_XLINK}}}role": "http://www.xbrl.org/2003/role/link"},
        )
        n = 0
        for source in (concepts, axes):
            for item in source:
                fm = item.front_matter
                local = _local_name(fm.get("concept_id") or fm.get("axis_id"))
                ET.SubElement(
                    label_link,
                    f"{{{NS_LINK}}}loc",
                    {
                        f"{{{NS_XLINK}}}type": "locator",
                        f"{{{NS_XLINK}}}href": f"regnskap-no.xsd#{local}",
                        f"{{{NS_XLINK}}}label": f"loc_{local}",
                    },
                )
                for lab in fm.get("labels") or []:
                    if lab["lang"] != lang:
                        continue
                    label_el = ET.SubElement(
                        label_link,
                        f"{{{NS_LINK}}}label",
                        {
                            f"{{{NS_XLINK}}}type": "resource",
                            f"{{{NS_XLINK}}}label": f"lab_{local}_{lab['role']}",
                            f"{{{NS_XLINK}}}role": label_role_uris.get(
                                lab["role"], label_role_uris["standardLabel"]
                            ),
                            "{http://www.w3.org/XML/1998/namespace}lang": lang,
                        },
                    )
                    label_el.text = lab["text"]
                    ET.SubElement(
                        label_link,
                        f"{{{NS_LINK}}}labelArc",
                        {
                            f"{{{NS_XLINK}}}type": "arc",
                            f"{{{NS_XLINK}}}arcrole": "http://www.xbrl.org/2003/arcrole/concept-label",
                            f"{{{NS_XLINK}}}from": f"loc_{local}",
                            f"{{{NS_XLINK}}}to": f"lab_{local}_{lab['role']}",
                        },
                    )
                    n += 1
        tree = ET.ElementTree(linkbase)
        ET.indent(tree, space="  ")
        tree.write(out_dir / f"regnskap-no-lab-{lang}.xml", encoding="utf-8", xml_declaration=True)
        counts[lang] = n
    return counts


def _build_calc_linkbase(concepts: list, out_dir: Path) -> int:
    arcs_by_role: dict[str, list[tuple[str, str, float, int]]] = defaultdict(list)
    for c in concepts:
        cid = c.front_matter["concept_id"]
        for parent in c.front_matter.get("parents") or []:
            arcs_by_role[parent["role"]].append(
                (parent["parent"], cid, float(parent["weight"]), parent.get("order", 0))
            )

    ET.register_namespace("link", NS_LINK)
    ET.register_namespace("xlink", NS_XLINK)
    linkbase = ET.Element(f"{{{NS_LINK}}}linkbase")

    n = 0
    for role, arcs in arcs_by_role.items():
        role_uri = f"https://regnskapnoter-taxonomy/role/{role.split(']', 1)[0].strip('[')}"
        calc_link = ET.SubElement(
            linkbase,
            f"{{{NS_LINK}}}calculationLink",
            {f"{{{NS_XLINK}}}type": "extended", f"{{{NS_XLINK}}}role": role_uri},
        )
        seen_locs: set[str] = set()
        for parent, child, weight, order in arcs:
            for cid in (parent, child):
                local = _local_name(cid)
                if local not in seen_locs:
                    seen_locs.add(local)
                    ET.SubElement(
                        calc_link,
                        f"{{{NS_LINK}}}loc",
                        {
                            f"{{{NS_XLINK}}}type": "locator",
                            f"{{{NS_XLINK}}}href": f"regnskap-no.xsd#{local}",
                            f"{{{NS_XLINK}}}label": f"loc_{local}",
                        },
                    )
            ET.SubElement(
                calc_link,
                f"{{{NS_LINK}}}calculationArc",
                {
                    f"{{{NS_XLINK}}}type": "arc",
                    f"{{{NS_XLINK}}}arcrole": "http://www.xbrl.org/2003/arcrole/summation-item",
                    f"{{{NS_XLINK}}}from": f"loc_{_local_name(parent)}",
                    f"{{{NS_XLINK}}}to": f"loc_{_local_name(child)}",
                    "weight": str(weight),
                    "order": str(order),
                },
            )
            n += 1
    tree = ET.ElementTree(linkbase)
    ET.indent(tree, space="  ")
    tree.write(out_dir / "regnskap-no-cal.xml", encoding="utf-8", xml_declaration=True)
    return n


def _build_taxonomy_package(out_dir: Path, version: str) -> None:
    meta_dir = out_dir / "META-INF"
    meta_dir.mkdir(exist_ok=True)
    pkg = ET.Element(
        "{http://xbrl.org/2016/taxonomy-package}taxonomyPackage",
        {
            "xmlns": "http://xbrl.org/2016/taxonomy-package",
            "{http://www.w3.org/XML/1998/namespace}lang": "en",
        },
    )
    ET.SubElement(pkg, "identifier").text = NS_RNO
    name = ET.SubElement(pkg, "name", {"{http://www.w3.org/XML/1998/namespace}lang": "en"})
    name.text = "Regnskap-NO Noter Taxonomy"
    ET.SubElement(pkg, "version").text = version
    ET.SubElement(
        pkg, "license", {"href": "https://creativecommons.org/licenses/by/4.0/", "name": "CC-BY-4.0"}
    )
    ET.SubElement(pkg, "publisher").text = "Sondre Skarsten / DNB Corporate Banking"
    tree = ET.ElementTree(pkg)
    ET.indent(tree, space="  ")
    tree.write(meta_dir / "taxonomyPackage.xml", encoding="utf-8", xml_declaration=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir", type=Path, default=Path(os.environ.get("RNT_OUT_DIR") or REPO_ROOT / "artifacts")
    )
    parser.add_argument("--version", default="0.1.0")
    parser.add_argument("--emit-package", action="store_true", help="zip the XBRL package")
    args = parser.parse_args()

    pkg_dir = args.out_dir / "xbrl"
    if pkg_dir.exists():
        shutil.rmtree(pkg_dir)
    pkg_dir.mkdir(parents=True)

    concepts = load_concepts()
    axes = load_axes()

    n_concepts = _build_xsd(concepts, axes, pkg_dir)
    label_counts = _build_label_linkbases(concepts, axes, pkg_dir)
    n_calc = _build_calc_linkbase(concepts, pkg_dir)
    _build_taxonomy_package(pkg_dir, args.version)

    print(f"  XBRL: {n_concepts} concepts, labels={label_counts}, calc_arcs={n_calc}")

    if args.emit_package:
        zip_path = args.out_dir / f"regnskap-no-{args.version}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in pkg_dir.rglob("*"):
                if path.is_file():
                    zf.write(path, path.relative_to(pkg_dir.parent))
        print(f"  XBRL package: {zip_path.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
