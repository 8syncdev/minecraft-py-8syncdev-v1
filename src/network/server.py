from ursinanetworking import (
    UrsinaNetworkingServer,
    UrsinaNetworkingConnectedClient,
    EasyUrsinaNetworkingServer
)
from time import sleep

# Initialize the server
server = UrsinaNetworkingServer("localhost", 25565)
easy_server = EasyUrsinaNetworkingServer(server)

class ServerService:

    @staticmethod
    def create_services():
        @server.event
        def onClientConnected(client: UrsinaNetworkingConnectedClient):
            print(f"Client connected: {client.id}")
            # Create a replicated variable for the player
            easy_server.create_replicated_variable(f'player_{client.id}', {'id': client.id, 'position': (0, 0, 0)})
            client.send_message('GetId', client.id)

        @server.event
        def get_new_position(client: UrsinaNetworkingConnectedClient, content):
            # Update the player's position
            easy_server.update_replicated_variable_by_name(f'player_{client.id}', 'position', content)

        ServerService.event_update()

    @staticmethod
    def event_update():
        while True:
            server.process_net_events()

# Run the server services
ServerService.create_services()
