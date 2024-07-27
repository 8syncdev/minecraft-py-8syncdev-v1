from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Entity, color, scene
from src.settings import *
from src.resources import (
    brick_texture,
)


class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = f'{MODEL_PATH}\\Block'
        self.texture = brick_texture
        self.origin_y = 0.5
        self.mouse_sensitivity = (200, 200)
        scale=(0.5, 1, 0.5)

    def input(self, key):
        if key == 't':
            self.camera_pivot.z_setter(-10)
            self.camera_pivot.y_setter(8)


class PlayerPresentation(Entity):
    def __init__(self, position=(5,5,5)):
        super().__init__(
            parent=scene,
            position=position,
            model=f'{MODEL_PATH}\\Block',
            texture=brick_texture,
            origin_y=0.5,
            color=color.red,
            highlight_color=color.lime,
            scale=(0.5, 1, 0.5)
        )
