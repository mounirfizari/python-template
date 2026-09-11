# Contributing

Thanks for considering a contribution! This document covers the setup and
workflow for this project.

## Development setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management
and Python version pinning.

```bash
# Clone and enter the repo
git clone https://github.com/mounirfizari/python-template.git
cd python-template

# Install dependencies (creates .venv automatically)
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

## Running checks locally

```bash
uv run pytest              # tests
uv run mypy                # type check
uv run ruff check .        # lint
uv run ruff format .       # format
uv run pre-commit run --all-files   # everything at once
```

## Workflow

1. Create a branch off `main`: `git checkout -b your-feature`.
2. Make changes. Add tests for new behavior.
3. Ensure `pre-commit run --all-files` and `pytest` pass.
4. Update `CHANGELOG.md` under the `## [Unreleased]` section.
5. Open a PR against `main`. CI must pass before merge.

## Commit messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat: add search endpoint`
- `fix: handle empty user list`
- `docs: clarify install steps`
- `chore: bump ruff to 0.16.6`

## Reporting issues

Open a GitHub issue with a minimal reproduction, your Python version, and
the output of `uv run python -V` and `uv --version`.
