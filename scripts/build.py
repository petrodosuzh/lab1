import ast
from pathlib import Path
import sys


def main():
    repository_root = Path(__file__).resolve().parents[1]
    source_root = repository_root / "src"
    source_files = sorted(source_root.rglob("*.py"))

    if not source_files:
        print(f"No Python source files found under {source_root}", file=sys.stderr)
        return 1

    try:
        for source_file in source_files:
            ast.parse(source_file.read_text(encoding="utf-8"), filename=str(source_file))
    except (OSError, SyntaxError, UnicodeDecodeError) as error:
        print(f"Build check failed: {error}", file=sys.stderr)
        return 1

    print(f"Build check passed ({len(source_files)} Python source file(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())