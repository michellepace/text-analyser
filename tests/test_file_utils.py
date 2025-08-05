"""Tests for file operations."""

from pathlib import Path

import pytest

from text_analyser.file_utils import read_file


def test_read_file_success(tmp_path: Path) -> None:
    test_file = tmp_path / "test.txt"
    test_file.write_text("test content", encoding="utf-8")
    assert read_file(test_file) == "test content"


def test_read_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        read_file(Path("nonexistent_file.txt"))


def test_read_file_unicode_error(tmp_path: Path) -> None:
    test_file = tmp_path / "invalid.txt"
    test_file.write_bytes(b"\xff\xfe\x00\x00")  # Invalid UTF-8 bytes
    with pytest.raises(UnicodeDecodeError):
        read_file(test_file)


def test_read_file_permission_error(tmp_path: Path) -> None:
    test_file = tmp_path / "restricted.txt"
    test_file.write_text("test content", encoding="utf-8")
    test_file.chmod(0o000)  # Remove read permissions
    with pytest.raises(PermissionError):
        read_file(test_file)
