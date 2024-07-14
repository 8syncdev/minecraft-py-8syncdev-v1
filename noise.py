from perlin_noise import PerlinNoise
import random

noise = PerlinNoise (octaves=3,seed=random.randint(1,1000000))

for z in range(-10,10):
    for x in range(-10,10):
        y = noise([x * .02,z * .02])
        y = math.floor(y * 7.5)
        voxel = Voxel(position=(x,y,z))