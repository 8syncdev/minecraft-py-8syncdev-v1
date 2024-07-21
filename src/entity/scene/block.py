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
    def __init__(self, 
                 position=(0, 0, 0),
                 name_block='block', 
                 texture=grass_texture
                 ):
        super().__init__(
            parent=scene,
            position=position,
            model=f'{MODEL_PATH}\\Block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )
        self.name_block = name_block

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)
                Block.client.send_message('request_destroy_block', self.name_block)
            elif key == 'left mouse down':
                punch_sound.play()
                if Block.block_pick == 1:
                    # voxel = Block(position=self.position + mouse.normal, texture=grass_texture)
                    Block.client.send_message('request_create_block', self.position + mouse.normal)
                elif Block.block_pick == 2:
                    # voxel = Block(position=self.position + mouse.normal, texture=stone_texture)
                    Block.client.send_message('request_create_block', self.position + mouse.normal)
                elif Block.block_pick == 3:
                    # voxel = Block(position=self.position + mouse.normal, texture=brick_texture)
                    Block.client.send_message('request_create_block', self.position + mouse.normal)
                elif Block.block_pick == 4:
                    # voxel = Block(position=self.position + mouse.normal, texture=dirt_texture)
                    Block.client.send_message('request_create_block', self.position + mouse.normal)
                elif Block.block_pick == 5:
                    # voxel = Block(position=self.position + mouse.normal, texture=wood_texture)
                    Block.client.send_message('request_create_block', self.position + mouse.normal)
    
    
                