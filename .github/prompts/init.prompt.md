---
name: init
description: "Initialize and validate the lab1 Python project by running git-init, create-project, create-build, create-actions, then check in order."
agent: "Build Engineer"
---

# init

## Purpose

Orchestrate the full lab1 project setup in a fixed order by following the five stage prompts: [git-init](./git-init.prompt.md), [create-project](./create-project.prompt.md), [create-build](./create-build.prompt.md), [create-actions](./create-actions.prompt.md), and [check](./check.prompt.md).

## Prerequisites

- Run at the repository root with the Build Engineer agent.
- Python 3 and Git must be available. Network access may be needed only to install declared dependencies.
- Preserve user changes; do not change branches, stage, or commit files.
- Read the five linked stage prompts and their linked skills before starting, so their procedures and stop conditions are clear.

## Actions

Run each stage in this exact order, completing and evaluating its validation before starting the next:

1. **git-init**: follow [git-init.prompt.md](./git-init.prompt.md).
2. **create-project**: follow [create-project.prompt.md](./create-project.prompt.md).
3. **create-build**: follow [create-build.prompt.md](./create-build.prompt.md).
4. **create-actions**: follow [create-actions.prompt.md](./create-actions.prompt.md).
5. **check**: follow [check.prompt.md](./check.prompt.md).

Treat a reported stage failure, unmet required validation, or unresolved conflict as a failure. Stop immediately at that stage, do not start subsequent stages, and report the failed stage, evidence, and next corrective action. Continue only when the current stage's required checks pass. At completion, summarize all five stage outcomes and final check results.

## Expected Files

- `.gitignore`
- `src/hello_world/main.py`
- `run.py`
- `README.md`
- `requirements-dev.txt` or equivalent dependency declaration
- `pyproject.toml` or equivalent pytest configuration
- `tests/test_main.py` or equivalent focused tests
- `scripts/build.py` and `scripts/test.py` or existing equivalents
- `.github/workflows/ci.yml` or an existing suitable CI workflow
- Local `.venv/` may exist after `create-build`, but must be ignored and never committed.

## Validation

- Each stage reports its required checks and passes before the next stage starts.
- The final `check` confirms repository structure, Python application, tests, scripts, CI YAML, ignore rules, and unchanged workspace state during that read-only stage.
- No required stage is skipped or reordered. Remote CI is reported as unverified unless a GitHub Actions run actually completed.

## Error Handling

- On any required stage failure, stop the sequence immediately. Do not continue to later prompts or hide the failure.
- Do not automatically delete files, recreate `.venv`, overwrite correct configuration, or commit changes while recovering.
- Report stage name, command/check that failed, concise error evidence, and a safe next step. Resume only when the user reruns or explicitly authorizes the failed stage.
- If an environment limitation blocks validation, classify the stage as not passed and stop if that validation is required for the stage.

## Idempotency

- Before every stage change, follow that stage's inspect-before-create and preserve-existing-files rules.
- Re-running `init` must reuse valid project files, configuration, and a healthy `.venv`, without duplicate rules, tests, workflows, or generated files.
- `check` remains read-only; the orchestrator does not stage, commit, switch branches, or clean user files.