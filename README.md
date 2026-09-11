# Python Project Template

Template repo for modern Python projects. Includes uv-based dependency management, ruff linting, mypy type checking, pre-commit hooks, Conventional Commits and Semantic Versioning, and a basic GitHub CI workflow that enforces several of the above. Use this as the working starting point for future Python projects.

## What's included

- **Packaging & environments** — [uv](https://docs.astral.sh/uv/) for
  dependency management, lockfile, and Python-version pinning
- **Linting & formatting** — [ruff](https://docs.astral.sh/ruff/) with a
  medium-strict rule set
- **Type checking** — [mypy](https://mypy.readthedocs.io/) in strict mode
- **Testing** — [pytest](https://docs.pytest.org/) with coverage
- **Pre-commit hooks** — ruff, mypy, codespell, gitleaks, commitizen, and the
  standard file-hygiene set
- **CI** — GitHub Actions workflow that runs the full pre-commit suite and the
  test matrix across Python 3.10–3.13
- **Conventional Commits** enforced via commitizen; **Semantic Versioning**
  tracked in `CHANGELOG.md`


## Requirements

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/) on your `PATH`

## Quick start

```bash
git clone https://github.com/mounirfizari/python-template.git
cd python-template
uv sync
uv run pre-commit install
```

Verify everything works:

```bash
uv run pytest
uv run pre-commit run --all-files
```

## Using this as a template

1. Click **Use this template** on GitHub (or clone and re-init git).
2. Rename `python_template` in `src/`, `pyproject.toml`, and `tests/` to your
   project name.
3. Replace this README, fill in `LICENSE`, and update `pyproject.toml`
   metadata (`name`, `description`, `authors`).
4. Delete the placeholder ADR and start writing real ones.
5. Push, and CI runs on the first commit.

## Project layout
```
.
├── src/python_template/    # package source
├── tests/                  # pytest suite
├── docs/                   # documentation
├── .github/workflows/      # CI
├── pyproject.toml          # project + tool config
├── uv.lock                 # locked dependencies
└── .pre-commit-config.yaml # hook definitions
```

## Documentation

See [`docs/`](docs/index.md) for the full documentation.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

See [`LICENSE`](LICENSE).
