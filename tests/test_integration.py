"""Integration tests for CLI interface using subprocess."""

import shutil
import subprocess
from pathlib import Path


def run_cli_command(*args: str) -> subprocess.CompletedProcess[str]:
    """Run text-analyser CLI command safely with full paths."""
    uv_path = shutil.which("uv")
    if not uv_path:
        msg = "uv executable not found in PATH"
        raise RuntimeError(msg)

    cmd = [uv_path, "run", "text-analyser", *args]
    return subprocess.run(  # noqa: S603
        cmd,
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_help() -> None:
    """Test --help functionality works correctly."""
    result = run_cli_command("--help")

    assert result.returncode == 0
    assert "Analyse text files for word, line, and character counts" in result.stdout
    assert "filename" in result.stdout
    assert "Path to the text file to analyse" in result.stdout


def test_cli_success_with_valid_file(tmp_path: Path) -> None:
    """Test CLI works correctly with a valid file."""
    test_file = tmp_path / "sample.txt"
    test_file.write_text("hello world\ntest file", encoding="utf-8")

    result = run_cli_command(str(test_file))

    assert result.returncode == 0
    assert f"File: {test_file}" in result.stdout
    assert "Words: 4" in result.stdout
    assert "Lines: 2" in result.stdout
    assert "Characters: 21" in result.stdout


def test_cli_file_not_found_exit_code() -> None:
    """Test CLI returns exit code 1 for missing files."""
    result = run_cli_command("nonexistent_file_xyz.txt")

    assert result.returncode == 1
    assert "Error: File 'nonexistent_file_xyz.txt' not found." in result.stderr


def test_cli_no_arguments_exit_code() -> None:
    """Test CLI returns exit code 2 for missing arguments."""
    result = run_cli_command()

    assert result.returncode == 2
    assert "error: the following arguments are required: filename" in result.stderr


def test_cli_too_many_arguments_exit_code() -> None:
    """Test CLI returns exit code 2 for too many arguments."""
    result = run_cli_command("file1.txt", "file2.txt")

    assert result.returncode == 2
    assert "error: unrecognized arguments: file2.txt" in result.stderr


def test_cli_unicode_decode_error(tmp_path: Path) -> None:
    """Test CLI handles Unicode decode errors correctly."""
    test_file = tmp_path / "invalid.txt"
    test_file.write_bytes(b"\xff\xfe\x00\x00")  # Invalid UTF-8 bytes

    result = run_cli_command(str(test_file))

    assert result.returncode == 1
    assert f"Error: Cannot decode '{test_file}' as UTF-8." in result.stderr


def test_cli_permission_error(tmp_path: Path) -> None:
    """Test CLI handles permission errors correctly."""
    test_file = tmp_path / "restricted.txt"
    test_file.write_text("test content", encoding="utf-8")
    test_file.chmod(0o000)  # Remove read permissions

    result = run_cli_command(str(test_file))

    assert result.returncode == 1
    assert f"Error: Permission denied reading '{test_file}'." in result.stderr


def test_cli_with_readme() -> None:
    """Test CLI works with the actual README.md file."""
    result = run_cli_command("README.md")

    assert result.returncode == 0
    assert "File: README.md" in result.stdout
    assert "Words:" in result.stdout
    assert "Lines:" in result.stdout
    assert "Characters:" in result.stdout
    # README should have substantial content
    assert "Words: 0" not in result.stdout
