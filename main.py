from turtle import *
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Tải các tài nguyên
from src.resources.textures import grass_texture, stone_texture, brick_texture, dirt_texture, wood_texture, sky_texture, arm_texture, punch_sound

# Tắt nút thoát
window.exit_button.visible = False

# Cập nhật mỗi khung hình
from src.events.update import update, block_pick

# Import các lớp trong scene
from src.scene.voxel import Voxel
from src.scene.sky import Sky
from src.scene.hand import hand

# Tầm nhìn của người chơi (khoảng cách render)
render_distance = 10

# Tạo và lưu trữ các voxel
voxels = {}

for z in range(-render_distance, render_distance):
    for x in range(-render_distance, render_distance):
        voxel = Voxel(position=(x, 0, z))
        voxels[(x, z)] = voxel

# Hàm cập nhật tầm nhìn
def update():
    global render_distance

    player_x = int(player.position.x)
    player_z = int(player.position.z)

    for z in range(player_z - render_distance, player_z + render_distance):
        for x in range(player_x - render_distance, player_x + render_distance):
            if (x, z) not in voxels:
                voxel = Voxel(position=(x, 0, z))
                voxels[(x, z)] = voxel

# Khởi tạo các thực thể khác
player = FirstPersonController()
sky = Sky()

# Chạy ứng dụng
app.run()
