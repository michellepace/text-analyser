# Implementation Plan for Critical Remediations

## Deliverable 1: Remove sys.exit() from Utilities + Custom Exceptions

**Implementation**:
- Create custom exceptions in `file_utils.py`: `TextAnalyserError`, `FileReadError`
- Replace all `sys.exit()` calls with appropriate exception raising
- Update `read_file()` to raise exceptions instead of terminating
- Modify `main.py` to catch and handle these exceptions gracefully
- Remove unused `sys` import from `file_utils.py`

**Final Steps**:
- Run `uv run pre-commit run --all-files` to ensure code quality

**Verification Tests**:
```bash
# Test that utilities no longer terminate the program
uv run python -c "from text_analyser.file_utils import read_file; print('Testing...'); read_file('nonexistent.txt')"
# Should show exception traceback, not silent exit
```
- [ ] Exception traceback shown (not silent exit)

```bash
# Test CLI still works with good files
uv run text-analyser README.md
# Should display file statistics
```
- [ ] File statistics displayed correctly

```bash
# Test CLI handles errors gracefully  
uv run text-analyser nonexistent.txt
# Should show user-friendly error message and exit code 1
```
- [ ] User-friendly error message shown
- [ ] Exit code is 1

## Deliverable 2: Use pathlib Consistently for File Operations

**Implementation**:
- Update `read_file(filepath: str)` to `read_file(filepath: Path | str)`
- Convert string inputs to Path objects in `main.py`
- Update all type hints and docstrings
- Ensure cross-platform path handling throughout

**Final Steps**:
- Run `uv run pre-commit run --all-files` to ensure code quality

**Verification Tests**:
```bash
# Test cross-platform path handling
uv run text-analyser "README.md"
uv run text-analyser "./README.md"  
uv run text-analyser "../text-analyser/README.md"
# All should work correctly
```
- [ ] `"README.md"` works correctly
- [ ] `"./README.md"` works correctly  
- [ ] `"../text-analyser/README.md"` works correctly

```bash
# Test type checker is happy
uv run python -c "from text_analyser.file_utils import read_file; from pathlib import Path; read_file(Path('README.md'))"
# Should execute without type errors
```
- [ ] No type errors when using Path objects

## Deliverable 3: Implement argparse for CLI

**Implementation**:
- Replace `sys.argv` parsing with `argparse.ArgumentParser`
- Add `--help` functionality with proper description
- Implement better error messages and argument validation
- Handle file existence and readability checks in CLI layer
- Remove `EXPECTED_ARGS` constant

**Final Steps**:
- Run `uv run pre-commit run --all-files` to ensure code quality

**Verification Tests**:
```bash
# Test help functionality
uv run text-analyser --help
# Should show proper usage, description, and options
```
- [ ] Help message shows proper usage
- [ ] Help message shows description
- [ ] Help message shows available options

```bash
# Test error handling
uv run text-analyser
# Should show usage message and exit with code 2 (argparse standard)
```
- [ ] Usage message shown when no arguments
- [ ] Exit code is 2

```bash
uv run text-analyser file1.txt file2.txt  
# Should show error about too many arguments
```
- [ ] Error message about too many arguments

```bash
# Test normal functionality still works
uv run text-analyser README.md
# Should display file statistics correctly
```
- [ ] File statistics displayed correctly

## Deliverable 4: Add Integration Tests

**Implementation**:
- Create `tests/test_integration.py` with end-to-end CLI tests
- Test CLI with valid files using temporary test files
- Test CLI error scenarios (missing files, permission errors, invalid arguments)
- Test CLI help functionality using subprocess
- Ensure tests cover complete workflow from CLI input to output

**Final Steps**:
- Run `uv run pre-commit run --all-files` to ensure code quality

**Verification Tests**:
```bash
# Run new integration tests
uv run pytest tests/test_integration.py -v
# Should show all integration tests passing
```
- [ ] All integration tests pass

```bash
# Run complete test suite
uv run pytest -v
# Should show all tests (unit + integration) passing
```
- [ ] All unit tests still pass
- [ ] All integration tests pass
- [ ] No test failures or errors

```bash
# Test CLI still works after all changes
uv run text-analyser README.md
# Should display correct file statistics
```
- [ ] File statistics displayed correctly

```bash
# Verify global installation still works (if installed)
text-analyser README.md
# Should work identically to uv run version
```
- [ ] Global installation works (if applicable)
- [ ] Output identical to `uv run` version

## Expected Verification Results
After each deliverable, you should see:
- [ ] ✅ All pre-commit hooks passing (ruff, pytest, uv-lock)
- [ ] ✅ CLI functionality preserved or improved
- [ ] ✅ Better error messages and user experience
- [ ] ✅ All existing and new tests passing
- [ ] ✅ Type checking clean with proper pathlib usage

## Summary Checklist
- [ ] Deliverable 1 completed and verified
- [ ] Deliverable 2 completed and verified
- [ ] Deliverable 3 completed and verified
- [ ] Deliverable 4 completed and verified
- [ ] All verification tests passing
- [ ] Pre-commit hooks passing for all deliverables