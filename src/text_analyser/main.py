"""CLI interface for text analysis."""

import logging
import sys

from .analyser import analyze_text
from .file_utils import read_file

# Configure logging for CLI output
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

EXPECTED_ARGS = 2


def analyse_file() -> None:
    """Analyse a text file and display word, line, and character counts."""
    if len(sys.argv) != EXPECTED_ARGS:
        logger.error("Usage: text-analyser <filename>")
        sys.exit(1)

    filepath = sys.argv[1]
    content = read_file(filepath)
    results = analyze_text(content)

    logger.info("File: %s", filepath)
    logger.info("Words: %s", results["words"])
    logger.info("Lines: %s", results["lines"])
    logger.info("Characters: %s", results["characters"])


if __name__ == "__main__":
    analyse_file()
