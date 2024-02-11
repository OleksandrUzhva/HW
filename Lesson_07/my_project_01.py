team: list[dict] = [
    {"name": "Jhon", "age": 20, "number": 1},
    {"name": "Joe", "age": 31, "number": 7},
    {"name": "Alex", "age": 29, "number": 18},
    {"name": "Leo", "age": 25, "number": 35},
]


def repr_players(players: list[dict]) -> None:
    for team_player in players:
        print(
            f"[Player {team_player['number']}]: {team_player['name']}, {team_player['age']}"
        )
    return None


def player_add(name: str, age: int, number: int):
    for new_player in team:
        if new_player["number"] == number:
            print("Player with this number already exists.\nWrite other number")
            break
        else:
            add_player: dict = {
                "name": name,
                "age": age,
                "number": number,
            }

            team.append(add_player)
            return add_player


def player_delete(number: int) -> None:
    for player in team:
        if player["number"] == number:
            del player
    return None


def player_update(number: int, new_name: str, new_age: int) -> None:
    for update_player in team:
        if update_player["number"] == number:
            update_player["name"] = new_name
            update_player["age"] = new_age
            print(f"Player {number} updated successfully")
    return None


def main():
    operations: tuple[str, ...] = ("add", "del", "repr", "exit", "update")

    while True:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print(f"Operation: '{operation}' is not available\n")
            continue

        if operation == "exit":
            print("Bye")
            break
        elif operation == "repr":
            repr_players(team)
        elif operation == "add":
            user_data = input("Enter new player information[name, age, number]: ")
            user_items: list[str] = user_data.split(",")
            if len(user_items) != 3:
                print("You wrote incorrect information\n Try agein\n")
                continue
            name, age, number = user_items
            try:
                player_add(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number of player must be integers\n")
                continue
        elif operation == "update":
            number_player = input("Please write number, new name and new age player: ")
            user_number: list[str] = number_player.split(",")
            number, new_name, new_age = user_number
            try:
                player_update(
                    number=int(number), new_name=new_name, new_age=int(new_age)
                )
            except ValueError:
                print("Age and number of player must be integers\n")
                continue


if __name__ == "__main__":
    main()
