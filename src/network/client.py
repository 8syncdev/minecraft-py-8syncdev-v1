from ursinanetworking import (
    UrsinaNetworkingClient,
    EasyUrsinaNetworkingClient
)
from ursina import Ursina, Entity, color, Vec3, camera, invoke
from src.entity.character import character as player

class PlayerRepresentation(Entity):
    def __init__(self, position=(0, 0, 0)):
        super(PlayerRepresentation, self).__init__(
            model='cube', scale=(0.5, 1, 0.5), color=color.white, origin_y=0.5, position=position, texture='white_cube'
        )

# Initialize the client
client = UrsinaNetworkingClient("localhost", 25565)
easy_client = EasyUrsinaNetworkingClient(client)

SelfId = -1
PlayersTargetPosition = {}
Players = {}

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
        def GetId(content):
            global SelfId
            SelfId = content

        @easy_client.event
        def onReplicatedVariableUpdated(content):
            PlayersTargetPosition[content.name] = content.content['position']

        @easy_client.event
        def onReplicatedVariableCreated(content):
            PlayersTargetPosition[content.name] = Vec3(0, 0, 0)
            Players[content.name] = PlayerRepresentation()
            if SelfId == int(content.content['id']):
                Players[content.name].visible = False

        # invoke(ClientService.event_update, delay=0.1)  # To continuously call event_update

        ClientService.event_update()
        

    @staticmethod
    def event_update():
        client.process_net_events()
        # invoke(ClientService.event_update, delay=0.1)  # Schedule the next event update

def update():
    # Send the player's new position to the server
    if SelfId != -1:  # Ensure the player ID is received before sending positions
        client.send_message('get_new_position', tuple(player.position + (0, 1, 0)))
        try:
            for p in Players:
                if p != f'player_{SelfId}':  # Only update positions for other players
                    Players[p].position = Vec3(PlayersTargetPosition[p])
        except KeyError:
            pass
        # Update the camera position to follow the player in third-person view
        camera.position = player.position + Vec3(0, 10, -20)
        camera.look_at(player.position + Vec3(0, 1, 0))
        # Process network events
        ClientService.event_update()

# Initialize the player and ground
# player = Entity(model='cube', scale=(0.5, 1, 0.5), color=color.red, position=(0, 0, 0))
# ground = Entity(model='plane', collider='box', scale=20, texture='grass')

