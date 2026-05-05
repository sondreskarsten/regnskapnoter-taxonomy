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


def _read_version() -> str:
    vf = REPO_ROOT / "VERSION"
    return vf.read_text(encoding="utf-8").strip() if vf.exists() else "0.1.0"


def build_graph(version: str | None = None) -> Graph:
    if version is None:
        version = _read_version()
    g = Graph()
    g.bind("skos", SKOS)
    g.bind("dct", DCTERMS)
    g.bind("dcat", DCAT)
    g.bind("owl", OWL)
    g.bind("regnskap-no", RNO)
    g.bind("ifrs-full", IFRS_FULL)

    rd_file = REPO_ROOT / "RELEASE_DATE"
    iso_date = (
        rd_file.read_text(encoding="utf-8").strip()
        if rd_file.exists()
        else datetime.now(UTC).date().isoformat()
    )
    iso_datetime = f"{iso_date}T00:00:00+00:00"
    versioned_scheme = URIRef(f"https://regnskapnoter-taxonomy/regnskap-no/v{version}/Scheme")

    g.add((SCHEME, RDF.type, SKOS.ConceptScheme))
    g.add((SCHEME, OWL.versionIRI, versioned_scheme))
    g.add((SCHEME, DCTERMS.title, Literal("Regnskap-NO Noter Concept Scheme", lang="en")))
    g.add((SCHEME, DCTERMS.title, Literal("Regnskap-NO Noter konseptskjema", lang="nb")))
    g.add(
        (
            SCHEME,
            DCTERMS.description,
            Literal(
                "Concept dictionary for Norwegian financial-statement noter, modeled after XBRL "
                "(information model), SKOS (vocabulary semantics), and W3C Web Annotation Data Model "
                "(downstream annotation layer). Source-of-truth: Markdown + YAML front-matter.",
                lang="en",
            ),
        )
    )
    g.add((SCHEME, DCTERMS.hasVersion, Literal(version)))
    g.add((SCHEME, DCTERMS.issued, Literal(iso_date, datatype=XSD.date)))
    g.add((SCHEME, DCTERMS.modified, Literal(iso_datetime, datatype=XSD.dateTime)))
    g.add((SCHEME, DCTERMS.creator, Literal("Sondre Skarsten")))
    g.add((SCHEME, DCTERMS.publisher, Literal("Sondre Skarsten / DNB Corporate Banking")))
    g.add((SCHEME, DCTERMS.license, URIRef("https://creativecommons.org/licenses/by/4.0/")))
    g.add((SCHEME, DCTERMS.rightsHolder, Literal("Sondre Skarsten")))
    g.add((SCHEME, DCTERMS.language, Literal("nb")))
    g.add((SCHEME, DCTERMS.language, Literal("en")))
    g.add((SCHEME, DCTERMS.conformsTo, URIRef("https://www.w3.org/2009/08/skos-reference/skos.html")))
    g.add((SCHEME, DCTERMS.conformsTo, URIRef("https://www.w3.org/TR/shacl/")))
    g.add(
        (
            SCHEME,
            DCTERMS.conformsTo,
            URIRef(
                "https://www.xbrl.org/Specification/XBRL-2.1/REC-2003-12-31/XBRL-2.1-REC-2003-12-31+corrected-errata-2013-02-20.html"
            ),
        )
    )
    g.add(
        (
            SCHEME,
            DCTERMS.bibliographicCitation,
            Literal(
                f"Skarsten, S. ({iso_date[:4]}). Regnskap-NO Noter Concept Scheme, "
                f"version {version}. https://github.com/sondreskarsten/regnskapnoter-taxonomy"
            ),
        )
    )

    # DCAT Catalog -> Dataset -> Distributions
    catalog = URIRef(f"https://regnskapnoter-taxonomy/regnskap-no/v{version}/catalog")
    dataset = URIRef(f"https://regnskapnoter-taxonomy/regnskap-no/v{version}/dataset")
    g.add((catalog, RDF.type, DCAT.Catalog))
    g.add((catalog, DCTERMS.title, Literal(f"regnskapnoter-taxonomy v{version} catalog", lang="en")))
    g.add((catalog, DCTERMS.publisher, Literal("Sondre Skarsten / DNB Corporate Banking")))
    g.add((catalog, DCTERMS.issued, Literal(iso_date, datatype=XSD.date)))
    g.add((catalog, DCAT.dataset, dataset))

    g.add((dataset, RDF.type, DCAT.Dataset))
    g.add((dataset, DCTERMS.title, Literal(f"regnskapnoter-taxonomy v{version}", lang="en")))
    g.add((dataset, DCTERMS.identifier, Literal(f"regnskapnoter-taxonomy:v{version}")))
    g.add((dataset, DCTERMS.issued, Literal(iso_date, datatype=XSD.date)))
    g.add((dataset, DCTERMS.modified, Literal(iso_datetime, datatype=XSD.dateTime)))
    g.add((dataset, DCTERMS.publisher, Literal("Sondre Skarsten / DNB Corporate Banking")))
    g.add((dataset, DCTERMS.license, URIRef("https://creativecommons.org/licenses/by/4.0/")))
    g.add((dataset, DCTERMS.language, Literal("nb")))
    g.add((dataset, DCTERMS.language, Literal("en")))
    g.add((dataset, DCAT.theme, URIRef("https://eurovoc.europa.eu/4426")))  # accounting
    g.add((dataset, DCAT.keyword, Literal("Norwegian", lang="en")))
    g.add((dataset, DCAT.keyword, Literal("regnskap")))
    g.add((dataset, DCAT.keyword, Literal("noter")))
    g.add((dataset, DCAT.keyword, Literal("XBRL", lang="en")))
    g.add((dataset, DCAT.keyword, Literal("SKOS", lang="en")))
    g.add((dataset, DCAT.landingPage, URIRef("https://github.com/sondreskarsten/regnskapnoter-taxonomy")))

    distros = [
        (
            f"https://regnskapnoter-taxonomy/regnskap-no/v{version}/distribution/turtle",
            "taxonomy.ttl",
            "text/turtle",
            f"https://storage.googleapis.com/regnskapnoter-taxonomy/v{version}/taxonomy.ttl",
        ),
        (
            f"https://regnskapnoter-taxonomy/regnskap-no/v{version}/distribution/jsonld",
            "taxonomy.jsonld",
            "application/ld+json",
            f"https://storage.googleapis.com/regnskapnoter-taxonomy/v{version}/taxonomy.jsonld",
        ),
        (
            f"https://regnskapnoter-taxonomy/regnskap-no/v{version}/distribution/parquet-concepts",
            "concepts.parquet",
            "application/x-parquet",
            f"https://storage.googleapis.com/regnskapnoter-taxonomy/v{version}/concepts.parquet",
        ),
        (
            f"https://regnskapnoter-taxonomy/regnskap-no/v{version}/distribution/parquet-labels",
            "labels.parquet",
            "application/x-parquet",
            f"https://storage.googleapis.com/regnskapnoter-taxonomy/v{version}/labels.parquet",
        ),
        (
            f"https://regnskapnoter-taxonomy/regnskap-no/v{version}/distribution/parquet-mappings",
            "mappings.parquet",
            "application/x-parquet",
            f"https://storage.googleapis.com/regnskapnoter-taxonomy/v{version}/mappings.parquet",
        ),
    ]
    for distro_uri, title, mediatype, access_url in distros:
        d = URIRef(distro_uri)
        g.add((dataset, DCAT.distribution, d))
        g.add((d, RDF.type, DCAT.Distribution))
        g.add((d, DCTERMS.title, Literal(title)))
        g.add((d, DCAT.mediaType, Literal(mediatype)))
        g.add((d, DCAT.accessURL, URIRef(access_url)))
        g.add((d, DCAT.downloadURL, URIRef(access_url)))
        g.add((d, DCTERMS.license, URIRef("https://creativecommons.org/licenses/by/4.0/")))

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
    # Dated IRIs (criterion: SemVer + dated IRIs in published artifacts)
    rno_versioned = Namespace(f"https://regnskapnoter-taxonomy/regnskap-no/v{version}/")
    g.bind(f"rno-v{version.replace('.', '-')}", rno_versioned)
    for s, _, _ in list(g.triples((None, RDF.type, SKOS.Concept))):
        if str(s).startswith(str(RNO)):
            local = str(s).removeprefix(str(RNO))
            dated = URIRef(str(rno_versioned) + local)
            g.add((dated, OWL.sameAs, s))
            g.add((dated, DCTERMS.isVersionOf, s))
            g.add((dated, DCTERMS.hasVersion, Literal(version)))

    return g


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir", type=Path, default=Path(os.environ.get("RNT_OUT_DIR") or REPO_ROOT / "artifacts")
    )
    parser.add_argument("--version", default=None)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    g = build_graph(args.version)
    out_path = args.out_dir / "taxonomy.ttl"
    g.serialize(destination=str(out_path), format="turtle")
    print(f"  taxonomy.ttl  {len(g):>6d} triples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
