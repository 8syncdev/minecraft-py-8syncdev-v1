from ursinanetworking import (
    UrsinaNetworkingClient,
    EasyUrsinaNetworkingClient,
)

from src.entity.character import Player, PlayerPresentation
from ursina import color, destroy

from ursina import Vec3
from src.entity.scene import Block

import random

ClientId = -1
PlayersTargetPosition = {}
Players={}


class BlockState:
    count = 0
    blocks = {}


user = Player()


client = UrsinaNetworkingClient('localhost', 25565)
easy_client = EasyUrsinaNetworkingClient(client)


Block.client = client

class ClientService:

    @staticmethod
    def create_services():

        @client.event
        def onConnectionEstablished():
            print('Connected to server')
        
        @client.event
        def onConnectionError(reason):
            print(f'Connection error: {reason}')

        @client.event
        def connected(data):
            global ClientId
            print('Data', data)
            ClientId = data['id']

        @easy_client.event
        def onReplicatedVariableCreated(res_server):
            var_name=res_server.name
            type_name=res_server.content['type']

            if type_name == 'player':
                PlayersTargetPosition[var_name] =Vec3(0,0,0)
                Players[var_name]=PlayerPresentation()
                if ClientId == int(res_server.content['client_id']):
                    Players[var_name].color=color.yellow
                    Players[var_name].visible=False
            
            elif type_name == 'block':
                BlockState.blocks[var_name] = Block(res_server.content['position'], block_name=var_name)
                BlockState.count += 1

        @easy_client.event
        def onReplicatedVariableUpdated(res_server):
            PlayerPresentation[res_server.name] = res_server.content['position']

        @easy_client.event
        def onReplicatedVariableRemoved(res_server):
            var_name=res_server.name
            type_name=res_server.content['type']

            if type_name == 'player':
                PlayersTargetPosition.pop(var_name)
                Players.pop(var_name)
            elif type_name == 'block':
                destroy(BlockState.blocks[var_name])
                BlockState.blocks.pop(var_name)
                BlockState.count -= 1

    @staticmethod
    def run_client():
        easy_client.process_net_events()


def run_client():
    if user.position[1] < -5:
        user.position = (random.randrange(0, 20), 20, random.randrange(0, 20))

    for player_id, target_position in PlayersTargetPosition.items():
        Players[player_id].position += (Vec3(target_position) - Players[player_id].position) / 20

    ClientService.run_client()

def input_client(key):
    client.send_message('get_client_position', user.position + (0, 1, 0))