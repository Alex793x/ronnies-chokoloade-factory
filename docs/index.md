# ronnies-chokoloade-factory

> Verdens bedste italienske chokolade is

Owned by the **Energy** department
(Adam Lagoda, Alex Holmberg, Allan Zimmermann, 7AI, Elina K.).
Generated from the Ramboll Developer Platform (Keel) `monolith-root`
golden-path blueprint.

## Services

| Dir | Type | Language | Path |
| --- | --- | --- | --- |
| `fe` | Frontend | react | `services/fe/` |
| `api` | Backend API | python | `services/api/` |
| `dp` | Data pipeline | python | `services/dp/` |
| `inf` | Infrastructure | terraform | `services/inf/` |

The machine-readable index is `keel.services.json` at the repo root — the CI
resolver's single source of truth.

## Where to go next

- **[How the smart CI works](ci.md)** — detection rules and worked examples.
- **[Contributing](../CONTRIBUTING.md)** — branching, PRs, and the quality gates.
- **`.claude/skills/monorepo-selective-ci/SKILL.md`** — the manifest contract
  and how to add a service.

## Standards, as code

The non-negotiable engineering standards are embedded as AI agent skills under
`.claude/skills/` so any coding agent adopts them automatically:

- **monorepo-selective-ci** — the service manifest contract + selective CI.
- **property-based-testing** — every pure function ships with Hypothesis properties.
- **python-clean-code** — small, typed, lint/format/type-clean functions.
- **git-ci-governance** — `main`/`dev`/`staging` and strict branch naming.
