# Skosmos Deployment Guide

This taxonomy is published as Skosmos-compatible Turtle (`taxonomy.ttl`) with full SKOS semantics. Any Skosmos instance can host it.

## Quick deploy via Docker

```bash
docker run -d --name skosmos \
  -p 9090:80 \
  -e SKOSMOS_VOCABULARIES_BASE_URL=https://skosmos.example.org/ \
  natlibfi/skosmos:latest
```

## Vocabulary configuration

Add to Skosmos `config-vocabularies.ttl`:

```turtle
@prefix skosmos: <http://purl.org/net/skosmos#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix void: <http://rdfs.org/ns/void#> .

:regnskap-no a skosmos:Vocabulary ;
    dct:title "Regnskap-NO Noter Concept Scheme"@en, "Regnskap-NO Noter konseptskjema"@nb ;
    skosmos:shortName "regnskap-no" ;
    skosmos:vocabularyURI "https://regnskapnoter-taxonomy/regnskap-no/Scheme" ;
    skosmos:language "nb", "en" ;
    skosmos:defaultLanguage "nb" ;
    void:dataDump <https://storage.googleapis.com/regnskapnoter-taxonomy/latest/taxonomy.ttl> ;
    skosmos:groupClass skos:Collection ;
    skosmos:fullAlphabeticalIndex true ;
    skosmos:showStatistics true ;
    skosmos:fullSearch true .
```

## Verification

After deploy, verify these queries work:

- Concept lookup: `https://skosmos.example.org/regnskap-no/page/Aksjekapital`
- Search: `https://skosmos.example.org/regnskap-no/search?clang=nb&q=skatt*`
- SPARQL endpoint: `https://skosmos.example.org/regnskap-no/sparql`

## Refresh strategy

The taxonomy publishes new versions to `gs://regnskapnoter-taxonomy/v{X.Y.Z}/` and `gs://regnskapnoter-taxonomy/latest/`. Skosmos's `void:dataDump` should point at `latest/` for tracking head, or pin to a specific `v1.0.X/` for stable references.
