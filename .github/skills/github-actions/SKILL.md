---
name: github-actions
description: "Create or validate GitHub Actions CI for the lab1 Python project on Ubuntu, Windows, and macOS using a matrix, declared dependencies, and repository build/test scripts. Use when setting up or maintaining cross-platform CI."
---

# GitHub Actions CI

## Purpose

Create a clear GitHub Actions workflow that validates the Python project on Ubuntu, Windows, and macOS, using the repository's dependency declaration and build/test scripts.

## Prerequisites

- Work from the repository root and inspect existing `.github/workflows/` files before editing.
- A working local project test workflow must be present or its intended paths and commands must be established: `requirements-dev.txt`, `scripts/build.py`, and `scripts/test.py` are the default conventions.
- Python version must come from existing project metadata or documentation; if none exists, select and document a supported stable Python 3 version consistently.
- Apply the Build Engineer agent's safety and idempotency rules; do not add secrets or commit changes.

## Inputs

- Existing workflow files, project Python-version requirements, dependency declarations, and build/test scripts.
- Repository event and branch conventions. The project context names `feature/develop` as the working branch and `develop` as the target; do not change branches.
- Available GitHub Actions runner labels and the required CI platforms.

## Actions

1. Inspect existing workflows and reuse or extend a suitable CI workflow; do not create a duplicate workflow for the same test job.
2. Create or update `.github/workflows/ci.yml` with a job strategy matrix that explicitly includes `ubuntu-latest`, `windows-latest`, and `macos-latest`.
3. Configure the workflow to check out the repository and set up the selected Python version with the maintained `actions/checkout` and `actions/setup-python` actions.
4. Use runner-neutral commands and matrix values; avoid shell syntax that works only on one operating system.
5. Install declared test dependencies using the matrix interpreter, for example `python -m pip install -r requirements-dev.txt`. Do not install unrelated or global dependencies.
6. Invoke the repository build and test scripts from the repository root: `python scripts/build.py`, then `python scripts/test.py`. The test script must execute pytest and propagate its exit code. Keep CI logs clear enough to identify the matrix OS/Python pair and the failing step.
7. Ensure each matrix job is independently visible and a nonzero build/test result fails that job. Do not mask errors with `continue-on-error`, `|| true`, or equivalent.
8. Validate workflow structure and commands locally where tooling permits. Check the matrix contains all three required OS labels, dependencies match the declared file, scripts exist, and test execution reaches pytest. State that remote GitHub execution cannot be confirmed from a local run.

## Outputs

- One maintainable GitHub Actions CI workflow, or a minimal update to an existing workflow.
- A concise report naming the workflow and describing local validation and any remote-only checks.

## Expected Files

- `.github/workflows/ci.yml` or the existing workflow file updated to meet these requirements.
- Existing `requirements-dev.txt` (or the repository's declared equivalent).
- Existing `scripts/build.py` and `scripts/test.py` (or equivalent repository scripts).

Create or edit only the workflow within this skill's responsibility unless a missing script/dependency declaration is an explicit blocker; report such a blocker rather than expanding scope without need.

## Validation Checks

- The workflow YAML parses with available validation tooling.
- The matrix includes Ubuntu, Windows, and macOS runners.
- Each job checks out source, sets up Python, installs the declared test dependencies, invokes the repository build/test scripts, and runs pytest through the test script.
- No operating-system-specific activation command is required in CI; each job uses the setup-python interpreter directly.
- Build or test failures remain visible as failed job/step results, and logs identify the failed step and matrix context.
- Workflow contains no credentials, tokens, unnecessary permissions, or generated files.
- Local execution of the referenced build/test scripts passes where the current environment supports it; remote workflow success is reported only after an actual GitHub Actions run.

## Expected Result

Every push or pull request covered by the workflow runs a distinct CI job on Ubuntu, Windows, and macOS. Each job installs the declared dependencies, runs the project build check and pytest, and reports a clear pass or failure.

## Typical Failure Scenario

The workflow passes on Ubuntu but fails on Windows because it uses POSIX activation or shell syntax, or because a required dependency/script is missing from the clean runner.

## Error Handling

- If an expected dependency or script is missing, verify the repository state and report the exact prerequisite. Do not write application source files as a workaround.
- If YAML validation fails, correct only the malformed workflow and rerun the same validation.
- If a command is platform-specific, replace it with a Python-based or otherwise runner-neutral invocation rather than suppressing the failing job.
- If a local platform cannot be tested, validate the workflow structure and available commands, then explicitly identify the untested operating systems; do not claim cross-platform CI passed.
- Never embed secrets in workflow YAML. Use GitHub Actions secrets only when a future, explicitly authorized workflow genuinely requires them; this Hello World CI should not need secrets.

## Idempotency Requirements

- Reuse an existing suitable workflow and retain unrelated jobs/triggers unless they conflict with the stated CI requirements.
- Do not add duplicate OS matrix entries, jobs, dependency installation, or workflow files.
- Keep Python version and dependency source aligned with project metadata and local build/test instructions.
- Do not change branches, commit, delete files, or leave generated artifacts as part of CI configuration.