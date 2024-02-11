from . import database_improved


def repr_players():
    team: dict[int, dict] = database_improved.get_team()
    for number, player in team.items():
        print(f"[Player {number}]: {player['name']}, {player['age']}")


def player_add(name: str, age: int, number: int) -> dict:
    player_data: dict = {
        "name": name,
        "age": age,
        "number": number,
    }
    created_player: dict = database_improved.save(id_=number, instance=player_data)
    return created_player


def player_delete(number: int) -> None:
    database_improved.delet(id_=number)


def player_update(number: int, name: str, age: int) -> dict:
    player_data: dict = {
        "name": name,
        "age": age,
        "number": number,
    }
    updated_player: dict = database_improved.update(id_=number, instance=player_data)
    return updated_player


def dispatcher(operation: str):
    operations = ("add", "del", "repr", "exit", "update")
    if operation not in operations:
        raise Exception(f"Operation: '{operation}' is not available\n")

    if operation == "exit":
        raise SystemExit("Bye! Exiting the application")

    elif operation == "repr":
        repr_players()

    elif operation == "add":
        user_data = input("Enter new player information[name, age, number]: ")
        user_items: dict[int, dict] = user_data.split(",")
        name, age, number = user_items
        player_add(name=name, age=int(age), number=int(number))
        print(f"Player {number} is added")

    elif operation == "update":
        user_data = input("Enter new player information[name, age, number]: ")
        user_items: dict[int, dict] = user_data.split(",")
        name, age, number = user_items
        try:
            updated_player: dict = player_update(
                number=int(number), name=name, age=int(age)
            )
        except ValueError:
            raise Exception("Age and number of player must be integers\n")
        else:
            print(
                f"Player [{number}] is updated:"
                f" Name [{updated_player['name']}]"
                f" Age [{updated_player['age']}]"
            )

    elif operation == "del":
        user_data = input("Enter player`s number[int]: ")
        try:
            _user_data = int(user_data)

        except ValueError:
            raise Exception("Age and number of player must be integers\n")
        else:
            player_delete(number=_user_data)
            print(f"Player: [{_user_data}] is removed")


def main():
    while True:
        operation = input("Please enter the oparation: ")
        try:
            dispatcher(operation=operation)
        except database_improved.databaseError as error:
            print(error)
        except SystemExit as error:
            print(error)
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
