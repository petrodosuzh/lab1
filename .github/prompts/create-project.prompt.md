---
name: create-project
description: "Create the minimal cross-platform Python Hello World project by following the project-scaffold skill."
agent: "Build Engineer"
---

# create-project

## Purpose

Create and launch-validate the minimal Python Hello World application using the [project-scaffold skill](../skills/project-scaffold/SKILL.md).

## Prerequisites

- Run from the repository root after `git-init` has verified the worktree.
- Python 3 is available for launch validation.
- Read and follow the linked skill's full workflow, safety, and idempotency instructions.

## Actions

1. Inspect current files and status; follow the linked `project-scaffold` skill rather than inventing a second layout.
2. Create only missing project scaffold files and preserve correct existing files.
3. Launch the Hello World app using the script and command documented by the skill.
4. Report changed files and the exact launch validation result.

## Expected Files

- `src/hello_world/main.py`
- `run.py`
- `README.md`
- `.gitignore` (only if missing or incomplete; preserve existing rules)

## Validation

- Required scaffold files exist and their roles match the skill.
- The documented launch command works from the repository root, prints the expected greeting, and exits with status 0.
- No virtual environment, cache, or generated artifact is added to source control.

## Error Handling

- If an expected path contains unrelated user work, do not overwrite it; adapt to the existing correct layout or stop and report the conflict.
- If Python is unavailable or launch fails, report the exact command and error. Fix only scaffold-caused defects and rerun the launch check.
- Do not claim launch success when it was not verified.

## Idempotency

- Follow the skill's inspect-before-create rule and add only missing content.
- Repeated runs must not create duplicate launchers, source packages, README sections, or ignore rules.