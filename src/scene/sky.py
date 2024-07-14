from ursina import Entity, scene
from src.resources.textures import sky_texture

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="Sphere",
            texture=sky_texture,
            scale=150,
            double_sided=True
        )
