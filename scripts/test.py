from pathlib import Path
import subprocess
import sys


def main():
    repository_root = Path(__file__).resolve().parents[1]
    result = subprocess.run([sys.executable, "-m", "pytest"], cwd=repository_root)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())