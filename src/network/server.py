from ursinanetworking import (
    UrsinaNetworkingServer,
    UrsinaNetworkingConnectedClient
)


server = UrsinaNetworkingServer(
    "localhost", 
    25565
)

class ServerService:

    @staticmethod
    def create_services():
        @server.event
        def onClientConnected(client: UrsinaNetworkingConnectedClient):
            print(f"Client connected: {client.id}")

        while True:
            ServerService.event_update()

    @staticmethod
    def event_update():
        server.process_net_events()

ServerService.create_services()
        