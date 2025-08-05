"""Tests for CLI interface."""

from pathlib import Path
from unittest.mock import patch

import pytest

from text_analyser.main import analyse_file


def test_main_with_file(tmp_path: Path) -> None:
    test_file = tmp_path / "sample.txt"
    test_file.write_text("hello world\ntest", encoding="utf-8")

    with (
        patch("sys.argv", ["text-analyser", str(test_file)]),
        patch("builtins.print") as mock_print,
    ):
        analyse_file()
        # Note: We only test key outputs; analyse_file() prints 4 lines total
        mock_print.assert_any_call(f"File: {test_file}")
        mock_print.assert_any_call("Words: 3")


def test_main_no_args() -> None:
    with patch("sys.argv", ["text-analyser"]), pytest.raises(SystemExit):
        analyse_file()
