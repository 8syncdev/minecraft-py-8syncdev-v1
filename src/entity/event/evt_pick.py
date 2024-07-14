from ursina import held_keys
from src.resources import *
from src.entity.scene import hand, Block

def evt_pick():
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: Block.block_pick = 1
    if held_keys['2']: Block.block_pick = 2
    if held_keys['3']: Block.block_pick = 3
    if held_keys['4']: Block.block_pick = 4
    if held_keys['5']: Block.block_pick = 5