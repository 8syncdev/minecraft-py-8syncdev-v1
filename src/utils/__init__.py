from perlin_noise import PerlinNoise
import random


def gen_noise():
    noise = PerlinNoise(octaves=3, seed=random.randint(0, 100000000))
    return noise