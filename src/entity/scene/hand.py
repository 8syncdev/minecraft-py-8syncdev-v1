from ursina import (
    Entity,
    camera,
    Vec3,
    Vec2,
)

from src.resources import arm_texture
from src.settings import MODEL_PATH

class Hand(Entity):
    def __init__(self):
        self.passive_pos = Vec2(0.3, -0.6)
        self.active_pos = Vec2(0.3, -0.5)
        super().__init__(
            parent=camera.ui,
            model=f'{MODEL_PATH}\\Arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=self.passive_pos
        )

    def active(self):
        self.position = self.active_pos

    def passive(self):
        self.position = self.passive_pos

hand = Hand()