---
name: project-scaffold
description: "Create or validate the minimal cross-platform lab1 Python Hello World scaffold: source directory, application entry point, launch script, README, and initial Git ignore rules. Use when bootstrapping the application structure."
---

# Project Scaffold

## Purpose

Create the minimal Python Hello World application structure and verify that the launch script works. This skill defines the initial app scaffold; it does not configure pytest or GitHub Actions.

## Prerequisites

- Work from the repository root on the supplied working branch.
- Python 3 must be available for launch validation.
- The Build Engineer agent's repository safety rules apply: preserve user changes, do not delete files, do not commit, and do not add generated files or secrets.

## Inputs

- The current repository tree and Git status.
- Existing project conventions and any user-provided Python version or greeting requirements.
- The Python interpreter available for local validation.

## Actions

1. Inspect the repository tree and Git status. Read existing instructions and any files that overlap this scaffold before editing.
2. Reuse correct existing files. If an expected path already contains different user work, do not overwrite it; adapt to the established layout or report the conflict.
3. Create only missing scaffold files, using this default layout when the repository has no established alternative:
   - `src/hello_world/main.py`: define `main()` and print `Hello, world!` when run as a module/script.
   - `run.py`: portable launcher that locates `src`, calls the application's `main()`, and returns a useful nonzero exit status on failure.
   - `README.md`: concise project purpose and launch instructions using `python run.py`.
   - `.gitignore`: initial Python ignores, including `.venv/`, `venv/`, `__pycache__/`, `*.py[cod]`, `.pytest_cache/`, and common generated build/test output.
4. Ensure the README's run command matches the launcher and works from the repository root. Do not claim venv or pytest setup exists unless those files/instructions are present.
5. Launch the app with the available Python interpreter from the repository root. Confirm the expected greeting appears and the process exits successfully.
6. Report created or updated paths and the launch result. State any check that could not be run and why.

## Outputs

- A minimal, runnable Hello World scaffold, or a concise report of conflicts that prevent safe creation.
- A list of changed files and the launch validation result.

## Expected Files

- `src/hello_world/main.py`
- `run.py`
- `README.md`
- `.gitignore`

These are expected project outputs when missing, not permission to overwrite correct or user-owned files.

## Validation Checks

- `python run.py` runs from the repository root without requiring a globally installed package.
- Standard output contains exactly the documented greeting (apart from a trailing newline), and the process exits with status 0.
- The source directory, entry point, launcher, README, and `.gitignore` exist.
- `.gitignore` contains rules for `.venv` and generated Python/test/build files without removing existing rules.
- `git status --short` shows no virtual environment, cache, or generated output as project content.

## Expected Result

The repository has one minimal Python application entry point, a working root-level launcher, concise launch documentation, and ignore rules for local/generated files. Re-running the skill makes no duplicate files or duplicate ignore entries.

## Typical Failure Scenario

An existing `run.py`, README, or source tree belongs to the user or follows a different layout, so blindly creating the default paths would overwrite or duplicate their project.

## Error Handling

- Inspect conflicting files and adapt to the existing correct layout; do not delete or replace them to force the default structure.
- If Python is unavailable, finish only safe file work and report that launch validation was not performed; do not claim success.
- If launch fails, report the exact command and relevant error, fix only scaffold-caused defects, and rerun the same launch check.
- Do not stage or commit files, and do not leave a virtual environment or generated artifacts behind.

## Idempotency Requirements

- Check each target before creating or changing it.
- Preserve correct content and unrelated user changes; make the smallest necessary edit.
- Add only missing `.gitignore` patterns, avoiding repeated entries.
- Do not create a second application entry point, launcher, README, or source package when an equivalent correct one exists.