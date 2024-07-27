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
    client = None

    def __init__(self, position=(0, 0, 0), block_name: str = None, texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model=f'{MODEL_PATH}\\Block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )
        self.block_name = block_name

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                Block.client.send_message('request_destroy_block', self.block_name)
            elif key == 'right mouse down':
                punch_sound.play()
                if Block.block_pick == 1:
                    Block.client.send_message('request_create_block', self.position + mouse.normal)


                