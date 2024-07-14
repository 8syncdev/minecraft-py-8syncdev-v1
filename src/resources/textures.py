from ursina import load_texture, Audio
from src.settings import (
    MODEL_PATH,
    SFX_PATH,
    TEXTURE_PATH
)

# Tải các texture
grass_texture = load_texture(str(TEXTURE_PATH / "Grass_Block.png"))
stone_texture = load_texture(str(TEXTURE_PATH / "Stone_Block.png"))
brick_texture = load_texture(str(TEXTURE_PATH / "Brick_Block.png"))
dirt_texture = load_texture(str(TEXTURE_PATH / "Dirt_Block.png"))
wood_texture = load_texture(str(TEXTURE_PATH / "Wood_Block.png"))
sky_texture = load_texture(str(TEXTURE_PATH / "Skybox.png"))
arm_texture = load_texture(str(TEXTURE_PATH / "Arm_Texture.png"))

# Tải âm thanh
punch_sound = Audio(str(SFX_PATH / "Punch_Sound.wav"), loop=False, autoplay=False)
