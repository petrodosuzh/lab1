# Lab 1: Python Hello World

A minimal cross-platform Python Hello World application.

CI uses Python 3.14 on Ubuntu, Windows, and macOS.

## Run

From the repository root, run:

```sh
python run.py
```

Expected output:

```text
Hello, world!
```

## Development Setup

Create a virtual environment:

```sh
python -m venv .venv
```

Activate it in the shell you use:

- POSIX shells: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Windows Command Prompt: `.venv\Scripts\activate.bat`

Install the test dependency:

```sh
python -m pip install -r requirements-dev.txt
```

## Build and Test

Run these commands from the repository root with the virtual environment active:

```sh
python run.py
python scripts/build.py
python scripts/test.py
```