---
name: build-and-test
description: "Configure Python virtual-environment usage, pytest dependencies and tests, portable repository build/test scripts, and local validation for lab1. Use when setting up or checking the Python development and test workflow."
---

# Build and Test

## Purpose

Provide a repeatable, cross-platform local workflow to create/use a Python virtual environment, install test dependencies, validate the application, and run pytest.

## Prerequisites

- Run from the repository root with Python 3 available.
- Inspect the existing scaffold and follow its package layout; the default scaffold is `src/hello_world/main.py` with `run.py`.
- The project must use a local virtual environment; do not install project/test dependencies globally.
- Preserve the Build Engineer agent's safety rules and all unrelated work.

## Inputs

- Existing application, README, `.gitignore`, dependency declarations, test files, and build/test scripts.
- Available Python version and platform.
- Any existing repository test conventions or user-specified supported Python version.

## Actions

1. Inspect the repository and identify existing dependency, pytest, test, and build configuration. Reuse correct configuration instead of adding parallel files.
2. Document environment creation and activation in `README.md` using the platform-appropriate commands:
   - Create: `python -m venv .venv`.
   - POSIX activation: `source .venv/bin/activate`.
   - Windows PowerShell activation: `.venv\Scripts\Activate.ps1`.
   - Windows Command Prompt activation: `.venv\Scripts\activate.bat`.
3. Declare pytest as a development/test dependency in the existing dependency file, or create `requirements-dev.txt` containing a supported pytest requirement if no dependency convention exists. Keep runtime dependencies empty for this Hello World app.
4. Add pytest configuration to the existing project configuration or create `pyproject.toml` with `testpaths = ["tests"]` and `pythonpath = ["src"]`, unless an equivalent configuration already exists.
5. Add focused tests under `tests/` for the application behavior. Capture output or call `main()` directly; assert the documented greeting without coupling tests to implementation details.
6. Provide portable repository scripts under `scripts/` when they do not already exist:
   - `scripts/build.py` runs a deterministic syntax/build check for the source (for example, `python -m compileall -q src`) and returns a failing exit status if it fails.
   - `scripts/test.py` runs `python -m pytest` using the same interpreter that invoked the script, propagating pytest's exit status. Resolve the repository root from the script path so invocation works from any current directory.
7. Document dependency installation with the active venv interpreter: `python -m pip install -r requirements-dev.txt`. Document local validation using `python run.py`, `python scripts/build.py`, and `python scripts/test.py`.
8. Run the documented commands in order using the venv where available: install dependencies, launch app, build check, and pytest. Report commands and outcomes accurately.

## Outputs

- A documented venv/dependency workflow, focused pytest coverage, and portable build/test entry points, reusing existing correct project configuration.
- A concise report of changed paths and local validation results.

## Expected Files

- `requirements-dev.txt` or the repository's existing test-dependency declaration.
- `tests/test_main.py` or an equivalent focused test in the existing test layout.
- `pyproject.toml` or the existing pytest configuration.
- `scripts/build.py` and `scripts/test.py`, unless equivalent repository scripts already exist.
- Updated `README.md` and `.gitignore` when needed.

Do not create a second dependency declaration, pytest configuration, or script for behavior already handled by an existing correct file.

## Validation Checks

- Dependency installation uses the venv's `python -m pip` and completes successfully.
- `python run.py` prints the documented greeting.
- `python scripts/build.py` exits successfully and does not leave tracked generated output.
- `python scripts/test.py` invokes pytest and propagates its success/failure status.
- `python -m pytest` passes from the repository root; tests are discovered from the configured test directory.
- `.venv/`, caches, and build/test artifacts remain ignored by Git.
- README commands match actual file names and work on the documented shells/platforms.

## Expected Result

A developer can create and activate `.venv`, install the declared test dependency, launch the app, run the repository build check, and run pytest with documented commands. Failures produce nonzero statuses that local users and CI can detect.

## Typical Failure Scenario

Tests pass only when run from a particular working directory or with a globally installed pytest, while the documented venv workflow or CI's clean environment fails to import the `src` package.

## Error Handling

- If dependency installation fails, report the interpreter, command, and package-manager error; do not silently switch to a global install or alter unrelated dependency files.
- If test discovery/import fails, inspect the project layout and pytest configuration, then make the smallest compatible correction and rerun the failing command.
- Preserve failing test output and return codes; do not weaken or remove meaningful tests merely to obtain a pass.
- If Python/pytest is unavailable, report the blocked validation and exact prerequisite; do not report tests as passing.
- Do not leave `.venv`, caches, or build/test artifacts tracked. Keep the environment local and ignored.

## Idempotency Requirements

- Inspect before creating files; extend existing correct dependency, pytest, script, README, and ignore configuration rather than duplicating it.
- Test additions must be stable across repeated runs and must not depend on network access or external services.
- Build/test scripts must not destructively clean the repository and must return consistent exit statuses.
- Do not rewrite lockfiles or dependency declarations without a demonstrated need; never add duplicate requirements or ignore entries.