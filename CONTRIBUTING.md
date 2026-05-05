# Contributing to regnskapnoter-taxonomy

## Adding a New Concept

1. Identify the regnskapsloven paragraph or NRS standard section that authorizes the concept.
2. Create a Markdown file under `concepts/<domain>/<sub-domain>/` with the concept ID as filename.
3. Populate the YAML front-matter per `schemas/concept-frontmatter.schema.json`.
4. Quote the authoritative source verbatim in the Markdown body. Paraphrasing is rejected by CI.
5. Add an entry to `CHANGELOG.md` under the unreleased section.
6. Open a pull request. CI must pass before merge.

## Concept ID Conventions

- Format: `regnskap-no:<UpperCamelCaseName>`
- Norwegian roots, e.g., `Salgsinntekt`, not `SalesRevenue`.
- Drop short connector words (`og`, `i`, `av`, `til`, `for`, `med`).
- One word per concept where possible. Multi-word names join in CamelCase: `LonnskostnadPensjon`.
- Members of an axis end in `Member`: `AksjekapitalMember`.
- Axes end in `Axis`: `EgenkapitalKomponentAxis`.
- Hypercubes end in `Table`: `LonnskostnadTable`.
- Domains (axis roots) end in `Domain`: `EgenkapitalKomponentDomain`.

## Editing an Existing Concept

- Cosmetic changes (typo, label refinement): patch release. Open PR, get review, merge.
- Adding a label in a new language: minor release.
- Adding a reference to a new NRS version: minor release.
- Renaming a concept: forbidden. Deprecate the old concept (set `status: deprecated`, `deprecated_replacement` to the new concept ID) and add a new concept.
- Changing `period_type`, `balance`, or `data_type`: forbidden in patch or minor releases. Requires major version bump.

## Deprecation

A concept moves through `candidate → standard → deprecated → retired`.

- `candidate`: new in a release, not yet operational.
- `standard`: operational. Default.
- `deprecated`: replaced or rendered obsolete. Retains its ID forever. Has `deprecated_date` and (recommended) `deprecated_replacement`.
- `retired`: no longer used in any active fiscal year. ID still reserved.

## Code Contributions

- Python: ruff for formatting and linting. Run `ruff format` and `ruff check` before commit.
- All build scripts have type hints.
- All build scripts have at least one test.
- pre-commit hooks enforce these locally.

## Pull Request Process

1. Branch from `main`.
2. Make changes.
3. Run `pre-commit run --all-files` locally.
4. Push branch and open PR.
5. CI runs lint, schema validation, referential integrity, build, SHACL validation, optional Arelle validation, parity check, and tests.
6. Request review.
7. Merge.

## Releasing

Releases are tagged from `main`. The release workflow builds artifacts and publishes them to GCS.

1. Update `CHANGELOG.md` with the new version's changes.
2. Tag: `git tag -a v<X.Y.Z> -m "Release vX.Y.Z"`.
3. Push tag: `git push origin v<X.Y.Z>`.
4. The release workflow runs automatically.
