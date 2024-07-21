from perlin_noise import PerlinNoise
from src.entity.scene import Block
import random

noise = PerlinNoise(octaves=3, seed=random.randint(0, 100000000))

class Voxel:
    voxels = {}


# def gen_map():
#     for z in range(20):
#         for x in range(20):
#             y = int(noise([x * 0.1, z * 0.1]) * 10)
#             block = Block(position=(x, y, z))
#             Voxel.voxels[(x, z)] = block





