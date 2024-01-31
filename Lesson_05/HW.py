import time
from pathlib import Path

start_time = time.time()

current_path = Path(__file__).parent
with open(
    current_path / "rockyou.txt", "rt", encoding="utf-8", errors="replace"
) as file:
    file_content = file.read()

    search_string = input("Please enter a search word: ")

    lines = file_content.split()
    found_in_lines = [line for line in lines if search_string == line]

    if found_in_lines:
        print(f"Words'{search_string}' found in  ({len(found_in_lines)} ps.):")

    else:
        print(f"words '{search_string}' weren`t found.")

stop_time = time.time()
operating_time = stop_time - start_time
print(f"Operating time: {operating_time} sec")
