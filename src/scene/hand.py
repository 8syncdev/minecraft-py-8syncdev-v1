from ursina import Entity, camera, Vec3, Vec2
from src.resources.textures import arm_texture
from src.settings import MODEL_PATH

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model=str(MODEL_PATH / "Arm"),
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6)
        )
    
    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)
    


hand = Hand()