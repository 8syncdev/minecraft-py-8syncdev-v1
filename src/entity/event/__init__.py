from src.entity.event.evt_pick import evt_pick
# from src.entity.event.evt_distance import evt_distance
from src.network.client import run_client, input_client

def update():
    run_client()
    evt_pick()
    # evt_distance()
    ...

def input(key):
    input_client(key)