# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a UV-packaged Python CLI tool for text analysis. The project demonstrates modern Python development practices with UV as the package manager, strict linting with Ruff, and comprehensive testing with pytest.

## Key Architecture

**Entry Point Flow**: CLI command `text-analyser` → `analyse_file()` in `main.py` → `read_file()` from `file_utils.py` → `analyze_text()` from `analyser.py`

**Module Separation**:
- `main.py`: CLI interface and argument parsing
- `analyser.py`: Core text analysis functions (word/line/character counting)  
- `file_utils.py`: File I/O with error handling
- `__init__.py`: Package exports with `analyse_file` as the main entry point

The CLI is installable globally via `uv tool install` or as a project dependency via `uv add`, making it both a standalone tool and an importable library.

## Development Commands

**Setup Environment**:
```bash
uv sync                           # Install dependencies and create .venv
uv run pre-commit install        # Setup git hooks
```

**Testing**:
```bash
uv run pytest                    # Run all tests
uv run pytest tests/test_analyser.py              # Run specific test file
uv run pytest -k "test_count_words"               # Run tests matching pattern
uv run pre-commit run --all-files                 # Run all pre-commit hooks manually
```

**Code Quality**:
```bash
uv run ruff check                 # Lint code
uv run ruff check --fix           # Fix auto-fixable issues
uv run ruff format                # Format code
```

**CLI Testing**:
```bash
uv run text-analyser README.md    # Test CLI in project environment
text-analyser README.md           # Test globally installed version
```

## Important Configuration

**Ruff Settings**: Configured in `pyproject.toml` with "ALL" rules enabled and minimal exclusions. Uses Google docstring convention and strict complexity limits.

**Pre-commit Hooks**: Runs `uv-lock`, `ruff-check --fix`, `ruff-format`, and `pytest` on every commit. The `--exit-non-zero-on-fix` flag blocks commits when auto-fixes are made.

**UV Lockfile**: `uv.lock` ensures reproducible builds. The `uv-lock` pre-commit hook keeps it synchronized with `pyproject.toml`.

## Testing Strategy

All core functions have unit tests with edge case coverage:
- Empty string handling
- Different line ending types  
- File reading error scenarios (FileNotFoundError, UnicodeDecodeError, PermissionError)

Tests use direct function imports rather than CLI testing to maintain fast execution.