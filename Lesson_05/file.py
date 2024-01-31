from pathlib import Path
from typing import Generator

current_path = Path(__file__).parent


def read_line(file_name: Path) -> Generator:
    with open(file=file_name) as file:
        line = file.readline()
        while True:
            yield line
            if not line:
                break


def analize_file(file_name: Path, pattern: str) -> int:
    total = 0
    for line in read_line(file_name=file_name):
        if pattern in line:
            total += 1

    return total


def main():
    file_name = current_path / "rockyou.txt"
    pattern = input("Writting word whiche we will found:")

    matches: int = analize_file(file_name=file_name, pattern=pattern)
    print(f"Analize matched: {matches} lines")


if __name__ == "__main__":
    main()
