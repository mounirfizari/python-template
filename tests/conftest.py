from __future__ import annotations

from collections.abc import Iterator

import pytest


@pytest.fixture
def rng_seed() -> int:
    """Standard seed for deterministic ML tests."""
    return 20260910


@pytest.fixture
def tmp_data_dir(tmp_path: pytest.TempPathFactory) -> Iterator[object]:
    """Scratch directory for tests that write files, checkpoints, etc."""
    yield tmp_path
