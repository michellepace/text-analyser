"""Tests for file operations."""

import os
import tempfile

import pytest

from text_analyser.file_utils import read_file


def test_read_file_success():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as f:
        f.write("test content")
        temp_path = f.name

    try:
        content = read_file(temp_path)
        assert content == "test content"
    finally:
        os.unlink(temp_path)


def test_read_file_not_found():
    with pytest.raises(SystemExit):
        read_file("nonexistent_file.txt")
