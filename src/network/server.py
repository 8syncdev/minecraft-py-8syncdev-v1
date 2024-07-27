from ursinanetworking import (
    UrsinaNetworkingServer,
    UrsinaNetworkingConnectedClient,
    EasyUrsinaNetworkingServer,
)

from src.utils.noise import gen_noise


server = UrsinaNetworkingServer('localhost', 25565)
easy_server = EasyUrsinaNetworkingServer(server)

class BlockState:
    count = 0
    blocks = {}


class ServerService:

    @staticmethod
    def create_services():

        @server.event
        def onClientConnected(client: UrsinaNetworkingConnectedClient):
            print(f'Client {client.id} connected')
            easy_server.create_replicated_variable(f'player_{client.id}', {
                'type': 'player',
                'position': (0, 0, 0),
                'client_id': client.id
            })
            client.send_message('connected', {'id': client.id})

        @server.event
        def onClientDisconnected(client: UrsinaNetworkingConnectedClient):
            print(f'Client {client.id} disconnected')
            easy_server.remove_replicated_variable_by_name(f'player_{client.id}')

        @server.event
        def request_destroy_block(client: UrsinaNetworkingConnectedClient, name_block: str):
            ServerService.remove_block(name_block)
        
        @server.event
        def request_create_block(client: UrsinaNetworkingConnectedClient, position: tuple):
            ServerService.create_block(position)

        @server.event
        def get_client_position(client: UrsinaNetworkingConnectedClient, position: tuple):
            easy_server.update_replicated_variable_by_name(f'player_{client.id}', 'position', position)

        ServerService.gen_map()

        ServerService.run_server()
    
    @staticmethod
    def run_server():
        while True:
            easy_server.process_net_events()


        
    @staticmethod
    def create_block(position):
        count = BlockState.count
        block_name = f'block_{count}'
        easy_server.create_replicated_variable(block_name, {
            'type': 'block',
            'position': position,
            'name': block_name
        })

        BlockState.blocks[block_name] = {
            'type': 'block',
            'position': position,
            'name': block_name
        }
        BlockState.count += 1

    @staticmethod
    def remove_block(name):
        easy_server.remove_replicated_variable_by_name(name)
        BlockState.blocks.pop(name)

    @staticmethod
    def gen_map():
        for z in range(30):
            for x in range(30):
                y = int(gen_noise()([x * 0.1, z * 0.1]) * 10)
                ServerService.create_block((x, y, z))

ServerService.create_services()

