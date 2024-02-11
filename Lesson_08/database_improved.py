TEAM_TYPE = dict[int, dict]


class databaseError(Exception):
    pass


_TEAM: TEAM_TYPE = {
    1: {"name": "Jhon", "age": 20},
    3: {"name": "Joe", "age": 31},
    8: {
        "name": "Alex",
        "age": 29,
    },
    12: {"name": "Leo", "age": 25},
}


def get_team() -> TEAM_TYPE:
    return _TEAM


def save(id_: int, instance: dict, debug: bool = False) -> dict:
    if _TEAM.get(id_) is not None:
        raise databaseError(f"Instance with tis id: {id_} already exist ")
    else:
        _TEAM[id_] = instance
        return instance


def get(id_) -> dict:
    try:
        player = _TEAM[id_]
    except KeyError:
        raise databaseError(f"Id {id_} is not exist")
    else:
        return player


def update(id_: int, instance: dict, debug: bool = False) -> dict:
    player: dict = get(id_=id_)  # noqa
    _TEAM[id_] = instance

    return instance


def delet(id_: int, debug: bool = False) -> dict:
    player: dict = get(id_=id_)  # noqa
    del _TEAM[id_]
