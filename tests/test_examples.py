from __future__ import annotations

import math

import pytest


@pytest.mark.parametrize(
    ("sample_rate", "duration", "expected_len"),
    [
        (1_000, 0.001, 1),
        (1_000_000, 0.001, 1_000),
        (10_000_000, 0.0005, 5_000),
    ],
)
def test_sample_count(sample_rate: int, duration: float, expected_len: int) -> None:
    assert math.floor(sample_rate * duration) == expected_len


@pytest.mark.slow
def test_placeholder_for_slow_function() -> None:
    # Marker registered in pyproject; deselect with `pytest -m "not slow"`.
    assert True
