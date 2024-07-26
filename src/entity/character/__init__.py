from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Entity, color, scene, load_texture
from src.settings import *
from src.resources import (
    brick_texture,
)


class Player(FirstPersonController):
    object_to_follow: Entity = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mouse_sensitivity = (155, 155)
        self.model = f'{MODEL_PATH}\\Block'
        self.texture = brick_texture
        self.origin_y = -0.5
        # self.color = color.black
        # self.highlight_color = color.black


    def input(self, key):
        super().input(key)
        if key == 't':
            # 3rd person view
            self.camera_pivot.z_setter(-10)
            self.camera_pivot.y_setter(10)
            

        
        

class PlayerRepresentation(Entity):
    camera = None

    def __init__(self, position = (5,5,5)):
        super().__init__(
            parent = scene,
            position = position,
            model = f'{MODEL_PATH}\\Block.obj',
            texture = brick_texture,
            double_sided = True,
            origin_y = .5,
            color = color.yellow,
            highlight_color = color.yellow,
            scale = (0.5, 1, 0.5),
        )




