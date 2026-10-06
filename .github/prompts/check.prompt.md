---
name: check
description: "Read-only validation of the lab1 repository structure, Python project, tests, scripts, and GitHub Actions YAML."
agent: "Build Engineer"
---

# check

## Purpose

Validate the complete repository without changing any project file, Git state, environment, or configuration.

## Prerequisites

- Run from the repository root with Python available.
- Do not install dependencies, create a venv, edit files, or run commands directly against the workspace if they can write generated output.
- Use a disposable temporary copy outside the repository for execution of tests/build scripts; clean up only that command-owned temporary directory automatically.

## Actions

1. Capture `git status --short --branch` and inspect the repository tree without edits.
2. Verify required files exist: `src/hello_world/main.py`, `run.py`, `README.md`, `.gitignore`, dependency/pytest configuration, tests, build/test scripts, and a workflow under `.github/workflows/`.
3. Check Python source and scripts for syntax using read-only parsing (for example, Python `ast.parse`). Inspect the README commands, dependency declaration, pytest configuration, `.gitignore`, and scripts for consistency.
4. Copy the working tree to an OS temporary directory outside the repository, excluding `.git`, virtual environments, and existing caches. Run the documented app launch, build script, and pytest/test script in that copy using the project's declared environment/dependencies only if already available. Do not install missing dependencies. Remove the temporary copy through its temporary-directory context manager.
5. Validate GitHub Actions YAML using `actionlint` or an already-installed YAML parser. Confirm its matrix includes Ubuntu, Windows, and macOS, and its jobs use the expected dependency/build/test commands.
6. Check that `.venv/`, caches, and generated artifacts are ignored. Capture Git status again and confirm the repository state is unchanged.
7. Report each check as pass, fail, or not run, with relevant command output and any platform/parser limitation. Never modify files to fix failures during this command.

## Expected Files

- No files may be created, edited, deleted, staged, or committed by this command.
- Expected project files are inspected only: application, launcher, README, `.gitignore`, test/dependency configuration, tests, scripts, and GitHub Actions workflow.

## Validation

- Repository structure and required file presence are checked.
- Python source and scripts parse successfully.
- App launch, build script, and tests are exercised in the disposable copy when prerequisites are already available.
- GitHub Actions YAML is parsed when a validator is available; otherwise report static checks and mark YAML parsing not run.
- `.gitignore` covers local environments and generated files.
- Git status before and after is identical; the working repository remains untouched.

## Error Handling

- If a prerequisite is missing, mark the affected check not run and explain why; do not install dependencies or create project files.
- If a check fails in the temporary copy, report the exact command and failure without repairing the project.
- If the temporary copy cannot be created or cleaned automatically, stop execution and report the issue; do not fall back to potentially modifying commands in the workspace.
- A dirty initial Git status is not itself a failure; preserve it and compare with the final status.

## Idempotency

- This command is read-only and can be repeated without changing repository contents or Git state.
- Keep all execution output and generated files confined to the temporary copy; do not alter user files or configuration.