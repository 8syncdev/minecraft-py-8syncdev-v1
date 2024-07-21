from ursinanetworking import (
    UrsinaNetworkingClient,
    EasyUrsinaNetworkingClient
)
from ursina import (
    Ursina, Entity, color, Vec3, camera, invoke,
    destroy
)
from src.entity.character import (
    PlayerRepresentation,
    Player
)


from src.entity.scene import Block
from random import randrange



# Initialize the client
client = UrsinaNetworkingClient("localhost", 25565)
easy_client = EasyUrsinaNetworkingClient(client)

SelfId = -1
PlayersTargetPosition = {}
Players = {}

# Set up block management
class BlockState:
    count = 0
    blocks = {}

Block.client = client

user = Player()

PlayerRepresentation.camera = user


class ClientService:

    @staticmethod
    def create_services():
        @client.event
        def onConnectionEstablished():
            print("Connected to server")
        
        @client.event
        def onConnectionError(reason):
            print(f"Connection error: {reason}")

        @client.event
        def get_id(id):
            global SelfId
            SelfId = id
            print(f"Received ID: {SelfId}")

        @easy_client.event
        def onReplicatedVariableUpdated(res_server):
            PlayersTargetPosition[res_server.name] = res_server.content['position']

        @easy_client.event
        def onReplicatedVariableCreated(res_server):
            print(f"Replicated variable created: {res_server.name}", res_server.content)

            var_name = res_server.name
            type_name = res_server.content['type']
            if type_name == 'player':
                PlayersTargetPosition[var_name] = Vec3(0, 0, 0)
                Players[var_name] = PlayerRepresentation()
                if SelfId == int(res_server.content["client_id"]):
                    Players[var_name].color = color.red
                    Players[var_name].visible = False if SelfId == int(res_server.content["client_id"]) else True

            elif type_name == 'block':
                BlockState.blocks[var_name] = Block(position=res_server.content['position'], name_block=var_name)
                BlockState.count += 1

        @easy_client.event
        def onReplicatedVariableRemoved(res_server):
            print(f"Replicated variable removed: {res_server.name}")
            var_name = res_server.name
            type_name = res_server.content['type']
            if type_name == 'player':
                PlayersTargetPosition.pop(var_name)
                Players.pop(var_name)
            elif type_name == 'block':
                destroy(BlockState.blocks[var_name])
                BlockState.blocks.pop(var_name)
                BlockState.count -= 1

        

    @staticmethod
    def event_update():
        easy_client.process_net_events()



def update_client_pos():
    # Send the player's new position to the server
    # print(type(player.position))
    if user.position[1] < -5:
        user.position = (randrange(0, 15), 10, randrange(0, 15))
    
    # print(f"User position: {user.position}")    
    # print(Players, PlayersTargetPosition)
    # Update player positions
    for player_id, target_pos in PlayersTargetPosition.items():
        if player_id in Players:
            Players[player_id].position += (Vec3(target_pos) - Players[player_id].position) / 25
        

    ClientService.event_update()

def input_client(key):
    
    # print(f"Key pressed: {key}")
    client.send_message('get_client_pos', tuple(user.position + (0, 1, 0))) 







