"""Core text analysis functionality."""


def count_words(text: str) -> int:
    """Count words in text, handling edge cases."""
    if not text.strip():
        return 0
    return len(text.split())


def count_lines(text: str) -> int:
    """Count lines in text, handling different line endings."""
    if not text:
        return 0
    return text.count("\n") + (1 if not text.endswith("\n") else 0)


def count_characters(text: str) -> int:
    """Count total characters including whitespace."""
    return len(text)


def analyze_text(text: str) -> dict:
    """Comprehensive text analysis."""
    return {
        "words": count_words(text),
        "lines": count_lines(text),
        "characters": count_characters(text),
    }
