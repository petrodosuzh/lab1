from pathlib import Path
import sys


def main():
    source_dir = Path(__file__).resolve().parent / "src"
    sys.path.insert(0, str(source_dir))

    from hello_world.main import main as app_main

    app_main()
## sadasd

if __name__ == "__main__":
    main()