team: list[str] = ["Jhon", "Mark", "Joy", "Luck"]

# player = iter(team)
# print(next(player))


def for_loop(collection):
    player = iter(collection)
    while True:
        try:
            print(next(player))
        except StopIteration:
            break


players = for_loop(team)
print(players)
