# Agent and Project Architecture

## Purpose

The repository contains a minimal Python project and a set of customization
files for GitHub Copilot in VS Code. The Build Engineer agent addresses these
problems:

- creates a consistent cross-platform Hello World scaffold;
- configures a local virtual environment, dependencies, and pytest;
- provides repeatable build/test commands;
- creates GitHub Actions CI for Ubuntu, Windows, and macOS;
- validates structure, behavior, ignore rules, and CI without hiding failures;
- preserves existing changes, does not commit or switch branches, and does not
  create secrets.

The agent is not a runtime component of the application. It orchestrates changes
and checks in the repository. The runtime process is separate: `run.py` calls the
Python entry point.

## Client and Directory Conventions

The customization is implemented for **GitHub Copilot in VS Code**. It uses the
following workspace conventions:

- `.github/agents/*.agent.md` - custom agents;
- `.github/prompts/*.prompt.md` - user-invocable prompts/commands;
- `.github/skills/<name>/SKILL.md` - on-demand skills;
- `.github/workflows/*.yml` - GitHub Actions, not Copilot customization.

Another AI client may use different directories or extensions, such as
`.agents/skills/<name>/`, `.claude/skills/<name>/`, `AGENTS.md`,
`copilot-instructions.md`, `*.md`, or its own slash-command format. This
repository has no such alternative files: its primary format is `.agent.md`,
`.prompt.md`, and `SKILL.md` under `.github/`. When porting the setup, preserve
the roles and dependencies described below, but adapt paths and frontmatter to
the conventions of the specific client.

## Agent and Skills

### Build Engineer

`.github/agents/build-engineer.agent.md` defines the agent, its area of
responsibility, allowed operations, and restrictions. The agent follows the
inspect -> identify -> implement -> validate -> report cycle. Its available tool
classes are `read`, `search`, `edit`, and `execute`.

### Skills

- `project-scaffold` in `.github/skills/project-scaffold/SKILL.md` describes
  `src/hello_world/main.py`, `run.py`, README, `.gitignore`, and launch
  validation.
- `build-and-test` in `.github/skills/build-and-test/SKILL.md` describes `.venv`,
  `requirements-dev.txt`, pytest, `pyproject.toml`, build/test scripts, and
  local validation.
- `github-actions` in `.github/skills/github-actions/SKILL.md` describes the CI
  matrix, dependencies, runner-neutral commands, and workflow validation.

Skills are not separate commands. The corresponding prompts load them through
links and `description` when a specific stage is executed.

## Commands and Execution Order

The following prompt commands are available to the user:

| Command | Role |
| --- | --- |
| `init` | Full orchestrator with a fixed execution order |
| `git-init` | Verify Git and add safe `.gitignore` rules |
| `create-project` | Create/verify the Python scaffold and launch the application |
| `create-build` | Configure venv, pytest, dependencies, and local scripts |
| `create-actions` | Create/verify cross-platform GitHub Actions |
| `check` | Perform a comprehensive read-only repository check |

`init` runs `git-init` -> `create-project` -> `create-build` -> `create-actions`
-> `check` in order. Each stage must complete its checks before the next one
starts. Developers can also run these shell commands directly:

```text
python run.py
python scripts/build.py
python scripts/test.py
```

## Data Between Stages

The orchestrator does not pass large objects or hidden state between prompts.
The contract consists of the working-tree state and command results:

1. `git-init` passes the verified Git root, current status, and existing ignore
   rules to later stages.
2. `create-project` passes the agreed application paths, launcher, the
   `python run.py` command, and the launch result.
3. `create-build` uses those paths and adds the dependency declaration, pytest
   configuration, tests, build/test scripts, and venv rules.
4. `create-actions` reads those files and puts the same dependency, build, and
   test commands into the workflow for each runner.
5. `check` reads the final tree, configuration, and Git status and returns a
   read-only report.

At the process level, data is passed through stdout/stderr and exit codes. A
successful stage returns code `0`; a nonzero code signals an error. Secrets and
credentials are not passed between stages.

## Error Handling

The orchestrator is a fail-fast pipeline. If a stage fails a required check,
`init` stops, identifies the failed stage and command or check, shows concise
evidence, and suggests the next correction. Later stages are not started
automatically. Recovery does not delete files, recreate the venv without need,
switch branches, or commit changes.

At runtime:

- `scripts/build.py` returns `1` if source files are missing or AST parsing/file
  reading fails;
- `scripts/test.py` forwards pytest's exit code;
- `run.py` does not catch import/runtime exceptions, so they produce a traceback
  and a nonzero exit code;
- GitHub Actions does not use `continue-on-error` or `|| true`, so a build/test
  failure makes the matrix job fail.

## File-to-Role Mapping

| File | Role |
| --- | --- |
| `.github/agents/build-engineer.agent.md` | Custom agent rules and restrictions |
| `.github/prompts/init.prompt.md` | Main orchestrator and stage order |
| `.github/prompts/git-init.prompt.md` | Git/status/`.gitignore` stage |
| `.github/prompts/create-project.prompt.md` | Scaffold and launch-validation stage |
| `.github/prompts/create-build.prompt.md` | Venv, pytest, and local workflow stage |
| `.github/prompts/create-actions.prompt.md` | CI workflow stage |
| `.github/prompts/check.prompt.md` | Final read-only validation |
| `.github/skills/project-scaffold/SKILL.md` | Minimal Python scaffold rules |
| `.github/skills/build-and-test/SKILL.md` | Dependency, test, and script rules |
| `.github/skills/github-actions/SKILL.md` | Cross-platform CI rules |
| `.github/workflows/ci.yml` | CI on Ubuntu, Windows, and macOS with Python 3.14 |
| `src/hello_world/main.py` | Runtime entry point that prints the greeting |
| `run.py` | Root launcher that adds `src` to the import path and calls the app |
| `scripts/build.py` | AST syntax/build check for `src/**/*.py` |
| `scripts/test.py` | Runs pytest with the current Python and forwards its exit code |
| `tests/test_main.py` | Verifies the application's stdout and stderr |
| `pyproject.toml` | Pytest test path and `src` Python path |
| `requirements-dev.txt` | Development dependency: pytest |
| `README.md` | Run, venv, dependency-installation, and validation commands |
| `.gitignore` | Excludes venv, cache, coverage, and build artifacts |
| `docs/architecture.md` | This architecture and file-role documentation |

In summary, prompts define orchestration, skills define repeatable procedures,
Python scripts perform checks, and CI repeats the same checks in a clean
environment across three operating systems.