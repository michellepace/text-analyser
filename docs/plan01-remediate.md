# Implementation Plan for Critical Remediations

## Deliverable 1: Remove sys.exit() from Utilities (Simple Approach)

**Implementation**:
- Remove `sys.exit()` calls from `read_file()` - let built-in exceptions bubble up naturally
- Handle `FileNotFoundError`, `UnicodeDecodeError`, and `PermissionError` in `main.py`
- Maintain user-friendly error messages and proper exit codes in CLI layer
- Add comprehensive unit tests for all exception scenarios

**Final Steps**:
- Run `uv run pre-commit run --all-files` to ensure code quality

**Verification Tests**:
```bash
# Test that utilities no longer terminate the program
uv run python -c "from text_analyser.file_utils import read_file; print('Testing...'); read_file('nonexistent.txt')"
# Should show exception traceback, not silent exit
```
- [x] Exception traceback shown (not silent exit)

```bash
# Test CLI still works with good files
uv run text-analyser README.md
# Should display file statistics
```
- [x] File statistics displayed correctly

```bash
# Test CLI handles errors gracefully  
uv run text-analyser nonexistent.txt
# Should show user-friendly error message and exit code 1
```
- [x] User-friendly error message shown
- [x] Exit code is 1

**Additional Tests Added**:
```bash
# Test Unicode decode error handling
echo -e '\xff\xfe\x00\x00' > invalid_utf8.bin && uv run text-analyser invalid_utf8.bin
# Should show UTF-8 decode error message
```
- [x] Unicode decode error handled properly

```bash
# Test permission error handling  
echo "test" > no_read.txt && chmod 000 no_read.txt && uv run text-analyser no_read.txt
# Should show permission denied error message
```
- [x] Permission error handled properly

## Deliverable 2: Use pathlib Consistently for File Operations

**Implementation**:
- Update `read_file(filepath: str)` to `read_file(filepath: Path)`
- Convert `sys.argv[1]` to `Path` object early in `main.py`
- Remove internal `Path()` conversion from `read_file()` - now handled at entry point
- Update all tests to pass `Path` objects
- Add `from pathlib import Path` import to `main.py`

**Final Steps**:
- Run `uv run pre-commit run --all-files` to ensure code quality

**Verification Tests**:
```bash
# Test cross-platform path handling
uv run text-analyser "README.md"
uv run text-analyser "./README.md"  
uv run text-analyser "src/../README.md"
# All should work correctly
```
- [x] `"README.md"` works correctly
- [x] `"./README.md"` works correctly  
- [x] `"src/../README.md"` works correctly (complex relative paths)

```bash
# Test type checker is happy
uv run python -c "from text_analyser.file_utils import read_file; from pathlib import Path; read_file(Path('README.md'))"
# Should execute without type errors
```
- [x] No type errors when using Path objects

## Deliverable 3: Implement argparse for CLI

**Implementation**:
- Replace `sys.argv` parsing with `argparse.ArgumentParser`
- Add CLI description: "Analyse text files for word, line, and character counts"
- Add argument help text for filename parameter
- Use `type=Path` in argparse for automatic Path conversion
- Remove `EXPECTED_ARGS` constant

**Final Steps**:
- Run `uv run pre-commit run --all-files` to ensure code quality

**Verification Tests**:
```bash
# Test help functionality
uv run text-analyser --help
# Should show proper usage, description, and options
```
- [x] Help message shows proper usage
- [x] Help message shows description
- [x] Help message shows available options

```bash
# Test error handling
uv run text-analyser
# Should show usage message and exit with code 2 (argparse standard)
```
- [x] Usage message shown when no arguments
- [x] Exit code is 2

```bash
uv run text-analyser file1.txt file2.txt  
# Should show error about too many arguments
```
- [x] Error message about too many arguments

```bash
# Test normal functionality still works
uv run text-analyser README.md
# Should display file statistics correctly
```
- [x] File statistics displayed correctly

**Additional Verification**:
```bash
# Test file error handling still works
uv run text-analyser nonexistent.txt
# Should show file error message and exit code 1
```
- [x] File error handling preserved (exit code 1 for runtime errors)

## Deliverable 4: Add Integration Tests

**Implementation**:
- Create `tests/test_integration.py` with 8 end-to-end CLI tests using subprocess
- Safe subprocess helper using `shutil.which()` for full executable paths
- Test CLI with valid files using temporary test files
- Test CLI error scenarios (missing files, permission errors, invalid arguments)
- Test CLI help functionality and argument validation
- Ensure tests cover complete workflow from CLI input to output with real exit codes

**Final Steps**:
- Run `uv run pre-commit run --all-files` to ensure code quality

**Verification Tests**:
```bash
# Run new integration tests
uv run pytest tests/test_integration.py -v
# Should show all integration tests passing
```
- [x] All integration tests pass

```bash
# Run complete test suite
uv run pytest -v
# Should show all tests (unit + integration) passing
```
- [x] All unit tests still pass (13 unit + 8 integration = 21 total)
- [x] All integration tests pass
- [x] No test failures or errors

```bash
# Test CLI still works after all changes
uv run text-analyser README.md
# Should display correct file statistics
```
- [x] File statistics displayed correctly

```bash
# Verify global installation still works (if installed)
text-analyser README.md
# Should work identically to uv run version
```
- [x] Global installation works (if applicable)
- [x] Output identical to `uv run` version

## Expected Verification Results
After each deliverable, you should see:
- [ ] ✅ All pre-commit hooks passing (ruff, pytest, uv-lock)
- [ ] ✅ CLI functionality preserved or improved
- [ ] ✅ Better error messages and user experience
- [ ] ✅ All existing and new tests passing
- [ ] ✅ Type checking clean with proper pathlib usage

## Summary Checklist
- [x] Deliverable 1 completed and verified
- [x] Deliverable 2 completed and verified
- [x] Deliverable 3 completed and verified
- [x] Deliverable 4 completed and verified
- [x] All verification tests passing for all deliverables
- [x] Pre-commit hooks passing for all deliverables

## Final Results
- ✅ **21 tests total** (13 unit tests + 8 integration tests)
- ✅ **Complete CLI workflow coverage** with real subprocess execution
- ✅ **All error scenarios tested** with proper exit code validation
- ✅ **Professional CLI behavior** with argparse, help functionality, and pathlib usage
- ✅ **Clean, maintainable codebase** with modern Python practices