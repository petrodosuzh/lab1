---
name: create-actions
description: "Create or update cross-platform GitHub Actions CI using the github-actions skill and the repository build/test scripts."
agent: "Build Engineer"
---

# create-actions

## Purpose

Create or update the Ubuntu, Windows, and macOS CI workflow by following the [github-actions skill](../skills/github-actions/SKILL.md).

## Prerequisites

- Run from the repository root after the build/test workflow exists.
- Inspect existing workflows, dependency declarations, and build/test scripts.
- Read and follow the linked skill; preserve unrelated workflow jobs and user changes.

## Actions

1. Reuse a suitable existing workflow or create `.github/workflows/ci.yml` if none exists.
2. Define a matrix with `ubuntu-latest`, `windows-latest`, and `macos-latest`.
3. Check out the repository, set up the project's supported Python version, install declared test dependencies, then run `python scripts/build.py` and `python scripts/test.py` from the repository root.
4. Ensure the test script runs pytest and a nonzero command result fails the job. Keep matrix and step results clear; do not mask failures.
5. Validate the workflow and referenced paths/commands, then report local results and whether a remote GitHub Actions run was actually observed.

## Expected Files

- `.github/workflows/ci.yml`, or the existing appropriate workflow updated in place.
- No application source files; use existing dependency and script files.

## Validation

- Workflow YAML parses with available tooling.
- The matrix explicitly contains Ubuntu, Windows, and macOS.
- Every job installs declared dependencies and invokes the build and test scripts; pytest runs through the test script.
- Runner commands are cross-platform and failures remain visible.
- No secrets or credentials are added.

## Error Handling

- If scripts/dependencies are missing, report the prerequisite rather than writing application code or silently skipping a step.
- If the workflow parser reports an error, fix only the workflow and rerun the same validation.
- If a platform cannot be run locally, state that limitation; do not claim remote CI success without a completed GitHub Actions run.

## Idempotency

- Do not add duplicate workflow files, jobs, matrix entries, or dependency-install steps.
- Retain existing valid triggers, permissions, and unrelated jobs unless they conflict with the requirements.
- Repeated runs should produce no further changes once the workflow meets the criteria.