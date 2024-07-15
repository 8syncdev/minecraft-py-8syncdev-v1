from src.settings import (
    BASE_DIR,
    setup_settings
)
from ursina import *

app = Ursina()

from src.resources import * # tải tất cả các tài nguyên

from src.entity.scene import sky, hand, Block

from src.entity.genmap import gen_map
gen_map()

from src.entity.character import character
from src.entity.event import update

setup_settings()

app.run()
