"""File reading utilities with error handling."""

import sys
from pathlib import Path


def read_file(filepath: str) -> str:
    """Read file content with proper encoding and error handling."""
    try:
        with Path(filepath).open(encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Cannot decode '{filepath}' as UTF-8.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied reading '{filepath}'.", file=sys.stderr)
        sys.exit(1)
