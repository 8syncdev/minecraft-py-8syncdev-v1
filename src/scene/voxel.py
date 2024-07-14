from ursina import Button, mouse, destroy, scene, color
from src.resources.textures import grass_texture, stone_texture, brick_texture, dirt_texture, wood_texture, punch_sound
import random
from src.events.update import block_pick
from src.settings import MODEL_PATH

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model=str(MODEL_PATH / "Block"),
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.light_gray,
            scale=0.5
        )
    
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 5: voxel = Voxel(position=self.position + mouse.normal, texture=wood_texture)

            if key == "right mouse down":
                punch_sound.play()
                destroy(self)
