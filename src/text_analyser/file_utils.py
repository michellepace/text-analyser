"""File reading utilities with error handling."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def read_file(filepath: Path) -> str:
    """Read file content with proper encoding and error handling."""
    with filepath.open(encoding="utf-8") as f:
        return f.read()
