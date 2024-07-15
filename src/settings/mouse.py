from ursina import mouse

def setup_mouse():
    mouse.visible = True
    mouse.locked = False
    mouse.position = (0, 0)
    mouse.smooth_scroll = True
    mouse.scroll_speed = 1
    mouse.sensitivity = (2, 2)
    mouse.drag = 0.9
    mouse.ignore = False
    mouse.velocity = (0, 0)
    mouse.delta = (0, 0)
    mouse.last_click = 0
    mouse.double_click_time = 0.25
    mouse.double_click = False
    mouse.double_click_position = (0, 0)
    mouse.double_click_time = 0.25
    mouse.double_click = False
    mouse.double_click_position = (0, 0)
    mouse.left = False
    mouse.right = False
    mouse.middle = False
    mouse.delta_time = 0
    mouse.delta_time_smooth = 0
    mouse.delta_time_smoothed = 0
    mouse.delta_time_raw = 0
    mouse.delta_time_raw_smoothed = 0