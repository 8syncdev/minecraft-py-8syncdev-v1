from src.settings import BASE_DIR
from ursina import *

app = Ursina()
from src.resources import * # tải tất cả các tài nguyên
from src.network.client import ClientService
ClientService.create_services()


from src.entity.scene import hand

# from src.entity.genmap import gen_map
# gen_map()

# from src.entity.character import character
from src.entity.event import update, input
mouse.locked=False
window.borderless=False
app.run()
