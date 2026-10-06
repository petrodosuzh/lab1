---
name: create-build
description: "Configure the Python venv and run/test workflow, add pytest coverage, and validate locally using the build-and-test skill."
agent: "Build Engineer"
---

# create-build

## Purpose

Configure the Python virtual environment and repeatable build/test workflow, create pytest tests, and perform local validation by following the [build-and-test skill](../skills/build-and-test/SKILL.md).

## Prerequisites

- Run from the repository root after `create-project` has produced or verified the app scaffold.
- Python 3 is available. Read and follow the linked skill before editing.
- Preserve user files and do not install dependencies globally.

## Actions

1. Inspect existing dependencies, pytest settings, scripts, README, `.gitignore`, and `.venv` before making changes.
2. Follow the linked `build-and-test` skill to configure cross-platform venv usage, dependencies, tests, and portable build/test scripts.
3. If `.venv` does not exist, create it with `python -m venv .venv`; reuse an existing environment and never delete/recreate it to force success.
4. Install declared test dependencies into `.venv` using its Python interpreter and `-m pip`; update setup/run instructions to match actual files and commands.
5. Run the app, repository build script, and pytest through the repository test script. Report each command and result.

## Expected Files

- `requirements-dev.txt` or the existing test-dependency declaration.
- `pyproject.toml` or existing pytest configuration.
- `tests/test_main.py` or equivalent focused test(s).
- `scripts/build.py` and `scripts/test.py`, unless equivalent scripts already exist.
- Updated `README.md` and `.gitignore` if needed.
- Local `.venv/` environment, ignored by Git; do not include it in source control.

## Validation

- `.venv` is usable and ignored by Git; dependencies install into it.
- The app launch command passes.
- The build script exits successfully.
- The test script invokes pytest and propagates its exit code; pytest passes.
- README commands and venv activation instructions match the implementation on POSIX and Windows shells.
- Tests and build do not add tracked caches or generated files.

## Error Handling

- If Python/venv creation or dependency installation fails, report the exact command and error; do not install globally or delete an existing environment.
- If tests or build fail, inspect the failing output, make the smallest relevant correction, and rerun the failed check.
- If an existing file conflicts with the skill's default layout, preserve it and adapt or report the blocker; do not create duplicate configuration.
- Never claim a check passed unless it ran successfully.

## Idempotency

- Reuse an existing healthy `.venv`, dependencies, configuration, scripts, and tests.
- Do not recreate environments, duplicate requirements/configuration, or append repeated README/ignore entries.
- Keep `.venv/` and generated files ignored; do not stage or commit them.