"""File reading utilities with error handling."""

from pathlib import Path


def read_file(filepath: str) -> str:
    """Read file content with proper encoding and error handling."""
    with Path(filepath).open(encoding="utf-8") as f:
        return f.read()
