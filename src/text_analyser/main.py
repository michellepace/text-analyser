"""CLI interface for text analysis."""

import sys
from pathlib import Path

from .analyser import analyze_text
from .file_utils import read_file

EXPECTED_ARGS = 2


def analyse_file() -> None:
    """Analyse a text file and display word, line, and character counts."""
    if len(sys.argv) != EXPECTED_ARGS:
        print("Usage: text-analyser <filename>", file=sys.stderr)
        sys.exit(1)

    filepath = Path(sys.argv[1])
    try:
        content = read_file(filepath)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Cannot decode '{filepath}' as UTF-8.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied reading '{filepath}'.", file=sys.stderr)
        sys.exit(1)

    results = analyze_text(content)

    print(f"File: {filepath}")
    print(f"Words: {results['words']}")
    print(f"Lines: {results['lines']}")
    print(f"Characters: {results['characters']}")


if __name__ == "__main__":
    analyse_file()
