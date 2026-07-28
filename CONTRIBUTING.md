# Contributing to ronnies-chokoloade-factory

Thanks for contributing. `ronnies-chokoloade-factory` is a Ramboll monolith owned by the
**Energy** department
(Adam Lagoda, Alex Holmberg, Allan Zimmermann, 7AI, Elina K.)
and follows the Ramboll Developer Platform golden-path standards. These standards
are **non-negotiable** — they are what make the monolith maintainable and green.

## Branching model

Three long-lived branches:

- **`main`** — production. Protected: PR + review + green `gate` check required.
- **`dev`** — integration. **PRs target this branch.**
- **`staging`** — pre-production validation.

All work happens on short-lived branches cut from `dev`, named **exactly** one of:

| Prefix | Use | Example |
| --- | --- | --- |
| `feature/` | New behaviour | `feature/PROJ-142-orders-endpoint` |
| `bug/` | Defect fix | `bug/PROJ-188-empty-cart-crash` |
| `hotfix/` | Urgent production fix | `hotfix/PROJ-201-payment-timeout` |

The pattern is `<type>/<ticket>-<slug>`. Anything that does not match is
rejected — rename your branch.

## Commits

Use [**Conventional Commits**](https://www.conventionalcommits.org/):

```
feat(api): add /orders endpoint
fix(fe): handle empty cart state
test: strengthen resolver isolation property
ci: bump node to 22
```

Scope commits by service dir (`api`, `fe`, `wk`, …) where it helps.

## Pull requests

1. Open the PR **into `dev`**.
2. A review is required, and **CODEOWNERS**
   (`@adam-lagoda` `@Alex793x` `@skadefro` `@LishuaiJing3` `@mitanuriel`) must approve.
3. The **`gate`** check must be **green** before merge — and every affected
   service job must pass.
4. Keep changes scoped: touch one service where possible, so CI stays fast.

## The smart CI — what rebuilds and why

**CI only rebuilds affected services — see `.github/scripts/detect_services.py`.**
The `detect` job diffs your change and resolves it against
[`keel.services.json`](keel.services.json):

- `services/<dir>/…` ⇒ that service **plus its transitive dependents**
  (`depends_on` closure) rebuild.
- A shared path (`.github/`, `keel.services.json`, `libs/`) ⇒ **everything**
  rebuilds.
- Root docs / other paths ⇒ **no** service rebuilds (the `gate` job still runs).
- Unreadable diff or resolver error ⇒ **everything** rebuilds (safe fallback).

The resolver's rules are themselves property-tested in `tests/` — the `gate`
job proves them on every push. Worked examples live in [`docs/ci.md`](docs/ci.md).

## Quality gates (what CI enforces)

- **Root gate:** the resolver property suite (`pytest` at the root) and manifest
  sanity are always green.
- **Per-service gates**, only for affected services, inside `services/<dir>/`:
  - python ⇒ `pytest`, `ruff check`, `black --check`, `mypy`
  - node/react ⇒ `npm ci && npm test && npm run build --if-present`
  - go ⇒ `go vet`, `go test`, `go build`
  - dotnet ⇒ `dotnet test`
  - terraform ⇒ `terraform fmt -check`, `init -backend=false`, `validate`

Run the root gate locally before pushing:

```bash
pip install -e ".[dev]"
pytest
```

## The embedded agent skills

The full standards live as agent skills under `.claude/skills/`
(`monorepo-selective-ci`, `property-based-testing`, `python-clean-code`,
`git-ci-governance`). Point your coding agent at them via `CLAUDE.md` /
`AGENTS.md` and it will follow these rules automatically.
