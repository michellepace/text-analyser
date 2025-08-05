"""Tests for CLI interface."""

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from text_analyser.main import analyse_file


def test_main_with_file():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as f:
        f.write("hello world\ntest")
        temp_path = f.name

    try:
        with (
            patch("sys.argv", ["text-analyser", temp_path]),
            patch("text_analyser.main.logger") as mock_logger,
        ):
            analyse_file()
            # Verify logger.info calls for output
            mock_logger.info.assert_any_call("File: %s", temp_path)
            mock_logger.info.assert_any_call("Words: %s", 3)
    finally:
        Path(temp_path).unlink()


def test_main_no_args():
    with (
        patch("sys.argv", ["text-analyser"]),
        pytest.raises(SystemExit),
    ):
        analyse_file()
