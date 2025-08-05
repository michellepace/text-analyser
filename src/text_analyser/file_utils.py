"""File reading utilities with error handling."""

import logging
import sys

logger = logging.getLogger(__name__)


def read_file(filepath: str) -> str:
    """Read file content with proper encoding and error handling."""
    try:
        with open(filepath, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        logger.exception("File '%s' not found.", filepath)
        sys.exit(1)
    except UnicodeDecodeError:
        logger.exception("Cannot decode '%s' as UTF-8.", filepath)
        sys.exit(1)
    except PermissionError:
        logger.exception("Permission denied reading '%s'.", filepath)
        sys.exit(1)
