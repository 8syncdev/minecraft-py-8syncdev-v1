# Thư viện load các tài nguyên cần thiết cho game
from ursina import (
    load_texture,
    Audio,
)

# Lấy đường dẫn tới thư mục chứa tài nguyên
from src.settings import *


# load các tài nguyên cần thiết cho game
grass_texture = load_texture(f'{TEXTURE_PATH}\\Grass_Block.png')
stone_texture = load_texture(f'{TEXTURE_PATH}\\Stone_Block.png')
brick_texture = load_texture(f'{TEXTURE_PATH}\\Brick_Block.png')
dirt_texture = load_texture(f'{TEXTURE_PATH}\\Dirt_Block.png')
wood_texture = load_texture(f'{TEXTURE_PATH}\\Wood_Block.png')
sky_texture = load_texture(f'{TEXTURE_PATH}\\Skybox.png')
arm_texture = load_texture(f'{TEXTURE_PATH}\\Arm_Texture.png')

# load các âm thanh cần thiết cho game
punch_sound = Audio(f'{SFX_PATH}\\Punch_sound.wav', loop=False, autoplay=False)

# load các textures character cần thiết cho game
character_texture = load_texture(f'{TEXTURE_PATH}\\character\\Butcher.png')