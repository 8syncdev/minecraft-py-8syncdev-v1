from src.entity.scene import Block
import random


voxel = {}

# def gen_map():
#     for z in range(20):
#         for x in range(20):
#             y = int(noise([x * 0.1, z * 0.1]) * 10)
#             block = Block(position=(x, y, z))
#             voxel[(x, z)] = block