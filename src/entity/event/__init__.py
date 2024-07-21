from src.entity.event.evt_pick import evt_pick
# from src.entity.event.evt_distance import evt_distance
from src.network.client import update_client_pos, input_client

def update():
    evt_pick()
    # evt_distance()
    update_client_pos()
    ...


def input(key):
    input_client(key)
    ...