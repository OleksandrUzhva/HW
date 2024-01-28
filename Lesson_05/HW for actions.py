from pathlib import Path

current_path = Path(__file__).parent
with open(
    current_path / "rockyou.txt", "rt", encoding="utf-8", errors="replace"
) as file:
    file_content = file.read()

    search_string = input("Введіть строку для пошука: ")

    lines = file_content.split("\n")
    found_in_lines = [line for line in lines if search_string in line]

    if found_in_lines:
        print(
            f"Строка '{search_string}' знайдена в наступних ({len(found_in_lines)} шт.):"
        )

    else:
        print(f"Строка '{search_string}' не знайдена в файлі.")
