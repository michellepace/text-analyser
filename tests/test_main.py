"""Tests for CLI interface."""

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from text_analyser.main import analyse_file


def test_main_with_file() -> None:
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as f:
        f.write("hello world\ntest")
        temp_path = f.name

    try:
        with (
            patch("sys.argv", ["text-analyser", temp_path]),
            patch("builtins.print") as mock_print,
        ):
            analyse_file()
            # Note: We only test key outputs; analyse_file() prints 4 lines total
            mock_print.assert_any_call(f"File: {temp_path}")
            mock_print.assert_any_call("Words: 3")
    finally:
        Path(temp_path).unlink()


def test_main_no_args() -> None:
    with patch("sys.argv", ["text-analyser"]), pytest.raises(SystemExit):
        analyse_file()
