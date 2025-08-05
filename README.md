# README: Text Analyser With UV

**Shows [UV](https://docs.astral.sh/uv/)'s Python tooling through a simple text analysis tool.** UV is a modern package manager that handles dependencies, environments, and project setup in one tool. It replaces the traditional requirements.txt and pip workflow with integrated tooling. This project features a Python packaged application, pytest TDD, ruff linting, and [pre-commit hooks](.pre-commit-config.yaml).

```bash
# Run from anywhere (packaged CLI available in PATH)
mp@laptopmp ~/ 
$ text-analyser anywhere/HORSE.md 

File: anywhere/HORSE.md
Words: 798
Lines: 178
Characters: 6128
```

*A simple CLI tool to analyse text files.*

The project includes IDE setup with [extensions](.vscode/extensions.json), [settings](.vscode/settings.json), ruff/pylance [config](pyproject.toml), and [gitattributes](.gitattributes) to support development on any platform.

![pip to uv migration diagram](images/pip-to-uv.jpg)

## Prerequisites

UV must be installed on your system. See the [installation guide](https://docs.astral.sh/uv/getting-started/installation/) for setup instructions.

## Installation

💻 **Install as CLI Tool**

```bash
uv tool install git+https://github.com/michellepace/text-analyser

uv tool list # verify tool is globally installed
```

*Installs text-analyser command globally for use anywhere in your terminal. Use `uv tool upgrade text-analyser` to update to latest version.*

📦 **Install as Dependency**

```bash
uv add git+https://github.com/michellepace/text-analyser
```

*Adds text-analyser as a dependency in your current project.*

🛠️ **Clone for Development**

```bash
git clone https://github.com/michellepace/text-analyser
cd text-analyser
uv sync
```

*Sets up full development environment for contributing or modifying the project.*

**When to choose:**
- **CLI Tool**: Use `text-analyser` command system-wide from any directory
- **Dependency**: Include text analysis functionality in your project's code
- **Development**: Modify the source code, add features, or contribute changes

## Usage

Run as a command line tool:

```bash
# Direct execution - packaged CLI available in PATH (global)
text-analyser filename.txt
```

Run as command in project environment

```
# UV runs the CLI command in project environment
uv run text-analyser filename.txt
```

**a) Install IDE Extensions**

*Configure your IDE using the project's extension recommendations in [extensions.json](extensions.json) and workspace settings in [settings.json](settings.json). For Cursor IDE, use the provided configuration as-is. For VSCode, replace `anysphere.cursorpyright` with [Microsoft Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).*

**b) Create Virtual Environment**

```bash
# Sync creates .venv/ with Python interpreter and all dependencies
uv sync
```

*UV automatically installs Python 3.13, your project package, and all dev dependencies (including pre-commit, pytest, ruff) into `.venv/`*

**c) Activate Virtual Environment in IDE**

```bash
# Should show: .../text-analyser/.venv/bin/python
which python

# Should show: Python 3.13.x
python --version
```

*Restart your IDE and open a fresh terminal to ensure the virtual environment is active. Verify setup with the commands above.*

**d) Install Pre-commit Git Hooks**

```bash
# Install git hooks
uv run pre-commit install

# Test hooks work
uv run pre-commit run --all-files
```

*Pre-commit is installed as a dev dependency during `uv sync`. The `pre-commit install` command sets up git hooks to run automatically before commits.*

**e) Verify Complete Workflow**

```bash
# Test development workflow
uv sync                           # Sync dependencies
uv run pytest                    # Run tests
uv run ruff format               # Format code
uv run ruff check --fix          # Lint and fix issues

# Verify pre-commit hooks
uv run pre-commit run --all-files       # Test all hooks pass

# Test CLI functionality
uv run text-analyser README.md   # Should display file statistics
```

*These commands prove steps a-d are working correctly. UV automatically handles locking and syncing during `uv run` commands, but running `uv sync` manually ensures your editor has the correct dependency versions, especially after pulling changes.*

## Why This Project Used `--package`

Text-analyser is a [UV Packaged Application](https://docs.astral.sh/uv/concepts/projects/init/#packaged-applications). It was created with `uv init --package text-analyser` instead of basic `uv init` to unlock these capabilities:

**The Key Differences**

| **`uv init`** (Basic Script) | **`uv init --package`** (This Project) |
|-------------------------------|------------------------------------------|
| ❌ No build system configured | ✅ Complete build system with `uv_build` backend |
| ❌ Just files in a directory | ✅ Installs as importable package in `.venv` |
| ❌ No terminal commands possible | ✅ Creates `text-analyser` command system-wide |
| ❌ Cannot share or distribute | ✅ Installable from GitHub/PyPI |
| ❌ Basic flat file structure | ✅ Clean `src/` layout, making `tests/` ideal |

🎯 **Choose `--package` when you want to:**

- ✅ **Create terminal commands** that work from anywhere (`text-analyser file.txt`)
- ✅ **Share your project** through GitHub installation or PyPI publishing  
- ✅ **Build professionally** with `src/` and `tests/` directory structure
- ✅ **Enable library imports** so others can use your functions: `from text_analyser import analyser`
- ✅ **Install seamlessly** with `uv add git+https://github.com/user/repo`

**Skip `--package` for:**

- ❌ Quick one-time scripts
- ❌ Personal tools you won't share
- ❌ Simple prototypes without professional requirements

**Without `--package`, this would remain a collection of Python files that can't be installed, shared, or used as a real tool.** 🦚
