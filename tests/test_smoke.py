from __future__ import annotations

import pytest


def test_package_imports() -> None:
    import python_template

    assert hasattr(python_template, "main")


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    from python_template import main

    main()
    captured = capsys.readouterr()
    assert "python_template" in captured.out
