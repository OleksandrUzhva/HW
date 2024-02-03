team: list[str] = ["Jhon", "Mark", "Joy", "Luck"]


def get_player():
    for player in team:
        yield player


for player in get_player():
    print(player)
