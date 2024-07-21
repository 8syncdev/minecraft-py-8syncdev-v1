from ursinanetworking import (
    UrsinaNetworkingServer,
    UrsinaNetworkingConnectedClient,
    EasyUrsinaNetworkingServer
)
from time import sleep
# from src.entity.genmap import noise
from src.utils import gen_noise


# Initialize the server
server = UrsinaNetworkingServer("localhost", 25565)
easy_server = EasyUrsinaNetworkingServer(server)

class BlockState:
    count = 0
    blocks = {}

class ServerService:

    @staticmethod
    def create_services():
        @server.event
        def onClientConnected(client: UrsinaNetworkingConnectedClient):
            print(f"Client connected: {client.id}")
            # Create a replicated variable for the player
            easy_server.create_replicated_variable(f'player_{client.id}', {
                'type': 'player',
                'client_id': client.id,
                'position': (0, 0, 0),
            })
            client.send_message('get_id', client.id)

        @server.event
        def onClientDisconnected(client: UrsinaNetworkingConnectedClient):
            '''
                Tìm tới player_{client.id} trong content của client và xóa nó đi do dùng east_server.remove_replicated_variable_by_name
            '''
            print(f"Client disconnected: {client.id}")
            # Delete the replicated variable for the player
            easy_server.remove_replicated_variable_by_name(f'player_{client.id}')

        @server.event
        def request_destroy_block(client: UrsinaNetworkingConnectedClient, block_name):
            ServerService.remove_block(block_name)

        @server.event
        def request_create_block(client: UrsinaNetworkingConnectedClient, position):
            ServerService.create_block(position)

        @server.event
        def get_client_pos(client: UrsinaNetworkingConnectedClient, position):
            # print(f"Client {client.id} position: {position}")
            easy_server.update_replicated_variable_by_name(f'player_{client.id}', 'position', position)

        ServerService.gen_map()

        ServerService.event_update()

    @staticmethod
    def event_update():
        while True:
            easy_server.process_net_events()

    @staticmethod
    def create_block(position):
        count = BlockState.count
        block_name = f'block_{count}'
        easy_server.create_replicated_variable(block_name, {
            'type': 'block',
            'position': position,
        })
        BlockState.blocks[block_name] = {
            'type': 'block',
            'position': position,
        }
        BlockState.count += 1
    
    @staticmethod
    def remove_block(block_name):
        '''
            Send a message to all clients to remove the block
            
            `python
            content = {
                'type': 'block',
                'position': (x, y, z)
            }
            content.name = block_name # in ServerService.create_block
            `
        '''
        BlockState.blocks.pop(block_name)
        easy_server.remove_replicated_variable_by_name(block_name)

    @staticmethod
    def gen_map(space=35):
        for z in range(space):
            for x in range(space):
                # y = int(gen_noise()([x * 0.1, z * 0.1]) * 10)
                ServerService.create_block((x, 0, z))


# Run the server services
ServerService.create_services()
