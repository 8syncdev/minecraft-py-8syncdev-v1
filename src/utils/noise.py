from perlin_noise import PerlinNoise
import random

def gen_noise(value: int = 100000000) -> PerlinNoise:
    noise = PerlinNoise(octaves=3, seed=random.randint(0, value))
    return noise
