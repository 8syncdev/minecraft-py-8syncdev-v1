from src.settings import (
    BASE_DIR,
    setup_settings
)
from ursina import *

# smartphones
window.borderless = False

app = Ursina()
from src.resources import * # tải tất cả các tài nguyên
from src.network.client import ClientService
ClientService.create_services()

from src.entity.scene import hand
# gen map from server side


# from src.entity.character import user
from src.entity.event import update, input

setup_settings()

app.run()
