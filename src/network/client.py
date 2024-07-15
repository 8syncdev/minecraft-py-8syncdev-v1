from ursinanetworking import (
    UrsinaNetworkingClient,
)

client = UrsinaNetworkingClient(
    "localhost", 
    25565
)

class ClientService:

    @staticmethod
    def create_services():
        @client.event
        def onConnectionEstablished():
            print("Connected to server")
        
        @client.event
        def onConnectionError(reason):
            print(f"Connection error: {reason}")


        while True:
            ClientService.event_update()
    
        
    @staticmethod
    def event_update():
        client.process_net_events()

ClientService.create_services()

