---
name: git-init
description: "Verify the lab1 Git repository, add or update safe Python ignore rules, and report Git status."
agent: "Build Engineer"
---

# git-init

## Purpose

Verify repository Git state, ensure `.gitignore` excludes local Python environments and generated files, and show the resulting Git status.

## Prerequisites

- Run at the repository root in the Build Engineer agent.
- Preserve existing user changes. Do not change branches, stage files, or commit.

## Actions

1. Verify this is a Git worktree with `git rev-parse --show-toplevel`. Stop if it is not; do not run `git init`.
2. Inspect the existing `.gitignore` and Git status before editing.
3. Create `.gitignore` only if missing. Otherwise append only missing relevant patterns, retaining all existing rules. Ensure it ignores `.venv/`, `venv/`, `__pycache__/`, `*.py[cod]`, `.pytest_cache/`, `.coverage`, `build/`, `dist/`, and `*.egg-info/`.
4. Show status with `git status --short --branch` and report the repository root and changed paths.

## Expected Files

- `.gitignore` only if it is missing or needs relevant ignore patterns.

## Validation

- `git rev-parse --show-toplevel` succeeds and identifies this repository.
- `git check-ignore -v .venv/ __pycache__/ .pytest_cache/` confirms applicable ignore rules.
- `git status --short --branch` completes and is reported accurately.
- No file was staged or committed.

## Error Handling

- If Git is unavailable or the directory is not a worktree, stop and report the exact command/error without initializing a repository.
- If `.gitignore` has user-specific or conflicting rules, preserve them and add only non-conflicting missing patterns; explain any unresolved conflict.
- If an ignore check fails, inspect the effective rules and make only the smallest necessary `.gitignore` update, then rerun the check.

## Idempotency

- Detect existing rules before editing; do not duplicate patterns.
- Do not rewrite a correct `.gitignore` or change unrelated Git state.
- Repeated runs should leave `.gitignore` unchanged after the required rules exist.