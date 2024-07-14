from ursina import (
    Button,
    destroy,
    scene,
    color,
    mouse,
)

import random

from src.resources import *
from src.settings import MODEL_PATH




class Block(Button):
    block_pick = 1

    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model=f'{MODEL_PATH}\\Block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                destroy(self)
            elif key == 'right mouse down':
                punch_sound.play()
                if Block.block_pick == 1:
                    voxel = Block(position=self.position + mouse.normal, texture=grass_texture)
                elif Block.block_pick == 2:
                    voxel = Block(position=self.position + mouse.normal, texture=stone_texture)
                elif Block.block_pick == 3:
                    voxel = Block(position=self.position + mouse.normal, texture=brick_texture)
                elif Block.block_pick == 4:
                    voxel = Block(position=self.position + mouse.normal, texture=dirt_texture)
                elif Block.block_pick == 5:
                    voxel = Block(position=self.position + mouse.normal, texture=wood_texture)
                