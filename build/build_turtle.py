"""Emit SKOS Turtle from concept and axis sources."""

from __future__ import annotations

import argparse
import os
from datetime import UTC, datetime
from pathlib import Path

from rdflib import DCAT, DCTERMS, OWL, RDF, SKOS, Graph, Literal, Namespace, URIRef
from rdflib.namespace import XSD

from build.parse_concepts import REPO_ROOT, load_axes, load_concepts

RNO = Namespace("https://regnskapnoter-taxonomy/regnskap-no/")
IFRS_FULL = Namespace("https://xbrl.ifrs.org/taxonomy/ifrs-full/")
US_GAAP = Namespace("https://xbrl.fasb.org/us-gaap/")

SCHEME = URIRef("https://regnskapnoter-taxonomy/regnskap-no/Scheme")

RELATION_MAP = {
    "skos:exactMatch": SKOS.exactMatch,
    "skos:closeMatch": SKOS.closeMatch,
    "skos:broadMatch": SKOS.broadMatch,
    "skos:narrowMatch": SKOS.narrowMatch,
    "skos:relatedMatch": SKOS.relatedMatch,
}


def _to_uri(qname: str) -> URIRef:
    if qname.startswith("regnskap-no:"):
        return URIRef(str(RNO) + qname.split(":", 1)[1])
    if qname.startswith("ifrs-full:"):
        return URIRef(str(IFRS_FULL) + qname.split(":", 1)[1])
    if qname.startswith("us-gaap:"):
        return URIRef(str(US_GAAP) + qname.split(":", 1)[1])
    return URIRef(qname)


def build_graph(version: str = "0.1.0") -> Graph:
    g = Graph()
    g.bind("skos", SKOS)
    g.bind("dct", DCTERMS)
    g.bind("dcat", DCAT)
    g.bind("owl", OWL)
    g.bind("regnskap-no", RNO)
    g.bind("ifrs-full", IFRS_FULL)

    g.add((SCHEME, RDF.type, SKOS.ConceptScheme))
    g.add((SCHEME, DCTERMS.title, Literal("Regnskap-NO Noter Concept Scheme", lang="en")))
    g.add((SCHEME, DCTERMS.title, Literal("Regnskap-NO Noter konseptskjema", lang="nb")))
    g.add((SCHEME, DCTERMS.hasVersion, Literal(version)))
    g.add((SCHEME, DCTERMS.issued, Literal(datetime.now(UTC).date().isoformat(), datatype=XSD.date)))
    g.add((SCHEME, DCTERMS.license, URIRef("https://creativecommons.org/licenses/by/4.0/")))

    concepts = load_concepts()
    axes = load_axes()

    for c in concepts:
        fm = c.front_matter
        cid = _to_uri(fm["concept_id"])
        g.add((cid, RDF.type, SKOS.Concept))
        g.add((cid, SKOS.inScheme, SCHEME))
        g.add((cid, SKOS.notation, Literal(fm["concept_id"])))

        g.add((cid, RNO.periodType, Literal(fm["period_type"])))
        if fm.get("balance"):
            g.add((cid, RNO.balance, Literal(fm["balance"])))
        g.add((cid, RNO.dataType, Literal(fm["data_type"])))
        g.add((cid, RNO.substitutionGroup, Literal(fm["substitution_group"])))
        g.add((cid, RNO.abstract, Literal(bool(fm["abstract"]), datatype=XSD.boolean)))
        g.add((cid, RNO.status, Literal(fm["status"])))
        g.add((cid, RNO.introducedVersion, Literal(fm["introduced_version"])))

        if fm["status"] == "deprecated":
            g.add((cid, OWL.deprecated, Literal(True, datatype=XSD.boolean)))
            if fm.get("deprecated_date"):
                g.add((cid, RNO.deprecatedDate, Literal(fm["deprecated_date"], datatype=XSD.date)))
            if fm.get("deprecated_replacement"):
                g.add((cid, DCTERMS.isReplacedBy, _to_uri(fm["deprecated_replacement"])))

        for lab in fm.get("labels") or []:
            if lab["role"] == "standardLabel":
                g.add((cid, SKOS.prefLabel, Literal(lab["text"], lang=lab["lang"])))
            elif lab["role"] == "documentationLabel":
                g.add((cid, SKOS.definition, Literal(lab["text"], lang=lab["lang"])))
            else:
                g.add((cid, SKOS.altLabel, Literal(lab["text"], lang=lab["lang"])))

        for d in fm.get("definitions") or []:
            g.add((cid, SKOS.definition, Literal(d["text"], lang=d["lang"])))

        for m in fm.get("mappings") or []:
            target = m.get("to")
            relation = m.get("relation")
            if target and relation in RELATION_MAP:
                g.add((cid, RELATION_MAP[relation], _to_uri(target)))

        canonical_parent = next(iter(fm.get("parents") or []), None)
        if canonical_parent:
            g.add((cid, SKOS.broader, _to_uri(canonical_parent["parent"])))

    for a in axes:
        fm = a.front_matter
        aid = _to_uri(fm["axis_id"])
        g.add((aid, RDF.type, SKOS.Concept))
        g.add((aid, RDF.type, RNO.Axis))
        g.add((aid, SKOS.inScheme, SCHEME))
        g.add((aid, SKOS.notation, Literal(fm["axis_id"])))
        g.add((aid, RNO.axisKind, Literal(fm["axis_kind"])))

        for lab in fm.get("labels") or []:
            if lab["role"] == "standardLabel":
                g.add((aid, SKOS.prefLabel, Literal(lab["text"], lang=lab["lang"])))

        for m in fm.get("mappings") or []:
            target = m.get("to")
            relation = m.get("relation")
            if target and relation in RELATION_MAP:
                g.add((aid, RELATION_MAP[relation], _to_uri(target)))

        for member in fm.get("members") or []:
            mid = _to_uri(member["id"])
            g.add((mid, RDF.type, SKOS.Concept))
            g.add((mid, RDF.type, RNO.Member))
            g.add((mid, SKOS.inScheme, SCHEME))
            g.add((mid, SKOS.notation, Literal(member["id"])))
            g.add((mid, RNO.memberOf, aid))
            g.add((aid, SKOS.narrower, mid))
            for lab in member.get("labels") or []:
                if lab["role"] == "standardLabel":
                    g.add((mid, SKOS.prefLabel, Literal(lab["text"], lang=lab["lang"])))
            mapping = member.get("mapping") or {}
            mtarget = mapping.get("to")
            mrelation = mapping.get("relation")
            if mtarget and mrelation in RELATION_MAP:
                g.add((mid, RELATION_MAP[mrelation], _to_uri(mtarget)))
    return g


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir", type=Path, default=Path(os.environ.get("RNT_OUT_DIR") or REPO_ROOT / "artifacts")
    )
    parser.add_argument("--version", default="0.1.0")
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    g = build_graph(args.version)
    out_path = args.out_dir / "taxonomy.ttl"
    g.serialize(destination=str(out_path), format="turtle")
    print(f"  taxonomy.ttl  {len(g):>6d} triples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
