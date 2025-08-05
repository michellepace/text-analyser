"""Tests for text analysis functions."""

from text_analyser.analyser import (
    analyze_text,
    count_characters,
    count_lines,
    count_words,
)


def test_count_words_normal():
    assert count_words("hello world test") == 3


def test_count_words_empty():
    assert count_words("") == 0
    assert count_words("   ") == 0


def test_count_lines_single():
    assert count_lines("hello") == 1


def test_count_lines_multiple():
    assert count_lines("hello\nworld\ntest") == 3


def test_count_lines_empty():
    assert count_lines("") == 0


def test_count_characters():
    assert count_characters("hello") == 5
    assert count_characters("hello\nworld") == 11


def test_analyze_text():
    result = analyze_text("hello world\ntest")
    assert result == {"words": 3, "lines": 2, "characters": 16}
