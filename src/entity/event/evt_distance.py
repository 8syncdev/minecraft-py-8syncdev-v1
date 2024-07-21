from src.entity.genmap import Voxel, noise
from src.entity.character import character
from src.entity.scene import Block


distance = 10
def evt_distance():
    player_x = int(character.position.x)
    player_z = int(character.position.z)

    for z in range(player_z - distance, player_z + distance):
        for x in range(player_x - distance, player_x + distance):
            if (x, z) not in Voxel.voxels:
                y = int(noise([x * 0.1, z * 0.1]) * 10)
                block = Block(position=(x, y, z))
                Voxel.voxels[(x, z)] = block