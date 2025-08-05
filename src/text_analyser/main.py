"""CLI interface for text analysis."""

import sys

from .analyser import analyze_text
from .file_utils import read_file

EXPECTED_ARGS = 2


def analyse_file() -> None:
    """Analyse a text file and display word, line, and character counts."""
    if len(sys.argv) != EXPECTED_ARGS:
        print("Usage: text-analyser <filename>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    content = read_file(filepath)
    results = analyze_text(content)

    print(f"File: {filepath}")
    print(f"Words: {results['words']}")
    print(f"Lines: {results['lines']}")
    print(f"Characters: {results['characters']}")


if __name__ == "__main__":
    analyse_file()
