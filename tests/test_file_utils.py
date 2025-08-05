"""Tests for file operations."""

import tempfile
from pathlib import Path

import pytest

from text_analyser.file_utils import read_file


def test_read_file_success() -> None:
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as f:
        f.write("test content")
        temp_path = f.name

    try:
        content = read_file(Path(temp_path))
        assert content == "test content"
    finally:
        Path(temp_path).unlink()


def test_read_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        read_file(Path("nonexistent_file.txt"))


def test_read_file_unicode_error() -> None:
    with tempfile.NamedTemporaryFile(mode="wb", delete=False) as f:
        f.write(b"\xff\xfe\x00\x00")  # Invalid UTF-8 bytes
        temp_path = f.name

    try:
        with pytest.raises(UnicodeDecodeError):
            read_file(Path(temp_path))
    finally:
        Path(temp_path).unlink()


def test_read_file_permission_error() -> None:
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as f:
        f.write("test content")
        temp_path = f.name

    try:
        # Remove read permissions
        Path(temp_path).chmod(0o000)
        with pytest.raises(PermissionError):
            read_file(Path(temp_path))
    finally:
        # Restore permissions for cleanup
        Path(temp_path).chmod(0o644)
        Path(temp_path).unlink()
