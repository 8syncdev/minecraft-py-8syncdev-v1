from src.resources.load_textures import (
    grass_texture,
    stone_texture,
    brick_texture,
    dirt_texture,
    wood_texture,
    sky_texture,
    arm_texture,
    # Sounds
    punch_sound,
)

DICT_TEXTURES = {
    'grass': {
        'type': 'block',
        'texture': grass_texture
    },
    'stone': {
        'type': 'block',
        'texture': stone_texture
    },
    'brick': {
        'type': 'block',
        'texture': brick_texture
    },
    'dirt': {
        'type': 'block',
        'texture': dirt_texture
    },
    'wood': {
        'type': 'block',
        'texture': wood_texture
    },
    'sky': {
        'type': 'sky',
        'texture': sky_texture
    },
    'arm': {
        'type': 'arm',
        'texture': arm_texture
    },
    'punch': {
        'type': 'sound',
        'texture': punch_sound
    }
}