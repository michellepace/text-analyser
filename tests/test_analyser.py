"""Tests for text analysis functions."""

from text_analyser.analyser import (
    analyze_text,
    count_characters,
    count_lines,
    count_words,
)


def test_count_words_normal() -> None:
    assert count_words("hello world test") == 3


def test_count_words_empty() -> None:
    assert count_words("") == 0
    assert count_words("   ") == 0


def test_count_lines_single() -> None:
    assert count_lines("hello") == 1


def test_count_lines_multiple() -> None:
    assert count_lines("hello\nworld\ntest") == 3


def test_count_lines_empty() -> None:
    assert count_lines("") == 0


def test_count_characters() -> None:
    assert count_characters("hello") == 5
    assert count_characters("hello\nworld") == 11


def test_analyze_text() -> None:
    result = analyze_text("hello world\ntest")
    assert result == {"words": 3, "lines": 2, "characters": 16}
