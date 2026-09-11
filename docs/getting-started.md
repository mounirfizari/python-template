# Getting started

## Prerequisites

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/) installed and on your `PATH`

## Install

<!-- Detailed install instructions go here. -->

```bash
git clone https://github.com/mounirfizari/python-template.git
cd python-template
uv sync
uv run pre-commit install
```

`uv sync` creates a `.venv/` and installs the project plus its `dev`
dependency group. Add other groups (`--group ml`, `--group sigproc`) as
needed for the work you're doing.

## First run

<!-- Replace with the actual first-run command for this project. -->

```bash
uv run python-template
```

## Running the checks

```bash
uv run pytest                       # tests
uv run mypy                         # type check
uv run pre-commit run --all-files   # lint + format + type check + everything
```
