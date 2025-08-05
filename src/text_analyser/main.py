"""CLI interface for text analysis."""

import argparse
import sys
from pathlib import Path

from .analyser import analyze_text
from .file_utils import read_file


def analyse_file() -> None:
    """Analyse a text file and display word, line, and character counts."""
    parser = argparse.ArgumentParser(
        description="Analyse text files for word, line, and character counts"
    )
    parser.add_argument("filename", type=Path, help="Path to the text file to analyse")

    args = parser.parse_args()
    filepath = args.filename
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
